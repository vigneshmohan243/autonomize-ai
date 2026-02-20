class APIClient:
    """
    Simulated client for Agent and Model endpoints.
    Keeps assignment self-contained.
    """

    def extract_patient_data(self, payload: dict):
        # simulate validation
        required_fields = {"patient_id", "age", "conditions"}

        if not required_fields.issubset(payload.keys()):
            return MockResponse({}, 400)

        return MockResponse(payload, 200)

    def run_risk_model(self, payload: dict):
        # simple mock logic
        try:
            age = int(payload.get("age"))
        except Exception:
            return MockResponse({"error": "invalid age"}, 400)

        risk_score = min(1.0, age / 100)
        return MockResponse({"risk_score": risk_score}, 200)


class MockResponse:
    def __init__(self, json_data, status_code):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json
