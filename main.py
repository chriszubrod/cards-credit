from email.mime.text import MIMEText
from flask import (flash,
                   Flask,
                   make_response,
                   redirect,
                   render_template,
                   request,
                   url_for)
from flask import session as flask_session
from googleapiclient.discovery import build
from google.oauth2 import service_account
from httplib2 import Http

import base64
import random
import string

app = Flask(__name__)
app.secret_key = '1!2@3#4$'

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
SERVICE_ACCOUNT_FILE = 'gmail-service-key.json'
INFO_EMAIL = 'info@cardscredit.com'


def service_account_login():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject(INFO_EMAIL)
    service = build('gmail', 'v1', credentials=delegated_credentials)
    return service


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    return {'raw': raw}


def send_inquiry_to_info_account(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: '.format(message['id']))
        return message
    except errors.HttpError as error:
        print('An error occurred: '.format(error))


@app.route("/")
@app.route("/home", methods=['GET'])
def showHome():
    flask_session.clear()
    return render_template('home.html')


@app.route("/inquire", methods=['GET', 'POST'])
def showInquire():

    if request.method == 'GET':
        return render_template('inquire.html')
    elif request.method == 'POST':
        # Get user values from form
        try:
            name = request.form['name-input']
            user_email = request.form['email-input']
            year = request.form['year-input']
            brand = request.form['brand-input']
            athlete = request.form['athlete-input']
            value = request.form['value-input']
            company = request.form['company-select']
            grade = request.form['grade-select']

            subject = '{} - {} - {} - {}'.format(year, athlete, company, grade)
            content = '''NEW INQUIRY

A new inquiry has been submitted with the following details.
    Name: {}
    Email: {}
    Year: {}
    Brand: {}
    Athlete: {}
    Value: {}
    Grade Company: {}
    Grade: {}'''.format(name, user_email, year, brand, athlete, value, company, grade)

            service = service_account_login()
            message = create_message(INFO_EMAIL, INFO_EMAIL, subject, content)
            send_inquiry_to_info_account(service, 'me', message)

            state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                            for x in range(32))
            flask_session['inquiry_state'] = state

            return redirect('/confirmation')

        except Exception as e:
            response = make_response(json.dumps('Failed to get user inputs.'), 401)
            response.headers['Content-type'] = 'application/json'
            return redirect('/inquire')


@app.route("/confirmation", methods=['GET'])
def showConfirmation():
    if 'inquiry_state' not in flask_session:
        return redirect('/home')
    else:
        flask_session.clear()
        return render_template('confirmation.html')


if __name__=="__main__":
    app.run(debug=True)
