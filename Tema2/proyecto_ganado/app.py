from flask import Flask, render_template, request
from db_connection import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.close()
    conn.close()
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.close()
    conn.close()
    return render_template('formulario.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    celular = request.form['celular']
    horario = request.form['horario']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO contactos_ganado (nombre, apellido, correo, celular, horario) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nombre, apellido, correo, celular, horario))
    conn.commit()

    cursor.close()
    conn.close()

    return "Datos guardados correctamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
