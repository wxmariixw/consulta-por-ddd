from flask import Flask, request, jsonify, render_template
import psycopg2
import json
from settings.settings import conn

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cidades_por_ddd/<int:ddd>', methods=['GET'])
def cidades_por_ddd(ddd):
    try:
        # Conecta ao banco de dados
        cursor = conn.cursor()
    
        # Executa a consulta SQL para obter as cidades e estados associados ao DDD
        query = f"SELECT cidade, estado FROM cities.cities WHERE ddd = {ddd};"
        cursor.execute(query)

        # Obtém os resultados
        resultados = [{'cidade': row[0], 'estado': row[1]} for row in cursor.fetchall()]

        # Fecha a conexão com o banco de dados
        cursor.close()
        conn.close()

        return app.response_class(
            response=json.dumps({'cidades': resultados}, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
