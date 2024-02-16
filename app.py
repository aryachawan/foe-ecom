from flask import Flask,render_template,request,jsonify
from function import login_add_userdata_to_db,login_get_user_data,checkpasswordstrength,inventory_get_user_data
app=Flask(__name__)

#INITIAL ROUTE [ HOME PAGE BEFORE LOGIN ]
@app.route("/")
def hello_world():
    data=request.form
    logindata=login_get_user_data()
    flag=0
    if(data):
        for i in logindata:
            if(data['user']==i['username'] or data['user']==i['email']):
                flag+=1
                break
        return render_template('index.html',flag=flag,i=i)
    else:
        return render_template('index.html')

@app.route("/signup",methods=['post'])
def login():
    return render_template('tempform.html')

# HOME PAGE AFTER LOGIN
@app.route("/home",methods=['post'])
def homeafterlogin():
    data=request.form
    logindata=login_get_user_data()
    return render_template('home.html')



@app.route("/confirmation",methods=['post'])
def loginconfirmation():
    data=request.form
    logindata=login_get_user_data()
    flag=5 # FLAG FOR DECISION MAKING OF ADDING DATA TO DATABASE

    # DATABASE VALIDATION FOR SIGNING INTO ALREADY EXISITNG ACCOUNT
    if(len(data)==2):
        for i in logindata:
            if(((i['username']==data['userinput']) or (i['email']==data['userinput'])) and i['password']==data['password']):
                flag=3
    else:
    # DATABASE VALIDATION FOR LOGING INTO OR CREATING NEW ACCOUNT
        for i in logindata:
            # CHECKING FOR ALREADY EXISTING USERNAME
            if((i['username']==data['username'])):
                flag=1
            # CHECKING FOR ALREADY EXISTING EMAIL
            elif((i['email']==data['email'])):
                flag=2
        
    if(flag==5):
        login_add_userdata_to_db(data)
        
    return render_template('confirmation.html',F=flag,data=data)

@app.route("/signin",methods=['post'])
def signin():
    return render_template('signinform.html')  

@app.route("/shop",methods=['post'])
def shop():
    return render_template('shop.html')

@app.route("/FilterResults",methods=['post'])
def filterresults():
    jerseydata=request.form
    price=int(jerseydata['uplimit'])
    inventorydata=inventory_get_user_data()
    selection_dict=[]
    gigaflag=0
    flag=0
    for i in inventorydata:
        if((i['price']<=price) and (i['size']==jerseydata['sizeinput'])):
            dict_temp={
                "name":i['name'],
                "size":i['size'],
                "price":i['price']
            }
            flag+=1
            selection_dict.append(dict_temp)

    return render_template('filterresult.html',data=selection_dict,flag=flag)

 
if __name__=="__main__":
    app.run(debug=True)