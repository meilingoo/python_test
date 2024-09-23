from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample tasks for demonstration
tasks = ['Buy groceries', 'Complete coding tutorial', 'Walk the dog']

@app.route('/')
def index():
  return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('newTask')  # 获取表单中的任务
    if new_task:
        tasks.append(new_task)   # 将任务添加到任务列表中
    return redirect(url_for('index'))  # 重定向回主页

@app.route('/complete', methods=['POST'])
def complete_tasks():
    completed_tasks = request.form.getlist('taskCheckbox')
    for index in map(int, completed_tasks):
        if 1 <= index <= len(tasks):
            tasks[index - 1] += " - Completed"
    return redirect(url_for('index'))

# Add a new route to handle task deletion
@app.route('/delete', methods=['POST'])
def delete_tasks():
    tasks_to_delete = request.form.getlist('taskCheckbox')
    tasks_to_delete.sort(reverse=True)  # Start deleting from the end to avoid index issues
    for index in map(int, tasks_to_delete):
        if 1 <= index <= len(tasks):
            del tasks[index - 1]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)