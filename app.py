from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/about-us", methods=['GET'])
def about_us():
    return render_template("about-us.html")

@app.route("/contact-us", methods=['GET', 'POST'])
def contact_us():

    if request.method == "POST":
        name = request.form["name"]

        flash("Form Submitted Successfully")
        return redirect(url_for(contact_us))

    return render_template("contact-us.html")

if __name__ == '__main__':
    app.run(debug=True)