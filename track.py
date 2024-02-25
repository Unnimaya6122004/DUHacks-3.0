##Medication Reminder and Adherence Tracking Application 

********************************************************************************************************************************************************************************
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

users = {}

@app.route('/add_medication', methods=['POST'])
def add_medication():
    data = request.json
    user_id = data['user_id']
    medication_name = data['medication_name']
    dosage = data['dosage']
    schedule = data['schedule']
    
    users[user_id] = {'medications': [{'name': medication_name, 'dosage': dosage, 'schedule': schedule}], 'adherence': {}}
    
    return jsonify({'message': 'Medication added successfully'})

@app.route('/take_medication', methods=['POST'])
def take_medication():
    data = request.json
    user_id = data['user_id']
    medication_name = data['medication_name']
    
    if user_id in users:
        for med in users[user_id]['medications']:
            if med['name'] == medication_name:
                users[user_id]['adherence'].setdefault(medication_name, []).append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                return jsonify({'message': 'Medication taken successfully'})
    
    return jsonify({'error': 'User or medication not found'})

if __name__ == '__main__':
    app.run(debug=True)
