from flask import Flask,render_template,redirect

app=Flask(__name__)

@app.route('/')
def homepage():
    f=open('goods.txt' ,'r' ,'utf-8')
    txt=f.readlines()
    return render_template('index.html',goods=txt)



