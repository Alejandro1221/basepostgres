from flask import Flask, jsonify, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
#
# Parametros de configuracion a la base de datos
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#
# A continuacion se crea un modelo o esquema para la base de datos
#
class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	completed = db.Column(db.Integer, default=0)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)
	#
	# Funcion que devuelve una cadena cada vez que se crea un nuevo elemento
	# Devuelve el 'id' de la tarea recien creada
	#
	def __repr__(self):
    	      return '<Task %r>' % self.id

def convert_todo_to_dict(todo):
    todo_dict = {}
    for attr in vars(todo):
        if attr not in ['_sa_instance_state']: 
            attr_value = getattr(todo,attr) 
            todo_dict[attr] = attr_value
    return todo_dict

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST': 
        task_content = request.form['content'] 
        # 
        # Se crea un objeto conforme al modelo declarado 
        # 
        new_task = Todo(content = task_content) 
        try: 
            db.session.add(new_task) 
            db.session.commit() 
            return redirect('/') 
        except: 
            return 'There was an issue adding your task' 
    else: 
        tasks = Todo.query.order_by(Todo.date_created).all() 
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
	task_to_delete = Todo.query.get_or_404(id)

	try:
    	  db.session.delete(task_to_delete)
    	  db.session.commit()
    	  return redirect('/')
	except:
    	  return "There was a problem deleting that task"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	task = Todo.query.get_or_404(id)

	if request.method == 'POST':
    	  task.content = request.form['content']
    	  try:
        	    db.session.commit()
        	    return redirect('/')
    	  except:
        	    return 'There was an issue updating your task'
	else:
    	    return render_template('update.html', task=task)

@app.route('/todo/<int:id>', methods=['DELETE','PUT'])
def todo_del_put(id): 
    task = Todo.query.get_or_404(id) 
    if request.method == 'DELETE': 
        try: 
            db.session.delete(task)
            db.session.commit()
            return jsonify({'Result': 'Ok'})
        except: 
            return f'There was an issue deleting a task whose id is {id}'
    else:
        if request.json and 'content' in request.json:
            task.content = request.json.get('content',"")
            try:
                db.session.commit() 
                return jsonify({'Result': 'Ok'})
            except: 
                return f'There was an issue updating a task whose id is {id}'

@app.route('/todo', methods=['GET','POST'])
def todo_get_post(): 
    if request.method == 'GET': 
        tasks = Todo.query.order_by(Todo.date_created).all() 
        todos = []
        for todo in tasks:
            todos.append(convert_todo_to_dict(todo))
        return jsonify({'tasks': todos})
    else:
        if request.json and 'content' in request.json:
            content = request.json 
            new_task = Todo(**content) 
            try: 
                db.session.add(new_task) 
                db.session.commit() 
                return jsonify({'Result': 'Ok'}) 
            except: 
                return f'There was an issue creating a task with content \'{content}\'' 

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
