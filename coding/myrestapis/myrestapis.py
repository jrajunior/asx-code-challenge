from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/validate_json', methods=['POST'])
def validate_json():
    try:
        json_data = request.get_json()
        if json_data is None:
            return jsonify({'error': 'Invalid JSON'}), 400

        # Additional validation can be added here if needed

        return jsonify({'message': 'JSON is valid'}), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)

