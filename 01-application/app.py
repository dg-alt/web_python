from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    author = os.getenv('AUTHOR', 'Неизвестен')
    
    return f"""
    <h1>Server Information</h1>
    <p><b>Имя хоста:</b> {hostname}</p>
    <p><b>IP адрес:</b> {ip_address}</p>
    <p><b>Автор:</b> {author}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)