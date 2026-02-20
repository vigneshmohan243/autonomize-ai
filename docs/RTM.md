## 📊 Requirements Traceability Matrix (RTM)
### Objective Coverage
This RTM ensures full traceability between:
- Assignment requirements
- Risk areas
- Test cases
- Automation coverage
- Priority
with emphasis on clinical safety and data integrity.

### 🔗 High-Level Requirement Mapping
| Req ID     | Requirement Description                                        | Risk Area              | Priority | Covered By Test Case(s) | Automation Status      |
| ---------- | -------------------------------------------------------------- | ---------------------- | -------- | ----------------------- | ---------------------- |
| RQ-AG-001  | Validate Data Extraction Agent retrieves accurate patient data | Patient safety         | P0       | TC-AI-001               | Automated              |
| RQ-AG-002  | Validate schema compliance of extracted data                   | Data integrity         | P0       | TC-AI-001               | Automated              |
| RQ-AG-003  | Handle missing or malformed patient fields                     | Clinical accuracy      | P0       | TC-AI-002               | Automated              |
| RQ-MI-001  | Validate model accepts valid patient input                     | Clinical safety        | P0       | TC-MI-001               | Automated              |
| RQ-MI-002  | Ensure model output accuracy and bounds                        | Misclassification risk | P0       | TC-MI-001               | Automated              |
| RQ-MI-003  | Handle variations in input format                              | Data robustness        | P1       | TC-MI-002               | Automated              |
| RQ-UI-001  | Prevent upload of incorrect medical chart format               | User error             | P1       | TC-UI-001               | Automated (Playwright) |
| RQ-UI-002  | Prevent upload exceeding allowed limits                        | System stability       | P1       | TC-UI-002               | Automated (Playwright) |
| RQ-NFR-001 | CI/CD invocable automation framework                           | Release safety         | P1       | All                     | Automated              |
| RQ-NFR-002 | HTML reporting of execution results                            | Observability          | P2       | All                     | Automated              |

### 🧪 Detailed Traceability View
#### Agent Integration Coverage
| Requirement              | Test Case | Validation Type     | Risk | Status  |
| ------------------------ | --------- | ------------------- | ---- | ------- |
| Data extraction accuracy | TC-AI-001 | Functional + Schema | High | Covered |
| Data type validation     | TC-AI-001 | Schema              | High | Covered |
| Format compliance        | TC-AI-001 | Schema              | High | Covered |
| Missing field handling   | TC-AI-002 | Negative            | High | Covered |

#### Model Integration Coverage
| Requirement               | Test Case | Validation Type | Risk   | Status  |
| ------------------------- | --------- | --------------- | ------ | ------- |
| Valid input handling      | TC-MI-001 | Functional      | High   | Covered |
| Risk score bounds         | TC-MI-001 | Business rule   | High   | Covered |
| Format variation handling | TC-MI-002 | Edge            | Medium | Covered |

#### UX/UI Validation Coverage
| Requirement           | Test Case | Validation Type | Risk   | Status  |
| --------------------- | --------- | --------------- | ------ | ------- |
| Invalid file format   | TC-UI-001 | UX validation   | Medium | Covered |
| File size/page limit  | TC-UI-002 | Boundary        | Medium | Covered |
| Error message clarity | TC-UI-001 | UX              | Medium | Covered |

### Identified Gaps & Future Enhancements

Recommended for next phase:
- Performance/load testing of agent pipeline
- PHI masking validation
- Audit logging verification
- Model bias testing
- Prompt injection resilience
- Rate limiting validation
- Chaos testing for agent failures