from flask import Flask,render_template
from hwfsod import Students,Teachers,Registration,Subjects,session

app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:IADica26129@node36962-pawaris.proen.app.ruk-com.cloud:5432/hw'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False


@app.route('/')
def index():
    result = session.query(Students.student_id,Students.f_name,Students.l_name,Registration.subject_id,Subjects.subject_name,Registration.grade,Teachers.tf_name,Teachers.tl_name)\
        .outerjoin(Registration,Students.student_id == Registration.student_id)\
        .outerjoin(Subjects,Registration.subject_id == Subjects.subject_id).outerjoin(Teachers,Subjects.teacher_id == Teachers.teacher_id).all()
    return render_template('sss.html',result = result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)