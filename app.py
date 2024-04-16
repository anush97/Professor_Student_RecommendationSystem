from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load recommendations
def load_recommendations():
    with open('Recommendation_files/student_recommendations.json', 'r') as file:
        student_recs = json.load(file)
    with open('Recommendation_files/professor_recommendations.json', 'r') as file:
        professor_recs = json.load(file)
    with open('Recommendation_files/professor_to_professor_recommendations.json', 'r') as file:
        prof_to_prof_recs = json.load(file)
    with open('Recommendation_files/student_to_student_recommendations.json', 'r') as file:
        student_to_student_recs = json.load(file)
    return student_recs, professor_recs, prof_to_prof_recs, student_to_student_recs

student_recs, professor_recs, prof_to_prof_recs, student_to_student_recs = load_recommendations()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    user_type = data.get('user_type')
    guid = data.get('guid')

    if user_type == 'student':
        prof_recommendations = student_recs.get(guid, [])
        student_recommendations = student_to_student_recs.get(guid, [])
        return jsonify({'professors': prof_recommendations, 'students': student_recommendations})

    elif user_type == 'professor':
        student_recommendations = professor_recs.get(guid, [])
        peer_recommendations = prof_to_prof_recs.get(guid, [])
        return jsonify({'students': student_recommendations, 'professors': peer_recommendations})

    return jsonify({'error': 'Invalid user type or GUID'}), 400

if __name__ == '__main__':
    app.run(debug=True)
