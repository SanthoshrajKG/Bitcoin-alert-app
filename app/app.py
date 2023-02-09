from flask import Flask, request, render_template, make_response, session
from flask_mysqldb import MySQL

app=Flask(__name__)
mysql=MySQL(app)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="PASS"
app.config['MYSQL_DB']="DBNAME"

@app.route('/')
def index():
    return "<b>This is my Krypto task for the infra role !<br><br>Go to <a href='http://127.0.0.1:5000/alerts/create'>Create<a> and Enter the used data and trigger value<b>"

@app.route('/alerts/create',methods=['GET','POST'])
def Create_Alert():
    if(request.method=='POST'):
        userDetails=request.form
        name=userDetails['name']
        email=userDetails['emailid']
        triggerValue=userDetails['triggervalue']
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO users(name,email,triggervalue,isTriggered) VALUES(%s,%s,%s,%s)',(name,email,triggerValue,'NO'))
        mysql.connection.commit()
        cur.close()
        return 'Created an Alert'
    return render_template('index.html')

@app.route('/alerts/delete/',methods=['GET','POST'])
def Deleting_alert():
    if(request.method=='POST'):
        userDetails=request.form
        name=userDetails['name']
        triggervalue=userDetails['triggervalue']
        cur=mysql.connection.cursor()
        sql="DELETE FROM users WHERE name=%s AND triggervalue=%s"
        cur.execute(sql,(name, triggervalue))
        mysql.connection.commit()
        cur.close()
        return 'Deleted an Alert'
    return render_template('del.html')

@app.route('/alerts/fetch_all',methods=['GET'])
def Fetching_all_alert():
    cur=mysql.connection.cursor()
    rows=cur.execute('SELECT * FROM users')
    if(rows>0):
        userDetails=cur.fetchall()
        cur.close()
        return render_template('triggers.html',userDetails=userDetails)
    cur.close()
    return 'Enter some trigger values first !'

@app.route('/alerts/triggered',methods=['GET','POST'])
def Fetching_triggered_alert():
    cur=mysql.connection.cursor()
    rows=cur.execute('SELECT * FROM users WHERE isTriggered="%s"'%'YES')
    if(rows>0):
        userDetails=cur.fetchall()
        return render_template('triggers.html',userDetails=userDetails)
    return 'NO value is triggered yet !'

if __name__=='__main__':  
    app.run(debug=True)
