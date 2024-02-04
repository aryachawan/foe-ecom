from flask import Flask,render_template,request
from function import add_userdata_to_db
app=Flask(__name__)

#INITIAL ROUTE [ HOME PAGE ]
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/login",methods=['post'])
def login():
    return render_template('tempform.html')

@app.route("/confirmation",methods=['post'])
def loginconfirmation():
    data=request.form
    add_userdata_to_db(data)
    return render_template('confirm.html')

if __name__=="__main__":
    app.run(debug=True)