from flask import render_template, Blueprint, session, request,redirect,url_for,flash
from flask_login import login_required, current_user, logout_user, login_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.sql import func
from application import app, db
from .forms import Cal


@app.route('/fitness', methods=['GET','POST'])
def fitness():
    form = Cal()
    exe = Fitness.query.all()

    
    if form.validate_on_submit() and request.method == "POST":
        #exercise = request.form['item']
        weight = form.Weight.data
        timehr = form.DurationHR.data
        timemin = form.DurationMin.data
        exercise = form.ExerciseType.data
        
        data = Fitness.query.filter_by(ExerciseType=exercise).all()
        time = (timehr * 60) + timemin  
       

        

        if weight < 155 and exercise == "Weights":
            calories = time * 180/30
            return render_template('/fitness/exercise.html', form=form, calories=calories, value=data, items=exe)
        if weight < 155 and exercise == "Walking":
            calories = time * 135/30
            return render_template('/fitness/exercise.html', form=form, calories=calories, value=data, items=exe)
        if weight < 155 and exercise == "Jump Rope":
            calories = time * 300/30
            return render_template('/fitness/exercise.html', form=form, calories=calories, value=data, items=exe)
 
        if weight >= 155 and weight < 185 and exercise == "Weights":
            calories = time * 223/30
            return render_template('/fitness/exercise.html', form=form, calories=calories, value=data, items=exe)
        if weight >= 155 and weight < 185 and exercise == "Walking":
            calories = time * 167/30
            return render_template('/fitness/exercise.html', form=form, calories=calories, value=data, items=exe)
        if weight >= 155 and weight < 185 and exercise == "Jump Rope":
            calories = time * 372/30
            return render_template('/fitness/exercise.html', form=form, calories=calories, value=data, items=exe)

        if weight > 185 and exercise == "Weights":
            calories = time * 266/30
            return render_template('/fitness/exercise.html', form=form, calories=calories, value=data, items=exe)
        if weight > 185 and exercise == "Walking":
            calories = time * 200/30
            return render_template('/fitness/exercise.html', form=form, calories=calories, value=data, items=exe)
        if weight > 185 and exercise == "Jump Rope":
            calories = time * 444/30
            return render_template('/fitness/exercise.html', form=form, calories=calories, value=data, items=exe)


        return render_template('/fitness/exercise.html', form=form, value=data, weight=weight, time=time, items=exe, exercise=exercise)

    return render_template('/fitness/exercise.html', form=form, items=exe)


@app.route('/calFitness', methods=['GET', 'POST'])
def cal():

    data = Fitness.query.all()
    

    return render_template('/fitness/cal.html', items=data)



from .models import Fitness