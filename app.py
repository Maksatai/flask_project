from flask import Flask, render_template, request
from database import Books, engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
DBSession = sessionmaker(engine)
session = DBSession()

@app.route('/')
def homepage():
    book = session.query(Books).all()

    return render_template('index.html',books = book)
    
@app.route('/add/', methods=["POST"])
def add():
    a_object = Books(author = request.form["author"], descrip = request.form["descrip"], year = request.form["year"])
    session.add(a_object)
    session.commit()
    return """
        <h1>Архив добавлен</h1>
        <a href='/'>Домой</a>
    """

