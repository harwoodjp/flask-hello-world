from app import app
from flask import flash, redirect, render_template
from .forms import LoginForm

data = {'name' : 'Justin', 'technology' : 'Flask'}
info = {
	'python' : ['a good language', 'a powerful language', 'a syntax-friendly language'],
	'templating engine' : ['a way to render html fast', 'produces a pattern of elements', 'compliments repetition']
}


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

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' % 
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/')

	return render_template('login.html', title='sign in', form=form, data=data)










