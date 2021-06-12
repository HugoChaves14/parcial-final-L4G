from flask import request 
from flask.json import jsonify
from src import app
from src.models.subject import SubjectModel
subjectModel = SubjectModel()

@app.route('/materias',methods=['GET','POST'])
def subjects():
    if request.method == 'GET':
        subjects = subjectModel.bringSubjects()
        print(subjects)


        return jsonify({'materias':subjects})

    nombre = request.json['nombre']
    semestre = request.json['semestre']

    subjectModel.insertSubject(nombre, semestre)

    return jsonify({
        'materia':{
            'nombre':nombre,
            'semestre':semestre
        } 
    })


