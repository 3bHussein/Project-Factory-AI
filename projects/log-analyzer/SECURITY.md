# Security

The tool reads local logs only and does not make network requests. Output HTML escapes path strings. Query strings are removed from summarized error paths to reduce accidental disclosure of tokens, but raw paths may still be sensitive. HTML is written only when `--html` is specified. Logs remain on the device; never share reports without reviewing them.
