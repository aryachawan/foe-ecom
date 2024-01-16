from flask import Flask, render_template,redirect

app = Flask(__name__)
app.secret_key = "sunil"

@app.route("/",methods=["GET","POST"])
def home():
    return render_template("index.html")
@app.route("/form.html")
def login():
    return render_template("form.html")
if __name__ == "__main__":
    app.run(debug=True)