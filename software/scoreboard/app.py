from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Global scores dictionary
scores = {"R1": 0, "R2": 0}

# Route to update score (called during match)
@app.route('/score', methods=['POST'])
def update_score():
    data = request.get_json()
    robot = data.get('robot')
    event = data.get('event')
    score = data.get('score')

    if robot in scores and isinstance(score, int):
        scores[robot] += score
        return jsonify({"status": "success", "scores": scores})
    return jsonify({"status": "failure", "message": "Invalid robot or score"}), 400

# Route to get current scores (used in scoreboard & winner)
@app.route('/get_scores', methods=['GET'])
def get_scores():
    return jsonify({"scores": scores})

# Route to reset scores (used when restarting game)
@app.route('/reset_scores', methods=['POST'])
def reset_scores():
    global scores
    scores = {"R1": 0, "R2": 0}
    return jsonify({"status": "reset", "scores": scores})

# Route: redirect base to index
@app.route('/')
def home():
    return redirect('/index')

# Route: main game/index
@app.route('/index')
def index():
    return render_template('index.html')

# Route: countdown page
@app.route('/countdown')
def countdown():
    return render_template('countdown.html')

# Route: scoreboard page
@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')

# Route: winner page
@app.route('/winner')
def winner():
    return render_template('winner.html')

# Main app runner
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

    
