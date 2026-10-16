# Project 02 — Authentication Log Triage

**Type:** Runnable Python mini-project using synthetic logs  
**Objective:** Detect repeated failed logins and successful logins after multiple failures.

## What it does

The script reads a CSV file of authentication events and flags:
- A source IP with at least **5 failed logins** in the dataset.
- A successful login from the same source IP after **3 or more earlier failures** in the dataset.

These are simple training rules, not production-grade detections. They do not account for all identity, network, or time-window context.

## Files

- `auth_events.csv` — synthetic events
- `analyze_auth_logs.py` — standard-library Python script
- `expected_output.txt` — example findings

## Run

From this folder:

```bash
python analyze_auth_logs.py
```

Or provide a CSV path:

```bash
python analyze_auth_logs.py auth_events.csv
```

Python 3 is required. The script uses only the Python standard library.

## Sample result interpretation

- A high failed-login count can indicate password guessing, a misconfigured application, or normal user error.
- A successful login after repeated failures deserves review, but does not by itself prove account compromise.
- Confirm user, host, source reputation, MFA status, geolocation context (if available and approved), and surrounding events before escalation.

## Tuning ideas

1. Add a time window rather than counting the entire file.
2. Group by account as well as source IP.
3. Exclude approved test accounts and known service-account patterns only after validation.
4. Add severity and confidence fields.
5. Write unit tests for edge cases.

## Safety and honesty

All records are synthetic. The IP addresses are from documentation/reserved ranges. This project does not connect to a real identity provider or perform login attempts.
