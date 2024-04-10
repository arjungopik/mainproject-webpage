from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:user@localhost:5432/evaluation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login',methods=['POST','GET'])
def login():    
    if request.method == 'POST':
        return render_template('choose.html')

@app.route('/view-progress')
def progress():    
    return render_template('preview.html')

@app.route('/create-evaluation')
def facinput():    
    return render_template('facultyinput.html')


@app.route('/create-new-evaluation',methods=['POST','GET'])
def createnew():    
    if request.method == 'POST':
        return render_template('upload.html')
    

@app.route('/upload',methods=['POST','GET'])
def upload():    
    if request.method == 'POST':
        return render_template('upload.html')
    


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)

