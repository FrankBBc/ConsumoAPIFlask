from transformers import pipeline
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Inicializa el clasificador fuera de la función para mejorar el rendimiento
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clasificar', methods=['POST'])
def classify_text():
    texto = request.form.get('llamada', '')
    
    if not texto:
        return jsonify({'error': 'No se proporcionó ningún texto.'}), 400
    
    candidate_labels = [
        'Danza', 'Política', 'Deportes', 'Religión', 'Otros', 
        'Tecnología', 'Salud', 'Ciencia', 'Entretenimiento', 'Educación',
        'Negocios', 'Medio ambiente', 'Historia', 'Cultura', 'Viajes',
        'Finanzas', 'Moda', 'Gastronomía', 'Música', 'Literatura'
    ]
    resultado_clasificacion = classifier(texto, candidate_labels)
    
    # Verificar que el modelo esté devolviendo las puntuaciones correctamente
    print("Resultado de la clasificación:", resultado_clasificacion)
    
    max_score_idx = resultado_clasificacion['scores'].index(max(resultado_clasificacion['scores']))
    label_score = resultado_clasificacion['labels'][max_score_idx]
    
    return jsonify({'label': label_score})

if __name__ == '__main__':
    app.run(port=5010, debug=True, host='localhost')
