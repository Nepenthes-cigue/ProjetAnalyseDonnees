from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Chemin du fichier JSON
file_path = os.path.join(os.path.dirname(__file__), 'data', 'etudiant_results.json')

# Route principale
@app.route('/')
def index():
    # Charger les résultats des étudiants
    with open(file_path, 'r') as file:
        etudiant_results = json.load(file)
    
    # Passer les résultats au template HTML
    return render_template('index.html', results=etudiant_results)

# API pour renvoyer les résultats en JSON (optionnel)
@app.route('/api/results')
def api_results():
    with open(file_path, 'r') as file:
        etudiant_results = json.load(file)
    return jsonify(etudiant_results)

if __name__ == '__main__':
    app.run(debug=True)