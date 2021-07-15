from flask import Flask, render_template, request
from flask.wrappers import Request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
    excel_data_df = pd.read_excel(r'report.xlsx', engine='openpyxl')

    return render_template('index.html',excel_f=excel_data_df.values, exc=excel_data_df)
    

@app.route('/add/', methods=["POST"])
def add():
    author = request.form["author"]
    descrip = request.form["descrip"]
    year = request.form["year"]
    f = open('goods.txt','a+',encoding='utf-8')
    f.write(author + '\n')
    f.close()
    return """
        <h1>Архив добавлен</h1>
        <a href='/'>Домой</a>
    """

