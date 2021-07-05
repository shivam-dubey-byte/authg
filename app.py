from flask import Flask, render_template, redirect
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os

app = Flask(__name__)

# Below code does the authentication
# part of the code
gauth = GoogleAuth()

# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

@app.route('/')
def index():
	path = r"E:\Google Api"

	for x in os.listdir(path):
	    f = drive.CreateFile({'title': x})
	    f.SetContentFile(os.path.join(path, x))
	    f.Upload()
	    f = None
	return render_template('index.html')
if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0",port=8000)
