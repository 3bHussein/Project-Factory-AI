# Port Inspector V1 Test Plan

- Parser tests: Linux ss TCP/UDP, Windows netstat TCP listening and empty input.
- Run `python -m unittest discover -s projects/port-inspector/tests -v`.
- Real Windows/Linux system testing and CI run: pending verification.
- Limitations: Linux PIDs not included; Windows UDP not included.
