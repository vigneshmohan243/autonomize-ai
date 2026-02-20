import json
from jsonschema import validate, ValidationError


def validate_schema(data, schema_path):
    with open(schema_path) as f:
        schema = json.load(f)

    try:
        validate(instance=data, schema=schema)
        return True, None
    except ValidationError as e:
        return False, str(e)
