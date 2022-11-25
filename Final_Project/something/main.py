import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_dropzone import Dropzone
basedir = os.path.abspath(os.path.dirname(__file__))
import time

app = Flask(__name__)
app.config.update(
    UPLOADED_PATH= os.path.join(basedir,'uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 5*60*1000)


dropzone = Dropzone(app)
@app.route('/')
def index():
    # render upload page
    #return redirect(url_for('test'))
    return render_template('index.html',filename = "Masterring.jpg")

@app.route("/get_files/<path:filename>")
def get_files(filename):
    """Download a file."""
    print(filename)
    return send_file(os.path.join(app.config['UPLOADED_PATH'], filename), as_attachment=True)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        #@return redirect(url_for('test'))

@app.route('/test')
def test():
    return render_template('main.html')#, working() 

@app.route('/working')
def working():
    time.sleep(5)
    return redirect(url_for('done'))

@app.route('/done')
def done():
    return render_template('done.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)