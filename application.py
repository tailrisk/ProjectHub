import sqlite3
import datetime
from flask import Flask, render_template, g, request, redirect, url_for

PATH = 'projects.sqlite'
#PATH = 'mvp-mysqldb.ckrwmj7t0hcw.us-east-1.rds.amazonaws.com'
application = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    cursor.close()
    return results

@application.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

@application.route('/')
@application.route('/projects')
def projects():
    projects = execute_sql('SELECT project.id, project.title, project.description, project.salary, client.id as client_id, client.name as client_name FROM project JOIN client ON client.id = project.client_id')
    return render_template('index.html', projects=projects)

@application.route('/project/<project_id>')
def project(project_id):
    project = execute_sql('SELECT project.id, project.title, project.description, project.salary, client.id as client_id, client.name as client_name FROM project JOIN client ON client.id = project.client_id WHERE project.id = ?', [project_id], single=True)
    return render_template('project.html', project=project)

@application.route('/client/<client_id>')
def client(client_id):
    client = execute_sql('SELECT * FROM client WHERE id=?', [client_id], single=True)
    projects = execute_sql('SELECT project.id, project.title, project.description, project.salary FROM project JOIN client ON client.id = project.client_id WHERE client.id = ?', [client_id])
    reviews = execute_sql('SELECT review, rating, title, date, status FROM review JOIN client ON client.id = review.client_id WHERE client.id = ?', [client_id])
    return render_template('client.html', client=client, projects=projects, reviews=reviews)

@application.route('/client/<client_id>/review', methods=('GET', 'POST'))
def review(client_id):
    if request.method == 'POST':
        review = request.form['review']
        rating = request.form['rating']
        title = request.form['title']
        status = request.form['status']
        date = datetime.datetime.now().strftime("%m/%d/%Y")
        execute_sql('INSERT INTO review (review, rating, title, date, status, client_id) VALUES (?, ?, ?, ?, ?, ?)', (review, rating, title, date, status, client_id), commit=True)
        return redirect(url_for('client', client_id=client_id))
    return render_template('review.html', client_id=client_id)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
