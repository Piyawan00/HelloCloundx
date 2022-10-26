
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType,CHAR,VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('postgresql://webadmin:IADica26129@node36962-pawaris.proen.app.ruk-com.cloud:5432/hw')
#engine = create_engine('sqlite:///practice.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()


class Students(Base):
    __tablename__ = 'student'
    student_id = Column(CHAR(13), primary_key=True, nullable=False)
    f_name = Column(VARCHAR(30), nullable=False)
    l_name = Column(VARCHAR(30), nullable=False)
    e_mail = Column(VARCHAR(50), nullable=False)

class Teachers(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(CHAR(3), primary_key=True, nullable=False)
    tf_name = Column(VARCHAR(30), nullable=False)
    tl_name = Column(VARCHAR(30), nullable=False)
    e_mail = Column(VARCHAR(50), nullable=False)

class Subjects(Base):
    __tablename__ = 'subject'
    subject_id = Column(VARCHAR(15), primary_key=True, nullable=False)
    subject_name = Column(VARCHAR(50), nullable=False)
    creadit = Column(Integer(), nullable=False)
    teacher_id = Column(VARCHAR(50), nullable=False)

class Registration(Base):
    __tablename__ = 'registration'
    student_id = Column(CHAR(13), primary_key=True, nullable=False)
    subject_id = Column(VARCHAR(15),primary_key=True,nullable=False)
    year = Column(CHAR(4), nullable=False)
    semester = Column(CHAR(1), nullable=False)
    grade = Column(CHAR(2), nullable=False)

rg1 = Registration(student_id='6406022610040',subject_id='060233113',year='2022',semester='1',grade='C')
rg01 = Registration(student_id='6406022610040',subject_id='060233112',year='2022',semester='1',grade='B')
rg001 = Registration(student_id='6406022610040',subject_id='080103034',year='2022',semester='1',grade='A')
rg2 = Registration(student_id='6406022610058',subject_id='060233113',year='2022',semester='1',grade='C')
rg02 = Registration(student_id='6406022610058',subject_id='060233112',year='2022',semester='1',grade='A')
rg002 = Registration(student_id='6406022610058',subject_id='080103034',year='2022',semester='1',grade='A')
rg3 = Registration(student_id='6406022610031',subject_id='060233113',year='2022',semester='1',grade='A')
rg03 = Registration(student_id='6406022610031',subject_id='060233112',year='2022',semester='1',grade='A')
rg003 = Registration(student_id='6406022610031',subject_id='080103034',year='2022',semester='1',grade='A')

sb1 = Subjects(subject_id='060233113',subject_name='ADVANCED COMPUTER PROGRAMMIN',creadit=3,teacher_id='AMK')
sb2 = Subjects(subject_id='060233112',subject_name='DATA ENGINEERING',creadit=3,teacher_id='STS')
sb3 = Subjects(subject_id='080103034',subject_name='ENGLISH CONVERSATION',creadit=3,teacher_id='SPK')

tc1 = Teachers(teacher_id='AMK',tf_name='Anirach',tl_name='Mingkwan',e_mail='Anirach@email.kmutnb.ac.th')
tc2 = Teachers(teacher_id='STS',tf_name='Sarayoot',tl_name='Tanessakulwattana',e_mail='Sarayoot@email.kmutnb.ac.th')
tc3 = Teachers(teacher_id='SPK',tf_name='Supalak',tl_name='Nakhornsri',e_mail='Supalak@email.kmutnb.ac.th')

st1 = Students(student_id='6406022610040',f_name='Pawaris',l_name='Pitirit',e_mail='s6406022610040@email.kmutnb.ac.th')
st2 = Students(student_id='6406022610058',f_name='Piyawan',l_name='Nimpraprut',e_mail='s6406022610058@email.kmutnb.ac.th')
st3 = Students(student_id='6406022610031',f_name='Papop',l_name='Sangeamsak',e_mail='s6406022610031@email.kmutnb.ac.th')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

list = [st1,st2,st3,tc1,tc2,tc3,sb1,sb2,sb3,rg1,rg01,rg001,rg2,rg02,rg002,rg3,rg03,rg003]
for i in list: 
    session.add(i)

session.commit()
#result = session.query(Students.student_id,Students.f_name,Students.l_name,Registration.subject_id,Subjects.subject_name,Registration.grade,Teachers.teacher_id,Teachers.tf_name,Teachers.tl_name).join(Registration,Students.student_id == Registration.student_id).join(Subjects,Registration.subject_id == Subjects.subject_id).join(Teachers,Subjects.teacher_id == Teachers.teacher_id).all()
