from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config')

app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
app.config['MYSQL_HOST'] = ''
mysql = MySQL(app)


@app.route('/query')
def query():
	cur = mysql.connection.cursor()
	cur.execute("select * from blog order by id desc")
	result = cur.fetchall()
	return render_template('posts.html', title="posts", posts=result, data = {'name' : 'Justin', 'technology' : 'Flask'}
)





from app import views
