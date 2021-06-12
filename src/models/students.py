
from src.config.db import DB

class StudentsModel():

    def borrar_estudiante(self, id_estudiante):
        cursor = DB.cursor()
        cursor.execute('delete from students where id = ?',(id_estudiante,))
        cursor.close()

    def estudiantes(self):
        cursor = DB.cursor()
        cursor.execute('select * from students')
        students = cursor.fetchall()
        estudiantes = []
        for estudiante in students:
            estudiantes.append({
                'id': estudiante[0],
                'identificacion': estudiante[1],
                'nombre': estudiante[2],
                'apellido': estudiante[3],
                'telefono': estudiante[4],
                'email': estudiante[5],
                'semestre': estudiante[6]
            })
        return estudiantes

    def bringStudents(self, id):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM students INNER JOIN student_subjects AS s_s ON students.id = s_s.student_id INNER JOIN subjects ON s_s.subject_id = subjects.id WHERE subjects.id = ?',(id,))
        students = cursor.fetchall()
        cursor.close()
        estudiantes = []
        for estudiante in students:
            estudiantes.append({
                'id': estudiante[0],
                'identificacion': estudiante[1],
                'nombre': estudiante[2],
                'apellido': estudiante[3],
                'telefono': estudiante[4],
                'email': estudiante[5],
                'semestre': estudiante[6]
            })
        return estudiantes

    def bringStudent(self, id):
        cursor = DB.cursor()
        cursor.execute('select * from students where id = ?',(id,))
        student = cursor.fetchone()
        cursor.close()
        
        return {
            'id': student[0],
            'identificacion': student[1],
            'nombre': student[2],
            'apellido': student[3],
            'telefono': student[4],
            'email': student[5],
            'semestre': student[6]
        }

    def bringStudentSubjects(selef, studentId, subjectId):
        cursor = DB.cursor()
        cursor.execute('select * from student_subjects where student_id = ? and subject_id = ?',(studentId, subjectId,))
        studentSubjects = cursor.fetchone()
        return studentSubjects 

    def insertStudent(self, idn, name, surname, phone, email, semester):
        cursor = DB.cursor()
        cursor.execute('insert into students(idn, name, surname, phone, email, semester) values(?, ?, ?, ?, ?,?)',(idn, name, surname, phone, email, semester,))
        cursor.close()

    def insertStudentSubject(self, studentId, subjectId):
        cursor = DB.cursor()
        cursor.execute('insert into student_subjects(student_id, subject_id) values(?,?)',(studentId, subjectId,))
        cursor.close()

    def editStudent(self, idn, name, surname, phone, email, semester, id):
        cursor = DB.cursor()
        cursor.execute('update students set idn = ?, name = ?, surname = ?, phone = ?, email  = ?, semester = ? where id = ?',(idn, name, surname, phone, email, semester, id,))
        cursor.close()
    
    def deleteStudentSubject(self, id_estudiante, id_materia):
        cursor = DB.cursor()
        cursor.execute('delete from student_subjects where student_id = ? and subject_id',(id_estudiante,id_materia))
        cursor.close()

    def deleteStudentSessions(self, idStudent, idSession):
        cursor = DB.cursor()
        cursor.execute('delete from student_sessions where student_id = ? and session_id = ?',(idStudent,idSession,))
        cursor.close()

