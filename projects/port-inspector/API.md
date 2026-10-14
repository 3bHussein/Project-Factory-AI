# CLI Interface

No HTTP API exists. The command-line interface accepts `--json` for a JSON array of objects and `--port N` to filter a port from 1 through 65535. Default output is CSV with header `protocol,local_address,port,pid`. JSON object fields are `protocol`, `local_address`, `port`, and `pid`; PID can be null. Exit status 0 indicates a successful query, and 1 indicates an inspection failure.
