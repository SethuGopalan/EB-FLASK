from flask import Flask, render_template

application = app= Flask(__name__)

@application.route("/")
def index():
    return render_template('index.html', title='Index')

@application.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

if __name__ == '__main__':
    application.debug = True
    application.run()
    