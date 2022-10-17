SELECT student.student_id,student.f_name,student.l_name,registration.subject_id,subject_name,grade,teacher.f_name,teacher.l_name
FROM student
JOIN  registration on student.student_id = registration.student_id
JOIN subject on registration.subject_id = subject.subject_id
JOIN teacher on subject.teacher_id = teacher.teacher_id