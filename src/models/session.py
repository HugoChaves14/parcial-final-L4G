from src.config.db import DB

class SessionModel():

    def insertSession(self,subjectId, name, description, date, startTime, endTime):

        cursor = DB.cursor()
        cursor.execute('insert into sessions(subject_id, name, description, date, start_time, end_time) values(?, ?, ?, ?, ?, ?)',(subjectId, name, description, date, startTime, endTime,))

        cursor.close()

    def bringSession(self,id_materia, name):
        cursor = DB.cursor()
        cursor.execute('select * from sessions where subject_id=? and name = ?',(id_materia, name,))
        session = cursor.fetchone()
        cursor.close()
        return session

    def bringSessions(self, subjectId):
        cursor = DB.cursor()
        cursor.execute('select * from sessions where subject_id = ?',(subjectId,))
        sessions = cursor.fetchall()
        cursor.close()
        sesiones = []
        for sesion in sessions:
            sesiones.append({
                'id':sesion[0],
                'nombre':sesion[2],
                'descripcion':sesion[3],
                'fecha':str(sesion[4]),
                'hora_inicio':str(sesion[5]),
                'hora_finalizacion':str(sesion[6]),
                'asistencia':'http://127.0.0.1:5000/sesiones/'+str(sesion[0])+'/estudiantes'
            })
        return sesiones

    def insertStudentSessions(self, studentId, sessionId):
        cursor = DB.cursor()
        cursor.execute('insert into student_sessions(student_id, session_id) values(?, ?)',(studentId, sessionId))
        cursor.close()

    def bringStudentsSession(self, sessionId):
        cursor = DB.cursor()
        cursor.execute('SELECT students.id, st_se.id, students.idn, students.name, students.surname, students.phone, students.email, students.semester, sessions.name,  st_se.check_attendance,sessions.id FROM students INNER JOIN student_sessions AS st_se ON students.id = st_se.student_id INNER JOIN sessions ON st_se.session_id = sessions.id WHERE sessions.id = ?',(sessionId,))
        students = cursor.fetchall()
        estudiantes = []
        for estudiante in students:
            estudiantes.append({
                'id': estudiante[0],
                'identificacion': estudiante[2],
                'nombre': estudiante[3],
                'apellido': estudiante[4],
                'telefono': estudiante[5],
                'email': estudiante[6],
                'semestre': estudiante[7],
                'ver_asistencia':'http://127.0.0.1:5000/sesiones/'+str(estudiante[1])+'/estudiantes',
                'asistencia': estudiante[9]
            })
        return estudiantes

    def updateAttendance(self, check,id):
        cursor = DB.cursor()
        cursor.execute('update student_sessions set check_attendance = ? where id = ?',(check,id))
        cursor.close()


     