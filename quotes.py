from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:kondom@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hujvpfyppgfodf:df43f86ea090eb0ec3d36e31b2c3bb43de110379d6728eec021031e2866d8c09@ec2-52-202-66-191.compute-1.amazonaws.com:5432/d9e0jra7t0b5sr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Favquotes(db.Model):
    id     = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(30))
    quote  = db.Column(db.String(1000))
    
@app.route('/')
def index():
    # quotes = ['quote 1','quote 2','quote 3']
    # return '<h1> Hello World </h1>'
    # return render_template('index.html', quote = 'Air beriak tanda tak dalam', quotes = quotes)
    result = Favquotes.query.all()
    return render_template('index.html', result = result)

@app.route('/quotes')
def quotes():
    # return '<h1> Life is a Journey</h1>'
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'] )
def process():
    # return '<h1> Life is a Journey</h1>'
    author = request.form['author']
    quote  = request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))