import json


def load_candidates_from_json(path:str) -> list[dict]:
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)
#– возвращает список всех кандидатов


def get_candidate(candidate_id: int) -> dict:
    for candidate in load_candidates_from_json("C:\\Users\\anna1\\skypro_lessons\\hw_11\\candidates.json"):
        if candidate['id'] == candidate_id:
            return candidate
# – возвращает одного кандидата по его id


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    result = []
    for candidate in load_candidates_from_json("C:\\Users\\anna1\\skypro_lessons\\hw_11\\candidates.json"):
        if candidate['name'].split()[0].lower() == candidate_name.lower():
            result.append(candidate)
    return result
# – возвращает кандидатов по имени


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    result = []
    for candidate in load_candidates_from_json("C:\\Users\\anna1\\skypro_lessons\\hw_11\\candidates.json"):
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
# – возвращает кандидатов по навыку
