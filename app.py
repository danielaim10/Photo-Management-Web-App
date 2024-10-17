from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import os
from utils import allowed_file, save_image

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Dummy admin credentials
ADMIN_USERNAME = 'tema'
ADMIN_PASSWORD = 'tema'

categories = ['Nature', 'Animals','People']

@app.route('/')
def index():
    categories = os.listdir(app.config['UPLOAD_FOLDER'])
    images = {category: os.listdir(os.path.join(app.config['UPLOAD_FOLDER'], category)) for category in categories}
    return render_template('index.html', images=images)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('upload'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('index'))
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not session.get('admin'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        
        if file and allowed_file(file.filename, app.config['ALLOWED_EXTENSIONS']):
            new_name = request.form.get('rename')
            filename = secure_filename(new_name if new_name else file.filename)
            category = request.form.get('category') or 'uncategorized'
            save_image(file, filename, category, app.config['UPLOAD_FOLDER'])
            flash('File successfully uploaded', 'success')
            return redirect(url_for('upload'))
    return render_template('upload.html', categories=categories)
@app.route('/delete/<category>/<image_name>', methods=['POST'])
def delete_image(category, image_name):
    if 'admin' in session:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], category, image_name)
        if os.path.exists(image_path):
            os.remove(image_path)
            flash('Image deleted successfully!', 'success')
        else:
            flash('Image not found!', 'danger')
    else:
        flash('You do not have permission to perform this action.', 'danger')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
