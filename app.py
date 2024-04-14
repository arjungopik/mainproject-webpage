from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:user@localhost:5432/evaluation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class studentData(db.Model):
    __tablename__ = 'studentdata'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    register_number = db.Column(db.String)
    mark_scored =  db.Column(db.String)
    assessmentid =  db.Column(db.String)





class answerscriptData(db.Model):
    __tablename__ = 'answerscripts'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    answer =  db.Column(db.String)
    assessmentid =  db.Column(db.String)

class assessmentData(db.Model):
    __tablename__ = 'assessment'  
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer =  db.Column(db.String)



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

