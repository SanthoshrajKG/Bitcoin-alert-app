import schedule
import time
import requests
import smtplib
import mysql.connector

def send_mail(receiver_email):
    message = """ 
    Subject: Your Alert Triggered for BTC !

    Current price of BTC is now reached your expected value"""
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, password)
    s.sendmail(sender_email, receiver_email, message)
    s.quit()
    return

def fetch_bitcoin():
    url="https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=ma rket_cap_desc&per_page=100&page=1&sparkline=false"
    data=requests.get(url)
    input=data.json()
    result = input[0]['current_price']
    return(result)

def check():
    conn=mysql.connector.connect(host="localhost",user="root",password="PASS",database="DBNAME")
    cur=conn.cursor()
    rows=cur.execute("SELECT * FROM users WHERE isTriggered='NO'")
    if(rows==0):return
    else:
        coin=fetch_bitcoin()
        print("Current price is ",coin)
        userDetails=cur.fetchall()
        for user in userDetails:
            if(user[2]==coin):
                send_mail(user[1])
                print("Alert Triggered: Mail sent to the %s user !",user[0])
                cur.execute("UPDATE users SET isTriggered='YES' WHERE triggervalue=%s"%coin)
                conn.commit()                 
    cur.close()
    conn.close()

sender_email="YOUR_EMAIL@gmail.com"
password="EMAIL_PASS"
schedule.every(5).seconds.do(check)
while(True):
    schedule.run_pending()
    time.sleep(1)
