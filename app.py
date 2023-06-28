from flask import Flask, jsonify, render_template, url_for, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:314162846@localhost:5432/testdb'

# Inicialización de las extensiones Flask-SQLAlchemy y Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

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

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
