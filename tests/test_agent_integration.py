import json
import pytest
from utils.api_client import APIClient
from utils.validators import validate_schema

client = APIClient()


@pytest.mark.high
def test_agent_data_extraction_valid_schema():
    """P0: Validate extraction accuracy and schema compliance"""

    with open("test_data/valid_patient.json") as f:
        payload = json.load(f)

    response = client.extract_patient_data(payload)

    assert response.status_code == 200

    data = response.json()

    is_valid, error = validate_schema(
        data,
        "test_data/schema.json"
    )

    assert is_valid, f"Schema validation failed: {error}"


@pytest.mark.negative
def test_agent_handles_missing_fields():
    """P0: Agent should reject malformed payload"""

    with open("test_data/invalid_patient.json") as f:
        payload = json.load(f)

    response = client.extract_patient_data(payload)

    assert response.status_code == 400
