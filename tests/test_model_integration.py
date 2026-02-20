import pytest
from utils.api_client import APIClient

client = APIClient()


@pytest.mark.high
def test_risk_model_valid_input():
    """P0: Validate model response and bounds"""

    payload = {
        "age": 67,
        "conditions": ["diabetes"]
    }

    response = client.run_risk_model(payload)

    assert response.status_code == 200

    data = response.json()

    assert "risk_score" in data
    assert 0 <= data["risk_score"] <= 1


@pytest.mark.edge
def test_model_handles_format_variation():
    """P1: Model should gracefully handle format issues"""

    payload = {
        "age": "invalid"
    }

    response = client.run_risk_model(payload)

    assert response.status_code in [200, 400]
