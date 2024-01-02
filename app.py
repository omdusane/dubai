import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD']=os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER']=os.getenv('MAIL_USERNAME')
mail = Mail(app)

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/about-us", methods=['GET'])
def about_us():
    return render_template("about-us.html")

@app.route("/contact-us", methods=['GET', 'POST'])
def contact_us():
    # print("111")
    # msg = Message('TCIA Dubai Website Query', sender = 'omdusane8@gmail.com', recipients = ['omdusane8@gmail.com'])
    # msg.body = "Hello Flask message sent from Flask-Mail"
    
    # # You can also use msg.html to send html templates!
    # # Example:
    # # msg.html = render_template("hello.html") # Template should be in 'templates' folder
    
    # mail.send(msg)
    # return "Your email has been sent!"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            subject = request.form["subject"]
            company_name = request.form["company_name"]
            description = request.form["description"]
            msg = Message('TCIA Dubai Website Query', sender = 'omdusane8@gmail.com', recipients = ['omdusane8@gmail.com'])
            msg.body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nCompany Name: {company_name}\nDescription: {description}"
            mail.send(msg)

            flash("Form Submitted Successfully")
            return redirect(url_for('contact_us'))
        except:
            flash("Internal Server Error", 'error')
            return redirect(url_for(contact_us))
        
    return render_template("contact-us.html")

@app.route('/sap-services',methods=['GET'])
def sap_services():
    return render_template('sap-services.html')

@app.route('/assessment-services',methods=['GET'])
def assesment_services():
    return render_template('assessment-services.html')

@app.route('/it-services',methods=['GET'])
def it_services():
    return render_template('it-services.html')

@app.route('/services',methods=['GET'])
def cloud_services():
    return render_template('services.html')

@app.route('/trainings',methods=['GET'])
def trainings():
    return render_template('trainings.html')


if __name__ == '__main__':
    app.run(debug=True)