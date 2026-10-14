# Architecture

Python 3 standard-library CLI invokes local OS diagnostic tools through subprocess without a shell. Windows uses `netstat -ano -p tcp`; Linux uses `ss -lntu`. Parsers normalize records to protocol, address, port and optional PID, then output CSV or JSON. No remote scanning or network calls are performed. The program does not modify firewall or system settings.
