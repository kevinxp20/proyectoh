#!/usr/bin/env python3
"""
Marvel Comics Web Application
Flask web interface - Python conversion of the original HTML/JavaScript application.
"""

from flask import Flask, render_template, request, jsonify
import hashlib
import time
import requests
import os


app = Flask(__name__)

# Marvel API credentials
# Can be overridden with environment variables for security
PUBLIC_KEY = os.getenv('MARVEL_PUBLIC_KEY', 'c9b342b95e7fdb1c01efcea39f8e65e7')
PRIVATE_KEY = os.getenv('MARVEL_PRIVATE_KEY', '9d15e7cf75996f595ce74aa89ebc089fb19b9e34')
BASE_URL = "http://gateway.marvel.com/v1/public"


def generate_auth_params():
    """Generate authentication parameters for Marvel API."""
    timestamp = str(int(time.time() * 1000))
    hash_input = timestamp + PRIVATE_KEY + PUBLIC_KEY
    hash_value = hashlib.md5(hash_input.encode('utf-8')).hexdigest()
    
    return {
        'ts': timestamp,
        'apikey': PUBLIC_KEY,
        'hash': hash_value
    }


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/search', methods=['GET'])
def search_comics():
    """
    API endpoint to search comics by character ID.
    
    Query Parameters:
        character_id: The Marvel character ID
        
    Returns:
        JSON response with comics data
    """
    character_id = request.args.get('character_id', '').strip()
    
    if not character_id:
        return jsonify({'error': 'character_id parameter is required'}), 400
    
    # Build request parameters
    params = generate_auth_params()
    params['characters'] = character_id
    
    try:
        response = requests.get(f"{BASE_URL}/comics", params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
