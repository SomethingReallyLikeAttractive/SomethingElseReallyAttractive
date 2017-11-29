from flask import Flask, Response, request, flash, render_template, url_for
app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/', methods=['POST','GET'])
def get_data():
	print('Recieved from client: {}'.format(request.data))
	flash('We recieved {}'.format(request.data))
	return render_template('site.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,port=5000)
