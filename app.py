from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def foo():
	with open("database.txt", "a") as myfile:
		myfile.write(request.form['message']+"\n")
	'''execute whatever code you want when the button gets clicked here'''
	return index()#"hello world"

if __name__ == '__main__':
	app.run(debug = True)


