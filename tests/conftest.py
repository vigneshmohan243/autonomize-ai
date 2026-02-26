import csv


def load_csv_cases(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_agent_cases(scenario=None):
    cases = load_csv_cases("test_data/agent_data.csv")
    if scenario is None:
        return cases
    return [case for case in cases if case.get("scenario") == scenario]


def load_model_cases(scenario=None):
    cases = load_csv_cases("test_data/model_data.csv")
    if scenario is None:
        return cases
    return [case for case in cases if case.get("scenario") == scenario]


def build_agent_payload(case):
    raw_conditions = (case.get("conditions") or "").strip()
    conditions = (
        [c.strip() for c in raw_conditions.split(";")] if raw_conditions else []
    )
    age_str = (case.get("age") or "").strip()
    age = int(age_str) if age_str and age_str.lstrip("-").isdigit() else age_str or None
    return {
        "patient_id": (case.get("patient_id") or "").strip() or None,
        "age": age,
        "conditions": conditions,
    }


def build_model_payload(case):
    raw = (case.get("conditions") or "").strip()
    conditions = [c.strip() for c in raw.split(";") if c.strip()]
    age_raw = (case.get("age") or "").strip()
    age = int(age_raw) if age_raw.lstrip("-").isdigit() else age_raw
    return {"age": age, "conditions": conditions}
