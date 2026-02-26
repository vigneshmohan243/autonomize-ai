# Autonomize AI – Sr. QA Engineer Assignment  

**Data Validation & Model Integration – Prioritizing Clinical Safety & Accuracy**

## Objective

Create a comprehensive test suite and methodology to validate an Agentic Platform’s **data validation and model integration processes**, with a strong emphasis on:

- Patient safety  
- Clinical accuracy  
- Compliance  
- Data integrity  

## Repository Diagram

- Full repository flow (Mermaid): [docs/repo_overview.md](docs/repo_overview.md)

This repository demonstrates a risk-based, automation-first approach to ensure reliable simulated patient interactions across agent workflows and AI model pipelines.

## Scenario Coverage

This solution executes **simulated patient interactions within the Agentic platform**, covering the following areas:

### 1. Agent Integration Test

Simulates a **Data Extraction Agent** retrieving patient data from a connected healthcare application and validates the extracted payload against a pre-defined schema.

**Validation focus**

- Data extraction accuracy  
- Data type validation  
- Format compliance  
- Schema integrity  
- Error handling for malformed inputs  

---

### 2. Model Integration Test

Simulates patient data submission into a **pre-trained AI model** (e.g., risk classification model) and validates both input handling and output correctness.

**Validation focus**

- Model input robustness  
- Handling variations in data format  
- Interpretation of nuanced patient information  
- Response accuracy and bounds checking  
- Failure handling for invalid payloads  

---

### 3. UX/UI Validation

Validates user-facing safeguards for potential error scenarios.

**Covered scenario**

- Upload of medical chart with incorrect format  
- Upload exceeding allowed limits  
- Verification of UI responsiveness  
- Error message clarity and usability  

---

## Risk-Based Test Prioritization

| Priority | Area | Rationale |
|----------|------|-----------|
| P0 | Agent data extraction | Direct patient safety impact |
| P0 | Model risk scoring | Clinical decision risk |
| P1 | Input format variations | Data quality risk |
| P1 | UI upload validation | User error prevention |

---

## Automation Framework

The automation framework is designed to be **CI/CD invocable** and supports:

- Pytest-based API validation  
- JSON schema validation  
- Playwright UI automation  
- HTML reporting  
- Dockerized execution  
- GitHub Actions pipeline  

---

## How to Run
### Dependecies
- Python 3.11
- Poetry 1.8.x+
- Node 20+
- npm
- Playwright browsers (`npm run playinstall` in `playwright/`)

## Pytest
### Install Poetry (if needed):
```
pip install poetry
```
### Install Python dependencies
```
poetry install
```
### Local Execution
```
poetry run pytest
```
### Parallel Execution
```
poetry run pytest -n auto
```
### Report 
```
reports/
```
## Playwright
### Install Node dependencies
```
cd playwright
npm install
```
### Local Execution
```
npm test
```
### Report
```
report
```

### Docker Execution
#### Pytest
```
docker build -t autonomize-qa .
docker run autonomize-qa
```
#### Playwright
```docker build -f playwright/Dockerfile -t autonomize-playwright .
docker run --rm autonomize-playwright
````

### CI/CD Pipeline

The repository includes a ready-to-use pipeline that:
- Installs dependencies
- Executes automated tests
- Generates test reports
- Supports regression automation

Pipeline file:
```
.github/workflows/pytest.yml
.github/workflows/playwright.yml
```

### Deliverables Included
- Detailed automated test suite
- Step-by-step validation scenarios
- Expected results and pass/fail criteria
- Risk-based prioritization
- CI/CD-ready automation framework
- Dockerized runtime
