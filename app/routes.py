from app import app
from flask import render_template, request
from app.models import model, formopener
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/title', methods = ["GET", "POST"])
def title():
    if request.method == "GET":
        return "Enter in a movie"
    else:
        userdata = request.form
        title = userdata['title']
        print(title)
        runtime = model.get_runtime_by_title(title)
        runtime = int(runtime.strip(" min"))
        popcornsize = model.get_popcorn_size(runtime)
        return render_template("popcornanswers.html", title = title, popcornsize = popcornsize, runtime = runtime)
        
@app.route('/results', methods = ["GET","POST"])
def results():
    return render_template("result.html")
    
@app.route('/information', methods = ["GET", "POST"])
def work():
    if request.method == "POST":
        userdata = request.form
        movname = userdata['information']
        answers = model.getanswers(movname)
        print(answers)
        runtime = answers[0]
        title = answers[1]
        year = answers[2]
        rating = answers[3]
        return render_template("imdbAnswers.html", movname = movname, answers = answers, runtime = runtime, title = title, year = year, rating = rating)
    else:
        return "Enter IN a movie"
    
@app.route('/sendEmail', methods = ["GET", "POST"])
def sendEmail():
    userdata = request.form
    email = userdata['email'].decode("utf-8")
    emailBody = userdata['message'].decode("utf-8")
    message = Mail()
    from_email='atticusrothschild@gmail.com',
    to_emails=email,
    subject='Comments',
    html_content='<strong>' + emailBody + '</strong>'

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print(response.status_code)
    except Exception as e:
        print("ERROR:")
        print(e)
        
    return render_template("index.html")