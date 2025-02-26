import json


# Read
with open("docs/v2-cpa-data.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)


# Add id
for item in json_data:
    item["id"] = f"{item['year']}-{item['pid']}-{item['type']}-{item['source']}"


# Save
with open("docs/v3-cpa-data.json", "w", encoding="utf-8") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)