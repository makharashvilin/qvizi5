from flask import Flask, render_template, url_for, redirect, request


todo = []
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', todolist=todo)

@app.route('/addtask/<task>')
def addtask(task):
    todo.append(task)
    return render_template('addtask.html', todolist=todo)














if __name__ == '__main__':
    app.run(debug=True)