student_data = {
    "id1": {"name": "sara", "class": "v", "subject_integration": "english, math, science"},
    "id2": {"name": "david", "class": "v", "subject_integration": "english, math, science"},
    "id3": {"name": "sara", "class": "v", "subject_integration": "english, math, science "},
    "id4": {"name": "surya", "class": "v", "subject_integration": "english, math, science"},
}
result = {}
seen_keys = []
for student_id, detail in student_data.items():
    unique_key = (detail["name"], detail["class"], detail["subject_integration"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = detail
for k, v in result.items():
    print(k, ":", v)

