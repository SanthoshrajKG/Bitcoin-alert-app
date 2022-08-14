from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import yaml

app=Flask(__name__)
mysql=MySQL(app)

db=yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']

@app.route('/',methods=['GET','POST'])
def index():
    return 'This is my Krypto task for the infra role'

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