"""Reconcile scoped memory records while exposing conflicts and expiry."""
from runtime import *

def process(data):
    scope=text(data["scope"],"scope")
    now=instant(data["as_of"])
    grouped={}
    for row in records(data,"observations"):
        key=text(row.get("key"),"key")
        text(row.get("scope"),"scope")
        text(row.get("source"),"source")
        when=instant(row["updated_at"])
        if when>now: raise ValueError("observation is in the future")
        if key.casefold() in {"password","api_key","token","credential","secret"}:
            raise ValueError("credentials must not be stored in this ledger")
        if "value" not in row: raise ValueError("value is required")
        if type(row.get("deleted",False)) is not bool: raise ValueError("deleted must be boolean")
        if row.get("expires_at"): instant(row["expires_at"])
        if row["scope"]==scope:
            grouped.setdefault(key,[]).append((when,row))
    active,conflicts,inactive={},{},{}
    for key,items in grouped.items():
        latest=max(x[0] for x in items)
        candidates=[r for t,r in items if t==latest]
        signatures={json.dumps([r["value"],r.get("deleted",False),r.get("expires_at")],sort_keys=True) for r in candidates}
        if len(signatures)>1:
            conflicts[key]=candidates
            continue
        row=candidates[0]
        if row.get("deleted"): inactive[key]="deleted"
        elif row.get("expires_at") and instant(row["expires_at"])<=now: inactive[key]="expired"
        else: active[key]=row
    return {"scope":scope,"active":active,"conflicts":conflicts,"inactive":inactive}

if __name__ == "__main__":
    sys.exit(main(process, "Reconcile scoped memory records while exposing conflicts and expiry."))
