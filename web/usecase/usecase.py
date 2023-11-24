import psycopg2
from flask import jsonify, json

def cidades_por_ddd(ddd, db_config):
    try:
        # Conecta ao banco de dados
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Executa a consulta SQL para obter as cidades e estados associados ao DDD
        query = f"SELECT cidade, estado FROM cities.cities WHERE ddd = {ddd};"
        cursor.execute(query)

        # Obtém os resultados
        resultados = [{'cidade': row[0], 'estado': row[1]} for row in cursor.fetchall()]

        # Fecha a conexão com o banco de dados
        cursor.close()
        conn.close()

        return jsonify({'cidades': resultados}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
