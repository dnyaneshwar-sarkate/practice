##Python programme to flatten a nested dictionary using Dict. Comprehension

data = {
    "name": "John",
    "address": {
        "city": "Pune",
        "state": "Maharashtra"
    }
}

flattened = {}

for key, value in data.items():
    if isinstance(value, dict):
        for inner_key, inner_value in value.items():
            flattened[f"{key}.{inner_key}"] = inner_value
    else:
        flattened[key] = value

print(flattened)