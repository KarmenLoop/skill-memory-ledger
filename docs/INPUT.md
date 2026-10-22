# Input and output

English | [简体中文](input.zh-CN.md)

Supply a UTF-8 JSON object (maximum 10 MiB). Use `--input PATH` for a file or `--input -` for standard input. Run `--version` to inspect the installed helper version. Duplicate JSON keys and non-finite JSON constants are rejected. Arrays are required unless documented as optional. IDs must be stable and unique. Dates use ISO 8601; timestamps require an explicit UTC offset.

| Field | Contract |
| --- | --- |
| scope | Exact scope to retrieve. |
| as_of | Offset-aware timestamp. |
| observations | Objects: key, value, scope, source, updated_at, optional expires_at and deleted boolean. Multiple versions per key are allowed. |

## Example

```json
{
  "scope": "project:demo",
  "as_of": "2026-10-19T12:00:00Z",
  "observations": [
    {
      "key": "report_format",
      "value": "Markdown",
      "scope": "project:demo",
      "source": "user request 12",
      "updated_at": "2026-10-18T10:00:00Z"
    },
    {
      "key": "report_format",
      "value": "CSV",
      "scope": "project:demo",
      "source": "user correction 13",
      "updated_at": "2026-10-19T10:00:00Z"
    }
  ]
}
```

## Result

active map, conflicts map keyed by memory key, inactive map with expired/deleted reason, and scope.

See [the complete sample result](../examples/expected.json). Exit 0 means processing completed, not that all reported findings passed.

## Errors and side effects

The helper makes no network requests and executes no submitted commands. It reads the input and explicitly documented local paths. It writes only a requested new output file; stdout is the default. Invalid input exits 2. Existing output is preserved. An output write failure can leave a partial new file; remove that file before retrying. Installation is a separate explicit action.
