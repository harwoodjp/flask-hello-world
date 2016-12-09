from app import app
from flask import flash, redirect, render_template
from .forms import *
from flask_mysqldb import MySQL
import re

mysql = MySQL(app)


data = {'name' : 'Justin', 'technology' : 'Flask'}
info = {
	'python' : ['a good language', 'a powerful language', 'a syntax-friendly language'],
	'templating engine' : ['a way to render html fast', 'produces a pattern of elements', 'compliments repetition']
}

@app.route('/blog')
def blog():
	cur = mysql.connection.cursor()
	cur.execute("select * from blog order by id desc")
	result = cur.fetchall()
	cur.close()
	return render_template('posts.html', title="posts", posts=result, data = data)

@app.route('/')
def index():
	global data
	features = [
		"a micro-framework for python",
		"a routing and templating engine",
		"an easy way to build web applications"
	]
	return render_template('index.html', title="home", data=data, features=features)

@app.route('/about')
def about():
	global data
	subjects = ["python", "templating engine"]
	return render_template('about.html', data=data, title='about', subjects=subjects)

@app.route('/about/<string:technology>')
def about_technology(technology):
	global data
	global info

	if technology not in info:
		return redirect("/about")
	else:
		return render_template('about_detail.html', data=data, title='about %s' % technology,
			technology=technology.capitalize(), info=info[technology])


@app.route('/blog/add', methods=['GET','POST'])
def add_post():
	form = AddPost()

	if form.validate_on_submit():
		author = form.author.data
		date = form.date.data
		title = form.title.data
		body = re.escape(form.body.data)
		sql_string = ("insert into blog(author,date,title,body) values('%s','%s','%s','%s')" 
				% (author,date,title,body)
		)
		cur = mysql.connection.cursor()
		cur.execute(sql_string)
		cur.close()
		return redirect('/blog')

	return render_template("posts_add.html", data=data, form=form)






