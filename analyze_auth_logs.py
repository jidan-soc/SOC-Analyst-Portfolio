#!/usr/bin/env python3
"""Triage synthetic authentication CSV events using simple, explainable rules.

Usage:
    python analyze_auth_logs.py
    python analyze_auth_logs.py path/to/auth_events.csv

Expected columns: timestamp,username,source_ip,event,result
This is a learning example, not a production detection engine.
"""
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

FAILURE_THRESHOLD = 5
SUCCESS_AFTER_FAILURE_THRESHOLD = 3


def load_events(path):
    events = []
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {"timestamp", "username", "source_ip", "event", "result"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            raise ValueError(
                "CSV must include columns: timestamp,username,source_ip,event,result"
            )
        for line_no, row in enumerate(reader, start=2):
            result = (row.get("result") or "").strip().lower()
            if result not in {"success", "failure"}:
                print(f"[WARN] Skipping line {line_no}: invalid result {result!r}")
                continue
            events.append({
                "timestamp": (row.get("timestamp") or "").strip(),
                "username": (row.get("username") or "").strip(),
                "source_ip": (row.get("source_ip") or "").strip(),
                "event": (row.get("event") or "").strip(),
                "result": result,
            })
    return events


def analyze(events):
    failures_by_ip = Counter()
    failures_by_ip_user = Counter()
    failed_so_far_by_ip = Counter()
    success_after_failures = []

    # CSV order is treated as event order for this simple lab.
    for event in events:
        ip = event["source_ip"]
        user = event["username"]
        if event["result"] == "failure":
            failures_by_ip[ip] += 1
            failures_by_ip_user[(ip, user)] += 1
            failed_so_far_by_ip[ip] += 1
        elif failed_so_far_by_ip[ip] >= SUCCESS_AFTER_FAILURE_THRESHOLD:
            success_after_failures.append({
                "timestamp": event["timestamp"],
                "username": user,
                "source_ip": ip,
                "prior_failures": failed_so_far_by_ip[ip],
            })

    alerts = []
    for ip, count in sorted(failures_by_ip.items()):
        if count >= FAILURE_THRESHOLD:
            alerts.append({
                "rule": "AUTH-001",
                "severity": "Medium",
                "source_ip": ip,
                "count": count,
                "detail": f"{count} failed logins observed from {ip}",
            })
    for item in success_after_failures:
        alerts.append({
            "rule": "AUTH-002",
            "severity": "High - review",
            "source_ip": item["source_ip"],
            "count": item["prior_failures"],
            "detail": (
                f"Successful login for {item['username']} at {item['timestamp']} "
                f"after {item['prior_failures']} earlier failures from "
                f"{item['source_ip']}"
            ),
        })
    return alerts, failures_by_ip_user


def main():
    default_path = Path(__file__).with_name("auth_events.csv")
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_path
    if not path.is_file():
        print(f"[ERROR] CSV file not found: {path}", file=sys.stderr)
        return 2
    try:
        events = load_events(path)
    except (OSError, ValueError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2

    alerts, failures_by_ip_user = analyze(events)
    print("SOC AUTHENTICATION LOG TRIAGE")
    print("=" * 34)
    print(f"Events parsed: {len(events)}")
    print(f"Unique source/user pairs with failures: {len(failures_by_ip_user)}")
    print(f"Alerts generated: {len(alerts)}")
    if not alerts:
        print("\nNo alerts matched the configured rules.")
    for index, alert in enumerate(alerts, start=1):
        print(f"\n[{index}] {alert['rule']} | {alert['severity']}")
        print(f"    {alert['detail']}")
    print("\nAnalyst reminder: alerts require contextual validation; they are not proof of compromise.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
