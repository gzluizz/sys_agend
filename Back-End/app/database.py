import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),  # Converte para inteiro
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        print("Conexão bem-sucedida com o banco de dados!")
        return connection  # Retorna a conexão corretamente

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None  # Retorna None em caso de erro
