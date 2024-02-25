##Virtual Fitness Coach 
************************************************************************************************************************************************************************
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/set_goals', methods=['POST'])
def set_goals():
    data = request.json
    user_id = data['user_id']
    fitness_goals = data['fitness_goals']
    dietary_preferences = data['dietary_preferences']
    
    users[user_id] = {'fitness_goals': fitness_goals, 'dietary_preferences': dietary_preferences}
    
    return jsonify({'message': 'Goals set successfully'})

@app.route('/generate_workout_plan', methods=['POST'])
def generate_workout_plan():
    data = request.json
    user_id = data['user_id']
    fitness_level = data['fitness_level']
    preferred_workouts = data['preferred_workouts']
    
    if user_id in users:
        # Sample code to generate workout plan based on user preferences
        # Replace with actual algorithm or integration with fitness API
        workout_plan = {'workouts': ['Cardio', 'Strength Training'], 'duration': '1 hour'}
        return jsonify({'workout_plan': workout_plan})
    else:
        return jsonify({'error': 'User not found'})

if __name__ == '__main__':
    app.run(debug=True)

