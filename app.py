from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply


app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome !"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """
    Respon to incoming msgs
    """
    msg = request.form.get('Body')
    phone_no = request.form.get('From')

    reply = fetch_reply(msg, phone_no)


    resp = MessagingResponse()
    resp.message(f"ECHO: {reply}")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
