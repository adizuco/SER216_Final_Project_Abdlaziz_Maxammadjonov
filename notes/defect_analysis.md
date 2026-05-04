# Task 4 — Defect Analysis

## Defect Statement

> "A valid parking permit is shown as expired during security verification."

## Analysis

| Item | Answer |
|------|--------|
| **Defect category** | Functional defect — incorrect business logic. The system returns the wrong status (Expired) for a record whose stored expiry date is still in the future. It is not a UI defect (the message is rendered correctly) and not a performance defect (the response time is fine); the underlying *decision* is wrong. |
| **Severity** | **High.** The core promise of the system — telling security whether a permit is valid right now — is broken. A valid customer is wrongly flagged, which can lead to a false violation, customer complaints, and loss of trust in the system. It does not crash the system, so it is not Critical, but it directly blocks a primary use case. |
| **Priority** | **High (P1).** The defect happens during live security verification on campus and is visible to end users in real time. It must be fixed before the next release; a hotfix is appropriate. Workaround (manually overriding the check) is slow and error-prone, so the fix cannot wait. |
| **Possible root cause** | Most likely a **timezone / date-comparison bug** in the verification service: the permit's `expires_at` is stored in UTC but compared against the security device's local time (or vice versa), so a permit that expires at midnight UTC is reported as expired several hours early in a positive UTC offset. Other plausible causes: (a) the expiry field is a string and is being compared lexically rather than as a date, (b) a recent migration shifted expiry dates by one day due to a `date` vs `datetime` cast, (c) caching: an old expired record is being served from cache after renewal. The timezone hypothesis should be checked first because it matches the symptom (a *valid* permit being shown expired). |
| **Regression test** | After the fix, re-run **TC-06** (see `tables/test_cases.csv`): scan a permit issued today that expires next semester, on devices set to multiple timezones (UTC, UTC+5, UTC−8). The expected result is *Valid* on every device. Add this test to the automated regression suite so the defect cannot silently return after a future change to the verification service. |

## Recommended Fix Workflow

1. Reproduce the defect against a copy of production data with at least one near-expiry permit.
2. Inspect the verification service's expiry comparison — confirm both sides are timezone-aware `datetime` objects.
3. Patch the comparison to always evaluate in UTC (or use a database-level comparison so the database engine handles timezones consistently).
4. Add unit tests covering UTC, positive offsets, negative offsets, and the day-boundary edge case.
5. Add the regression test (TC-06) to the CI pipeline.
6. Deploy as a hotfix; monitor the verification audit log for any recurrence over the next 7 days.
