# Project 01 — Simulated Phishing Investigation

**Type:** Tabletop / simulated SOC investigation  
**Objective:** Practice reviewing a suspicious email, identifying indicators, deciding severity, and documenting a safe response.

> This is a simulated exercise. The email and indicators below are fictional; this is not a real incident.

## Scenario

An employee reports an unexpected email claiming that their mailbox will be disabled unless they sign in immediately. The message uses urgency and an unfamiliar sender domain.

## Sample evidence

| Field | Simulated value | Why it matters |
|---|---|---|
| Sender | `it-support@example-suspicious.test` | Sender domain does not match a verified corporate domain |
| Subject | `Urgent: mailbox access expires today` | Urgency can be a social-engineering signal |
| Link | `https://login.example-suspicious.test/verify` | Unverified login destination |
| Attachment | None observed | No attachment is present in this scenario |
| User action | User reports email; click status unknown | Must verify with the user and available telemetry |

The `.test` domain is reserved for testing and is not a real phishing destination.

## Investigation workflow

1. **Preserve evidence:** retain the original message as an attachment or export according to organizational policy; record who reported it and when.
2. **Inspect sender details:** compare the visible From address, Reply-To, Return-Path, and authentication results (SPF, DKIM, DMARC) if available.
3. **Review URL safely:** do not open a suspicious link on a normal device. Use approved analysis tooling and organizational procedures.
4. **Check scope:** search mail telemetry for matching sender, subject, URL, and recipients.
5. **Confirm user action:** ask whether the recipient clicked the link, entered credentials, approved MFA, or downloaded anything.
6. **Assess severity:** increase urgency if credentials were entered, a payload was executed, or multiple users were targeted.
7. **Recommend response:** quarantine/remove matching messages if authorized; block confirmed malicious indicators through approved controls; reset credentials and revoke sessions if compromise is suspected.
8. **Document and escalate:** record evidence, decisions, timestamps, affected users, actions, and unresolved questions.

## Initial assessment

**Initial disposition:** Suspicious — requires validation.  
**Confidence:** Medium, based on urgency and an unverified destination alone.  
**Severity:** Provisional; cannot be finalized without checking user interaction, authentication results, and campaign scope.

Avoid labelling an email “confirmed phishing” based only on its subject line. Corroborate indicators.

## Example analyst note

> Reported message impersonates IT support and pressures the recipient to verify mailbox access. The sender domain and login destination are unverified. User click/credential-entry status and message authentication results remain unknown. Recommend preserving the original message, searching mail telemetry for matching indicators, and confirming user interaction before assigning final severity.

## Learning outcomes

- Separate observed facts from assumptions.
- Explain why urgency and a mismatched domain may be suspicious.
- Identify the missing evidence needed to confirm phishing.
- Recommend proportionate containment and account-protection steps.

## Evidence checklist

- [ ] Original message preserved
- [ ] Sender and Reply-To reviewed
- [ ] SPF/DKIM/DMARC results checked where available
- [ ] URL assessed using approved safe workflow
- [ ] Recipient scope searched
- [ ] User click and credential-entry status confirmed
- [ ] Findings and escalation documented
