# Task 1 — Requirements

## System: Digital Parking Permit System

## Functional Requirements

**FR1 — Vehicle Registration**
The system shall allow students and staff to register a vehicle by providing the license
plate number, make, model, color, and owner ID. Each user may register up to three vehicles
per academic year.

**FR2 — Permit Request and Approval**
The system shall allow a registered user to request a parking permit by selecting a permit
type (student, staff, visitor) and a preferred parking zone. The request shall be reviewed
and either approved or rejected by the parking office, and the user shall be notified of
the decision by email.

**FR3 — Real-Time Zone Availability**
The system shall display the live availability (free / occupied / reserved) of every
campus parking zone so that users can choose a zone with open spaces before submitting
a permit request.

**FR4 — Permit Verification by Security**
The system shall allow security staff to scan a vehicle's license plate or permit QR code
and instantly verify whether the displayed permit is valid, expired, or revoked, and to
record any violation directly into the user's record.

## Non-Functional Requirements

**NFR1 — Performance**
The system shall respond to a permit verification scan in under 2 seconds, even when up
to 500 verifications are performed concurrently across campus during peak hours.

**NFR2 — Security**
All personal data (license plates, owner IDs, payment data) shall be transmitted over
HTTPS and stored encrypted at rest using AES-256. Only authenticated parking-office and
security staff shall be allowed to view or modify permit records.
