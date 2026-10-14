# Security

Port Inspector performs read-only local inspection and never changes firewall rules, terminates processes or scans remote addresses. Subprocess calls use fixed argument arrays rather than a shell. There are no credentials or network API keys. Local listening addresses and process identifiers can expose sensitive system configuration, so avoid publishing output without review. Do not run unknown downloaded scripts with administrator privileges.
