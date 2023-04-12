from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def frist_page():
	return render_template("index.html")
@app.route("/thanos")
def second_page():
	return render_template("second.html")
if __name__=="__main__":
	app.run(port=8000,debug=True)