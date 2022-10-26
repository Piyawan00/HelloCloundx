from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from hwfsod import Students ,Subjects ,Registration, Teachers ,session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:IADica26129@10.104.9.207:11254/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False

db = SQLAlchemy(app)

@app.route('/')
def index():
    result = session.query.all()
    return render_template('sss.html', result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
