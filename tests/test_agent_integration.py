import json
import pytest
from utils.api_client import APIClient
from utils.validators import validate_schema
from tests.conftest import load_agent_cases, build_agent_payload

client = APIClient()
_valid_cases = load_agent_cases(scenario="valid")
_invalid_cases = load_agent_cases(scenario="invalid")


@pytest.mark.high
@pytest.mark.parametrize(
    "case", _valid_cases, ids=[_case["id"] for _case in _valid_cases]
)
def test_agent_data_extraction_valid_schema(case):
    """P0: Validate extraction accuracy and schema compliance"""

    payload = build_agent_payload(case)
    response = client.extract_patient_data(payload)

    assert (
        response.status_code == 200
    ), f"{case['id']}: Expected 200, got {response.status_code}"

    is_valid, error = validate_schema(response.json(), "test_data/schema.json")
    assert is_valid, f"{case['id']}: Schema validation failed: {error}"


@pytest.mark.negative
@pytest.mark.parametrize(
    "case", _invalid_cases, ids=[_case["id"] for _case in _invalid_cases]
)
def test_agent_handles_missing_fields(case):
    """P0: Agent should reject malformed payload"""

    payload = build_agent_payload(case)
    response = client.extract_patient_data(payload)

    assert (
        response.status_code == 400
    ), f"{case['id']}: Expected 400, got {response.status_code}"
