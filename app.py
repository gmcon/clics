from flask import Flask, request, redirect
from datetime import datetime
import csv
import os

app = Flask(__name__)
REGISTRO = 'clics.csv'

@app.route('/confirmar')
def confirmar():
    alumno = request.args.get('id', 'desconocido')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Crea el archivo si no existe
    if not os.path.exists(REGISTRO):
        with open(REGISTRO, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['alumno', 'timestamp'])

    # Registra el clic
    with open(REGISTRO, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([alumno, timestamp])
    
    return f"""
    <html>
        <body style='font-family:sans-serif; text-align:center; margin-top: 50px;'>
            <h2>Tu confirmación fue registrada exitosamente</h2>
            <p>{alumno}</p>
            <p>Fecha y hora: {timestamp}</p>
        </body>
    </html>
    """

@app.route('/ver_registros')
def ver_registros():
    if not os.path.exists(REGISTRO):
        return "<p>No hay registros aún.</p>"
    
    with open(REGISTRO, 'r') as f:
        contenido = f.read().replace('\n', '<br>')
    
    return f"<html><body><h2>Registros de clics:</h2><p>{contenido}</p></body></html>"

@app.route('/')
def home():
    return "<p>Servidor funcionando. Usa /confirmar?id=... para registrar clics.</p>"

if __name__ == '__main__':
    app.run(debug=True)
