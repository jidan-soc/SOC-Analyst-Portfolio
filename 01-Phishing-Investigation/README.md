# Phishing Investigation — Simulated SOC Exercise

## 1. Investigation Overview

This project is a simulated phishing investigation designed to demonstrate a Security Operations Center (SOC) Level 1 investigation workflow.

The scenario involves a user receiving an email claiming that their Microsoft 365 account will be disabled unless they verify their identity.

This is a controlled training scenario and does not represent a real-world incident handled by the analyst.

---

## 2. Investigation Objective

The objectives of this investigation are to:

- Identify indicators associated with phishing.
- Analyze the sender and message content.
- Examine the suspicious URL/domain.
- Determine whether the message should be treated as suspicious.
- Identify relevant indicators of compromise (IOCs).
- Recommend appropriate initial SOC response actions.
- Document the investigation using an evidence-based methodology.

---

## 3. Simulated Email

**From:**

`security-alert@micr0soft-support.com`

**To:**

`employee@example.com`

**Subject:**

`Urgent: Your account will be disabled today`

**Message:**

> We detected unusual activity on your Microsoft 365 account.
> Your account will be permanently disabled unless you verify your identity within 30 minutes.
>
> Verify your account:
>
> `https://m365-security-verification.example/verify`
>
> Thank you,  
> Microsoft 365 Security Team

---

## 4. Initial Analysis

### Sender Address

The sender uses:

`security-alert@micr0soft-support.com`

The domain contains the word `micr0soft`, which uses a zero (`0`) instead of the letter `o`.

This is a potential impersonation indicator because an attacker could use a visually similar domain to make the sender appear legitimate.

### Urgency

The email states that the account will be permanently disabled within 30 minutes.

This creates urgency and pressure on the recipient to act without carefully verifying the message.

Urgency alone does not prove that an email is malicious, but it is an important phishing indicator when combined with other evidence.

### Suspicious URL

The message directs the user to:

`https://m365-security-verification.example/verify`

The URL claims to be related to Microsoft 365 security, but the domain does not represent an official Microsoft domain.

The mismatch between the claimed organization and the destination domain is a significant warning sign.

### Requested Action

The recipient is instructed to verify their identity through the provided link.

Credential verification requests delivered through unsolicited security alerts should be investigated carefully because phishing campaigns commonly attempt to obtain account credentials or other sensitive information.

---

## 5. Indicators of Compromise

The following indicators were identified during the investigation:

| Indicator | Value | Type |
|---|---|---|
| Sender domain | `micr0soft-support.com` | Suspicious domain |
| Sender address | `security-alert@micr0soft-support.com` | Email address |
| URL | `https://m365-security-verification.example/verify` | Suspicious URL |
| Subject | `Urgent: Your account will be disabled today` | Phishing indicator |

### IOC Handling Note

The indicators above are taken from a simulated training scenario.

They should not be treated as confirmed malicious infrastructure without additional validation.

---

## 6. Phishing Indicators Identified

The investigation identified multiple characteristics commonly associated with phishing:

1. **Brand impersonation**
   - The sender attempts to appear associated with Microsoft 365.

2. **Lookalike domain**
   - `micr0soft-support.com` uses a visually deceptive spelling.

3. **Artificial urgency**
   - The recipient is given only 30 minutes to respond.

4. **Threat of account loss**
   - The message claims the account will be permanently disabled.

5. **Suspicious verification link**
   - The destination domain does not match the organization being impersonated.

6. **Credential-related request**
   - The user is instructed to verify their identity through an external link.

---

## 7. Investigation Finding

### Finding

**Suspicious — likely phishing attempt**

The conclusion is based on the combination of:

- A lookalike sender domain
- Microsoft 365 impersonation
- Artificial urgency
- Threat of account suspension
- A suspicious external verification URL
- A request for identity verification

The evidence is sufficient to treat the message as suspicious and escalate it for further investigation.

This conclusion is based only on the simulated email content. In a real SOC investigation, additional evidence such as full email headers, URL analysis, domain reputation, authentication results, and endpoint telemetry would be reviewed before making a final determination.

---

## 8. Recommended SOC L1 Response

A SOC analyst could recommend the following initial actions:

1. Do not click the suspicious link.
2. Do not provide credentials or other sensitive information.
3. Preserve the original email and relevant headers.
4. Extract and investigate the sender domain and URL.
5. Search security telemetry for other users who received the same message.
6. Check whether any user interacted with the URL.
7. If credentials were submitted, initiate the organization's credential-compromise response procedure.
8. Block confirmed malicious indicators according to organizational procedures.
9. Escalate the incident when additional evidence indicates compromise.

---

## 9. MITRE ATT&CK Relevance

This simulated scenario can be related to techniques involving phishing and credential theft.

Potentially relevant techniques should only be mapped after examining the actual behavior and available evidence.

For this exercise, phishing is the primary behavior being investigated.

---

## 10. Evidence Limitations

This investigation has several limitations because it is a simulated exercise.

The investigation does not contain:

- Original email headers
- SPF/DKIM/DMARC authentication results
- Real DNS information
- URL sandbox results
- Malware samples
- Endpoint telemetry
- Authentication logs
- SIEM alerts

Therefore, the investigation demonstrates the **initial SOC triage and reasoning process**, rather than a complete real-world incident investigation.

---

## 11. Lessons Learned

This exercise demonstrates that phishing investigations should be evidence-driven.

Important lessons include:

- Do not trust the display name of an email sender.
- Examine the actual sender domain.
- Look for domain impersonation and typosquatting.
- Treat artificial urgency as a warning sign.
- Inspect links before interacting with them.
- Consider multiple indicators together rather than relying on one suspicious characteristic.
- Preserve evidence before taking investigative actions.
- Clearly document limitations and avoid claiming evidence that was not actually collected.

---

## 12. Skills Demonstrated

- Phishing analysis
- IOC identification
- Email security fundamentals
- Social-engineering analysis
- SOC alert triage
- Incident documentation
- Evidence-based reasoning
- Basic MITRE ATT&CK awareness
- Security investigation methodology

---

## 13. Investigation Status

**Status:** Completed — Simulated Training Exercise

**Environment:** Controlled educational scenario

**Analyst:** Jidan
