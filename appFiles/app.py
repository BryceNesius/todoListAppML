from flask import Flask, render_template, request
from models import Task
from prioritizer import prioritize_tasks

app = Flask(__name__)

tasks = [] 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_task = Task(request.form['description'], 
                        priority=request.form.get('priority', 'medium'),
                        due_date=request.form.get('due_date'))
        tasks.append(new_task)  

    prioritized_tasks = prioritize_tasks(tasks)

    return render_template('index.html', tasks=prioritized_tasks)

if __name__ == '__main__':
    app.run(debug=True)

