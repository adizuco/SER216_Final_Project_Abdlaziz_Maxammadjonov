# Task 3 — Test Case Table

Six test cases covering system, acceptance, and regression testing for the
Digital Parking Permit System.

| Test ID | Feature | Input / Data | Expected Result | Test Type |
|---------|---------|--------------|-----------------|-----------|
| TC-01 | End-to-end permit issuance | Register vehicle `ABC-123`, request Student permit for Zone A (4 free spaces), parking office approves | Permit is issued with a unique QR code, the user receives an approval email, and Zone A free count decreases from 4 to 3 | **System** |
| TC-02 | Permit verification under load | Security scans 50 different valid permit QR codes within 10 seconds during peak hours | All 50 scans return *Valid* in under 2 seconds each, no timeouts or duplicate verifications, audit log records all 50 events | **System** |
| TC-03 | Student requests a permit | A registered student logs in, selects **Staff** permit type for Zone B | System rejects the request with a clear message explaining staff permits are only available to staff users — meets business rule | **Acceptance** |
| TC-04 | Security reports a violation | Security scans an unregistered plate `XYZ-999` and adds violation note "No permit displayed" | System creates a violation record linked to the plate, marks it *Pending Review* for the parking office, and notifies the office — meets user expectation | **Acceptance** |
| TC-05 | Re-verify zone availability after permit fix | After fixing a defect that miscounted occupied spaces, run the original Zone A availability check with 2 cars parked | System reports 2 occupied / remaining free count is correct — earlier counting bug stays fixed | **Regression** |
| TC-06 | Re-verify permit expiry date logic after defect fix | After fixing the timezone bug in the permit expiry, scan a permit issued today that expires next semester | System returns *Valid*, never *Expired*, regardless of the security device's local timezone — earlier defect stays fixed | **Regression** |

## Notes on Test Type Selection

- **System tests (TC-01, TC-02)** check the complete integrated system end-to-end —
  the permit lifecycle through every component, and the verification subsystem
  under realistic concurrent load.
- **Acceptance tests (TC-03, TC-04)** check whether the system meets user and
  business expectations — the business rule that students cannot self-issue
  staff permits, and the user expectation that security can report violations
  smoothly.
- **Regression tests (TC-05, TC-06)** re-verify previously fixed defects to
  confirm they do not reappear after later changes — the zone counting bug and
  the permit expiry timezone bug.
