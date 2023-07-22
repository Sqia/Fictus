#   Copyright 2023 Aqila
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# Library
from flask import Flask, request
from twilio.rest import Client
# Fictus library
from fictus.env_manager import get_account_sid, get_auth_token, get_from
from fictus.model import predict_news

app = Flask("server_api")
PORT = 5000
IS_DEBUG = True


ACCOUNT_SID = get_account_sid()
AUTH_TOKEN = get_auth_token()
FROM = get_from()
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_message(message: str, to: str):
    response = client.messages.create(
        from_=f"whatsapp:{FROM}", # 'whatsapp:+14155238886'
        body=message, # 'Your appointment is coming up on July 21 at 3PM'
        to=f"whatsapp:{to}" # 'whatsapp:+62895410047408'
    )
    return response

@app.route("/")
def home():
    return "Server api"

@app.route("/whatsapp", methods=["GET", "POST"])
def whatsapp():
    print(request.get_data())
    message = request.form['Body']
    sender_id = request.form['From'].split('+')[1]
    print(f'Message --> {message}')
    print(f'Sender id --> {sender_id}')
    response = send_message(predict_news(message), sender_id)
    print(f'This is the response --> {response}')
    return '200'

if __name__ == "__main__":
    app.run(port=PORT, debug=IS_DEBUG, host="0.0.0.0")
