from flask import Flask, request, jsonify, render_template, redirect

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

scores = {"R1": 0, "R2": 0}

@app.route('/score', methods=['POST'])
def update_score():
    data = request.get_json()
    robot = data.get('robot')
    event = data.get('event')
    score = data.get('score')

    if robot in scores:
        scores[robot] += score
        return jsonify({"status": "success", "scores": scores})
    return jsonify({"status": "failure", "message": "Invalid robot"}), 400

@app.route('/get_scores', methods=['GET'])
def get_scores():
    return jsonify({"scores": scores})

@app.route('/')
def home():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/countdown')
def countdown():
    return render_template('countdown.html')

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')

@app.route('/winner')
def winner():
    return render_template('winner.html')

@app.route('/reset_scores', methods=['POST'])
def reset_scores():
    global scores
    scores = {"R1": 0, "R2": 0}
    return jsonify({"status": "reset", "scores": scores})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    
