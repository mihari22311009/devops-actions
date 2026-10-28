import sqlite3
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
DB = "/data/tarefas.db"


def conectar():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def iniciar():
    con = conectar()
    con.execute(
        "CREATE TABLE IF NOT EXISTS tarefas ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "titulo TEXT NOT NULL)"
    )
    con.commit()
    con.close()


PAGINA = """
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <title>Minhas tarefas</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 0 16px; }
    h1 { color: #333; }
    form { display: inline; }
    input[type=text] { padding: 8px; width: 60%; }
    button { padding: 8px 12px; cursor: pointer; }
    li { margin: 10px 0; list-style: none; }
  </style>
</head>
<body>
  <h1>Minhas tarefas</h1>

  <form action="/criar" method="post">
    <input type="text" name="titulo" placeholder="Nova tarefa" required>
    <button type="submit">Adicionar</button>
  </form>

  <ul style="padding: 0;">
    {% for t in tarefas %}
    <li>
      <form action="/editar/{{ t['id'] }}" method="post">
        <input type="text" name="titulo" value="{{ t['titulo'] }}" required>
        <button type="submit">Salvar</button>
      </form>
      <form action="/apagar/{{ t['id'] }}" method="post">
        <button type="submit">Apagar</button>
      </form>
    </li>
    {% else %}
    <li>Nenhuma tarefa ainda.</li>
    {% endfor %}
  </ul>
</body>
</html>
"""


@app.route("/")
def listar():
    con = conectar()
    tarefas = con.execute("SELECT * FROM tarefas ORDER BY id DESC").fetchall()
    con.close()
    return render_template_string(PAGINA, tarefas=tarefas)


@app.route("/criar", methods=["POST"])
def criar():
    titulo = request.form["titulo"].strip()
    if titulo:
        con = conectar()
        con.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
        con.commit()
        con.close()
    return redirect("/")


@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    titulo = request.form["titulo"].strip()
    if titulo:
        con = conectar()
        con.execute("UPDATE tarefas SET titulo = ? WHERE id = ?", (titulo, id))
        con.commit()
        con.close()
    return redirect("/")


@app.route("/apagar/<int:id>", methods=["POST"])
def apagar(id):
    con = conectar()
    con.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    con.commit()
    con.close()
    return redirect("/")


iniciar()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
