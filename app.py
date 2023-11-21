from flask import Flask, render_template,request,redirect
import mysql.connector
import datetime
from flask_mail import Mail,Message
app=Flask(__name__) 
app.secret_key="Nishant"
#----------------------------------------------------------------mail-----------------------------------------------------------------
app.config['SECRET KEY']='Nishant'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587

app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='flaskresturant2023@gmail.com'
app.config['MAIL_PASSWORD']='boxmcwvnaemxtpgi'

mail=Mail(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/response",methods=['post'])
def access():
    if request.method=="POST":
        name=request.form['nam']
        email=request.form['emal']
        date=request.form['dat']
        person=request.form['per']
        msg=request.form['comt']
        mssg=Message(
            'New Order Submit',
            sender="flaskresturant2023@gmail.com",
            recipients=[email,'shrivastavanishant600@gmail.com'],
            body=f'Name:{name}\nEmail:{email}\nDate:{date}\nTable:{person}\nYour Specail Request:{msg}'
            
        )
        mail.send(mssg)
        

       
    
    
        
    return redirect("/")
    
    

@app.route("/about")
def abt():
    return render_template("about.html")

@app.route("/service")
def ser():
    return render_template("service.html")


@app.route("/menu")
def men():
    return render_template("menu.html")

@app.route("/testimonial")
def test():
    return render_template("testimonial.html")


@app.route("/booking")
def book():
    return render_template("booking.html")


@app.route("/team")
def tem():
    return render_template("team.html")


@app.route("/contact")
def cnt():
    return render_template("contact.html")
@app.route("/query",methods=['post'])
def acc():
    if request.method=="POST":
        name=request.form['nm']
        email=request.form['mal']
        date=datetime.date.today()
        subject=request.form['sub']
        msg=request.form['comr']
        mssg=Message(
            'New Query Generated',
            sender="flaskresturant2023@gmail.com",
            recipients=[email,'shrivastavanishant600@gmail.com'],
            body=f'Name:{name}\nEmail:{email}\nDate:{date}\nSubject:{subject}\nYour Msg:{msg}'
            
        )
        mail.send(mssg)
        return redirect("/contact")




