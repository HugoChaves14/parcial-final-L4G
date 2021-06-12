from flask import  request, json
from src import app
from src.models.subject import SubjectModel
from src.models.students import StudentsModel
from src.models.session import SessionModel
subjectModel = SubjectModel()
sessionModel = SessionModel()
studentsModel = StudentsModel()

@app.route('/materias/<id_materia>/sesiones',methods=['GET','POST'])
def sesiones_materia(id_materia):
    if request.method == 'GET':
        sessions = sessionModel.bringSessions(id_materia)
        return json.jsonify({
            'sesiones':sessions,
            'materia':subjectModel.bringSubject(id_materia)[1]
        })

    name = request.json['nombre']
    description = request.json['descripcion']
    date = request.json['fecha']
    startTime = request.json['hora_inicio']
    endTime = request.json['hora_finalizacion']

    sessionModel.insertSession(id_materia, name, description, date, startTime, endTime)

    students = studentsModel.bringStudents(id_materia)
    session = sessionModel.bringSession(id_materia,name)
    print(session)
    for student in students:
        sessionModel.insertStudentSessions(student['id'],session[0])

    return json.jsonify({
        'materia': subjectModel.bringSubject(id_materia)[1],
        'sesion':{
            'id':session[0],
            'nombre':session[2],
            'descripcion':session[3],
            'date':str(session[4]),
            'hora_inicio':str(session[5]),
            'hora_finalizacion':str(session[6])
        }
    })



    
@app.route('/sesiones/<id_sesion>/estudiantes',methods=['GET','PUT'] )
def sessionAttendance(id_sesion):
    if request.method == 'GET':
        students = sessionModel.bringStudentsSession(id_sesion)
        #subject = subjectModel.bringSubject(subId)
        #print(students)

        return json.jsonify({
            'estudiantes':students
        })

    numero  = request.json['numero']
    sessionModel.updateAttendance(numero,id_sesion)
    if numero == 1:
        return json.jsonify({'mensaje':'Asistio'})
    else:
        return json.jsonify({'mensaje':'No asistio'})



