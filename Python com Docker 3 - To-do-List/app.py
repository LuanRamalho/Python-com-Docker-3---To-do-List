
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tarefas = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nova_tarefa = request.form.get("tarefa")
        if nova_tarefa:
            tarefas.append(nova_tarefa)
        return redirect("/")
    return render_template("index.html", tarefas=tarefas)

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tarefas):
        tarefas.pop(index)
    return redirect("/")
