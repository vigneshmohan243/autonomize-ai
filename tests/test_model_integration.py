import pytest
from utils.api_client import APIClient
from tests.conftest import load_model_cases, build_model_payload


client = APIClient()
_valid_cases = load_model_cases(scenario="valid")
_edge_cases = load_model_cases(scenario="edge")


@pytest.mark.high
@pytest.mark.parametrize(
    "case", _valid_cases, ids=[_case["id"] for _case in _valid_cases]
)
def test_risk_model_valid_input(case):
    """P0: Validate model response and bounds"""

    payload = build_model_payload(case)
    response = client.run_risk_model(payload)

    assert (
        response.status_code == 200
    ), f"{case['id']}: Expected 200, got {response.status_code}"

    assert "risk_score" in response.json()
    assert (
        0 <= response.json()["risk_score"] <= 1
    ), f"{case['id']}: Expected risk score between 0 and 1, got {response.json()['risk_score']}"


@pytest.mark.edge
@pytest.mark.parametrize(
    "case", _edge_cases, ids=[_case["id"] for _case in _edge_cases]
)
def test_model_handles_format_variation(case):
    """P1: Model should gracefully handle format issues"""

    payload = build_model_payload(case)

    response = client.run_risk_model(payload)

    assert response.status_code in [
        200,
        400,
    ], f"{case['id']}: Expected 200 or 400, got {response.status_code}"
