# SOC Incident Response Playbook — Entry-Level Triage

This playbook is a general educational checklist. Always follow the employer's approved policies, escalation matrix, and authority limits.

## 1. Intake and validate

- Record alert ID, source, detection time, affected user/host, and severity assigned by the tool.
- Identify what triggered the alert and preserve relevant logs.
- Check whether the event is expected activity, a known benign pattern, or unexplained.
- Do not close an alert solely because one indicator appears benign.

## 2. Scope and enrich

- Identify affected assets, accounts, and time range.
- Review related authentication, endpoint, DNS, proxy, firewall, and email events where available.
- Compare indicators against trusted internal context and approved threat intelligence.
- Separate facts, hypotheses, and unknowns in notes.

## 3. Decide priority

Increase urgency if evidence suggests:
- confirmed credential theft or account takeover;
- malware execution or persistence;
- privileged account involvement;
- multiple affected users or hosts;
- data access/exfiltration or business disruption.

When uncertain, escalate rather than independently dismissing a potentially serious alert.

## 4. Containment and evidence

- Only perform containment actions that are authorized for your role.
- Coordinate account disablement, session revocation, host isolation, or message removal with the responsible team.
- Preserve timestamps, event IDs, relevant logs, and chain-of-custody details where required.
- Avoid actions that destroy evidence unless approved by incident command.

## 5. Communicate and close

Record:
- summary and impact;
- evidence and timeline;
- actions taken and by whom;
- escalation and stakeholder notifications;
- final disposition and confidence;
- follow-up detection or prevention improvements.

## L1 analyst rule

**Observe → Validate → Scope → Document → Escalate / follow approved playbook.**

An L1 analyst should not claim root cause or compromise is confirmed unless the available evidence supports it.
