from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_NAME = 'tarefas.db'

def criar_tabela():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT NOT NULL,
                 description TEXT,
                 completion_date DATE,
                 priority INTEGER)''')
    conn.commit()
    conn.close()

criar_tabela()

@app.route('/criar_tarefa', methods=['POST'])
def create_task():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    completion_date = data.get('completion_date')
    priority = data.get('priority')

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO tasks (title, description, completion_date, priority)
                 VALUES (?, ?, ?, ?)''', (title, description, completion_date, priority))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'ok'}), 201

if __name__ == '__main__':
    app.run(debug=True)
