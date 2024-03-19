import os
from flask import Flask, render_template, redirect, url_for, request, flash
# from flask_mail import Mail, Message
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from utils import db
from models import Enquiries, Newsletter
from os import path
load_dotenv()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///enquiries.db'

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/about", methods=['GET'])
def about_us():
    return render_template("about.html")

@app.route("/product", methods=['GET'])
def product():
    return render_template("product.html")
@app.route("/product/automation-services", methods=['GET'])
def automation_services():
    return render_template("autoservices.html")

@app.route("/product/automation-services/cctv-solutions", methods=['GET'])
def cctv_solutions():
    return render_template("cctv.html")

@app.route("/product/automation-services/home-automation-solutions", methods=['GET'])
def home_automation_solutions():
    return render_template("homeauto.html")

@app.route("/product/automation-services/biometric-solutions", methods=['GET'])
def biometric_solutions():
    return render_template("biometric.html")

@app.route("/product/sap-services", methods=['GET'])
def sap_services():
    return render_template("sap.html")

@app.route("/product/sap-services/basic-sap-service", methods=['GET'])
def basic_sap():
    return render_template("basicsap1.html")

@app.route("/product/sap-services/consulting-sap-service", methods=['GET'])
def consulting_sap():
    return render_template("consultingsap2.html")

@app.route("/product/sap-services/sap-on-public-cloud", methods=['GET'])
def public_sap():
    return render_template("publicsap3.html")

@app.route("/product/assessment-services", methods=['GET'])
def assessment_services():
    return render_template("assessment.html")

@app.route("/product/assessment-services/cost-assessment-consulting", methods=['GET'])
def cac_services():
    return render_template("aservices1.html")

@app.route("/product/assessment-services/cloud-roadmap-and-stratergy-services", methods=['GET'])
def crass_services():
    return render_template("aservices2.html")

@app.route("/product/assessment-services/cloud-design-services", methods=['GET'])
def cd_services():
    return render_template("aservices3.html")

@app.route("/product/assessment-services/cloud-security-services", methods=['GET'])
def cs_services():
    return render_template("aservices4.html")

@app.route("/product/assessment-services/cloud-migration-services", methods=['GET'])
def cm_services():
    return render_template("aservices5.html")

@app.route("/product/assessment-services/cloud-viability-study-and-migration-plan", methods=['GET'])
def cvsamp_services():
    return render_template("aservices6.html")

@app.route("/product/assessment-services/why-public-cloud", methods=['GET'])
def wpc():
    return render_template("aservices7.html")

@app.route("/product/it-services", methods=['GET'])
def it_services():
    return render_template("itservices.html")

@app.route("/product/it-services/advisory-services", methods=['GET'])
def advisory_services():
    return render_template("it1.html")

@app.route("/product/it-services/aws", methods=['GET'])
def aws():
    return render_template("it2.html")

@app.route("/product/it-services/cloud-computing", methods=['GET'])
def cloud_computing():
    return render_template("it3.html")

@app.route("/product/it-services/azure-and-azure-sql", methods=['GET'])
def azure():
    return render_template("it4.html")

@app.route("/product/it-services/devops", methods=['GET'])
def devops():
    return render_template("it5.html")

@app.route("/product/it-services/office-365", methods=['GET'])
def o365():
    return render_template("it6.html")

@app.route("/product/it-services/oracle-database", methods=['GET'])
def oracle_db():
    return render_template("it7.html")

@app.route("/product/it-services/vmware", methods=['GET'])
def vmware():
    return render_template("it8.html")

@app.route("/product/it-services/data-centre-security", methods=['GET'])
def dcs():
    return render_template("it9.html")

@app.route("/product/it-services/networking", methods=['GET'])
def networking():
    return render_template("it10.html")

@app.route("/product/it-services/backup-and-disaster-recovery", methods=['GET'])
def badr():
    return render_template("it11.html")

@app.route("/product/it-services/business-continuity", methods=['GET'])
def bc():
    return render_template("it12.html")

@app.route("/product/it-services/trainings", methods=['GET'])
def trainings():
    return render_template("it13.html")

@app.route("/product/cloud-services", methods=['GET'])
def cloud_services():
    return render_template("cservices.html")

@app.route("/product/cloud-services/managed-services", methods=['GET'])
def managed_services():
    return render_template("cs1.html")

@app.route("/product/cloud-services/devops", methods=['GET'])
def devops_cloud_services():
    return render_template("cs2.html")

@app.route("/product/cloud-services/disaster-recovery-as-a-service", methods=['GET'])
def draas():
    return render_template("cs3.html")

@app.route("/product/cloud-services/vpn-services", methods=['GET'])
def vpn_services():
    return render_template("cs4.html")

@app.route("/product/cloud-services/aws-backup-and-disaster-recovery", methods=['GET'])
def aws_badr():
    return render_template("cs5.html")

@app.route("/product/cloud-services/microsoft-workloads-on-aws", methods=['GET'])
def microsoft_workloads():
    return render_template("cs6.html")

@app.route("/store", methods=['GET'])
def store():
    return render_template("store.html")

@app.route("/feature", methods=['GET'])
def feature():
    return render_template("feature.html")

@app.route("/blog", methods=['GET'])
def blog():
    return render_template("blog.html")

@app.route("/testimonial", methods=['GET'])
def testimonial():
    return render_template("testimonial.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    print("start")
    if request.method == "POST":
        print("1")
        try:
            print("2")
            name = request.form["name"]
            email = request.form["email"]
            subject = request.form["subject"]
            message = request.form["message"]
            new_query = Enquiries(name=name,email=email,subject=subject,message=message)
            db.session.add(new_query)
            db.session.commit()

            print("added Successfully *******************888")
            flash("Form Submitted Successfully")
            return redirect(url_for('contact'))
        except:
            flash("Internal Server Error", 'error')
            print("NOT SUBMITTED")
            return redirect(url_for('contact'))
        
    return render_template("contact.html")

@app.route("/newsletter-signup", methods=['POST'])
def newsletter_signup():
    print('1')
    if request.method == "POST":
        print('2')
        try:
            print('3')
            email = request.form["email"]
            new_mail = Newsletter.query.filter_by(email=email).first()
            if new_mail is None:
                print('4')
                new_entry = Newsletter(email=email)
                db.session.add(new_entry)
                db.session.commit()
                return redirect(url_for('home'))
            else:
                flash('You have alredy signed up for the newsletter')
                return redirect(url_for('home'))
        except:
            flash("Internal Server Error", 'error')
            return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)