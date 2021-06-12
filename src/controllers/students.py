from flask import Flask, json, render_template, request, redirect, url_for, flash
from flask.json import jsonify
from src import app
from src.models.subject import SubjectModel
from src.models.students import StudentsModel
from src.models.session import SessionModel
subjectModel = SubjectModel()
studentsModel = StudentsModel()
sessionModel = SessionModel()

@app.route('/materias/<id_materia>/estudiantes')
def students(id_materia):#estudiantes de una materia en especifico  
    #subject = subjectModel.bringSubject(id)   
    students = studentsModel.bringStudents(id_materia)
    #print(students)
    return jsonify({'estudiantes':students})


@app.route('/estudiantes',methods=['GET','POST'])
def estudiantes():
    if request.method == 'GET':
        estudiantes= studentsModel.estudiantes()
        
        return jsonify({'estudiantes': estudiantes})

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    identificacion = request.json['identificacion']
    telefono = request.json['telefono']
    email = request.json['email']
    semestre = request.json['semestre']
    
    studentsModel.insertStudent(identificacion, nombre, apellido, telefono, email, semestre)

    return jsonify({
        'identificacion': identificacion,
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'email': email,
        'semestre': semestre
    })







@app.route('/estudiantes/<id_estudiante>',methods=['PUT','DELETE'])
def studentEdit(id_estudiante):
    if request.method == 'DELETE':
        studentsModel.borrar_estudiante(id_estudiante)
    
        return jsonify({
            'mensaje':'Borrado'
        })
    
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    identificacion = request.json['identificacion']
    telefono = request.json['telefono']
    email = request.json['email']
    semestre = request.json['semestre']

    #print(name, surname, idStudent, phone, email, semester)
    studentsModel.editStudent(identificacion, nombre, apellido, telefono, email, semestre, id_estudiante)

    return jsonify({
        'estudiante':{
            'identificacion': identificacion,
            'nombre': nombre,
            'apellido': apellido,
            'telefono': telefono,
            'email': email,
            'semestre': semestre
        }
    })


@app.route('/estudiantes/<id_estudiante>/materias/<id_materia>',methods=['DELETE'])
def studentSubjectDelete(id_estudiante, id_materia):
    
    studentsModel.deleteStudentSubject(id_estudiante,id_materia)
    
    sessions = sessionModel.bringSessions(id_materia)
    
    for session in sessions:
       studentsModel.deleteStudentSessions(id_estudiante,session['id'])
    
   
    return jsonify({'mensaje':'Borrado'})

@app.route('/estudiantes/<id_estudiante>/materias/<id_materia>',methods=['POST'])
def studentSubjectPost(id_estudiante, id_materia):
    
    studentsModel.insertStudentSubject(id_estudiante, id_materia)
    sessions = sessionModel.bringSessions(id_materia)
    
    for sesion in sessions:
        sessionModel.insertStudentSessions(id_estudiante,sesion['id'])

    return jsonify({
        'estudiante':studentsModel.bringStudent(id_estudiante),
        'materia':subjectModel.bringSubject(id_materia)[1]
    })

