import datetime
import json
import os
from unidecode import unidecode

from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path="/photos", static_folder="photos")

@app.route('/')
def home():
    return redirect("/upload")

@app.route('/upload')
def upload_file():
    return render_template("upload.html")


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return render_template("messages.html", data=read_file(f.filename))


def read_file(filename):
    messages_list = [""]

    with open(filename) as json_file:
        data = json.load(json_file)

        for p in data['participants']:
            messages_list.insert(0, 'participants: ' + p['name'])

        for p in data['messages']:
            if 'content' in p and p['content'] != "":
                messages_list.insert(0, 'sender: ' + p['sender_name'])
                messages_list.insert(0, 'time: ' + convert_time(p['timestamp_ms']))
                messages_list.insert(0, 'content: ' + p['content'])

            elif 'photos' in p:
                for p in p['photos']:
                    messages_list.insert(0, 'url: ' + p['uri'])
                    # print('creation timestamp: ' + convert_time(p['creation_timestamp']))\

    # delete file from server (the user's data should not be accessible for reading after processing)
    os.remove(filename)

    return messages_list


def convert_time(ms_since_1970):
    return datetime.datetime.fromtimestamp(ms_since_1970 / 1000).strftime('%Y-%m-%d %H:%M')


if __name__ == '__main__':
    app.run(debug=True)
