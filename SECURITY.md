# Security Policy

## Reporting a vulnerability

Please report security issues privately rather than opening a public issue.
Use GitHub's **[Report a vulnerability](https://github.com/frescodicredito/lens/security/advisories/new)**
(Security → Advisories) so the report stays private until a fix is available.

Include: what the issue is, how to reproduce it, and the potential impact. You can expect
an initial response within a few days.

## Scope notes

Lens is an MCP server whose tools receive input from an LLM/agent. Two things are by design,
not vulnerabilities:

- **Prompt injection.** Tools like `lens_compose_prompt` deliberately place caller-supplied
  text (the topic and constraints) into a system prompt. Treat composed prompts as untrusted
  and review them before running agents on sensitive data.
- **Local file access.** The server reads and writes session/persona JSON under its own
  directory. Identifiers that flow into file paths are validated to prevent traversal
  (see `tests/test_security.py`), but the server still has the file permissions of the
  process that runs it. Run it with least privilege.
