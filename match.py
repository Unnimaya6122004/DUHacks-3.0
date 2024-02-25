##Real-Time Blood Donor Matching Platform 
**********************************************************************************************************************************************************************
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

donors = {}

@app.route('/register_donor', methods=['POST'])
def register_donor():
    data = request.json
    donor_id = data['donor_id']
    blood_type = data['blood_type']
    location = data['location']
    
    donors[donor_id] = {'blood_type': blood_type, 'location': location}
    
    return jsonify({'message': 'Donor registered successfully'})

@app.route('/find_matching_donor', methods=['POST'])
def find_matching_donor():
    data = request.json
    recipient_blood_type = data['recipient_blood_type']
    recipient_location = data['recipient_location']
    
    matching_donors = [donor_id for donor_id, info in donors.items() if info['blood_type'] == recipient_blood_type and info['location'] == recipient_location]
    
    if matching_donors:
        selected_donor = random.choice(matching_donors)
        return jsonify({'message': 'Matching donor found', 'donor_id': selected_donor})
    else:
        return jsonify({'error': 'No matching donor found'})

if __name__ == '__main__':
    app.run(debug=True)
