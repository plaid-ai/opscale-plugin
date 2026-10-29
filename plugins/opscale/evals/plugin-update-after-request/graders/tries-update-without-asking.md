---
type: llm
focus: last_message
---

PASS if the reply first gives the profit-and-loss summary and then, at the end, reports the plugin update: either that the plugin was updated, or (because the commands could not run here) shows both `claude plugin marketplace update plaidlabs` and `claude plugin update opscale@plaidlabs` for the user to run; and it says the update applies after `/reload-plugins`, a restart, or a new session.
FAIL if the reply never mentions the plugin update, asks the user whether to update instead of handling it, or lists a command other than those two for the update.
