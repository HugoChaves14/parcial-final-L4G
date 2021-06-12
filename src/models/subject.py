from src.config.db import DB

class SubjectModel():

    def bringSubjects(self):
        cursor = DB.cursor()
        cursor.execute('select * from subjects')
        subjects = cursor.fetchall()
        cursor.close()
        materias = []
        for materia in subjects:
            materias.append({
                'id': materia[0],
                'nombre': materia[1],
                'semestre': materia[2],
                'estudiantes':'http://127.0.0.1:5000/materias/'+str(materia[0])+'/estudiantes'
            }) 
        return materias


    def bringSubject(self,id):
        cursor = DB.cursor()
        cursor.execute('select * from subjects where id = ?',(id,))
        subject = cursor.fetchone()
        cursor.close()
        return subject
        

    def insertSubject(self, name, semester):
        cursor = DB.cursor()

        cursor.execute('insert into subjects(name, semester) values(?, ?)',(name, semester))

        cursor.close()
        
