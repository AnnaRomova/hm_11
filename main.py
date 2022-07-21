from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates: list[dict] = load_candidates_from_json("C:\\Users\\anna1\\skypro_lessons\\hw_11\\candidates.json")
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:idx>')
def show_candidate_page(idx):
    candidate: dict = get_candidate(idx)
    if not candidate:
        return "кандидат не найден"
    return render_template('card.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def search_candidate_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    if candidates:
        return render_template('search.html', candidates=candidates, lenght=len(candidates))
    return "кандидат не найден"

@app.route('/skill/<skill_name>')
def search_candidate_by_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    if candidates:
        return render_template('skill.html', candidates=candidates, lenght=len(candidates))
    return "кандидат не найден"

app.run()