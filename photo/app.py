from flask import Flask, request, render_template, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            message = 'No file part'
            return render_template('upload.html', message=message)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            message = 'No selected file'
            return render_template('upload.html', message=message)
        if file and allowed_file(file.filename):
            # save file to uploads folder
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            message = 'File uploaded successfully'
            return render_template('upload.html', message=message)
        else:
            message = 'File format not supported. Please select a valid image file'
            return render_template('upload.html', message=message)
    return render_template('upload.html')

@app.route('/gallery')
def gallery():
    # get list of uploaded files
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    # create list of URLs for each file
    urls = [url_for('static', filename=f'uploads/{file}') for file in files]
    return render_template('gallery.html', urls=urls)

if __name__ == '__main__':
    app.run(debug=True)
