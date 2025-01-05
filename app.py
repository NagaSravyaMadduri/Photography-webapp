from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
import os
from extensions import db
from models import BlogPost
from forms import PostForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
db.init_app(app)
migrate = Migrate(app, db)

# Ensure the uploads directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

with app.app_context():
    db.create_all()  # Ensure tables are created

@app.route('/')
def index():
    posts = BlogPost.query.all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        file = form.image.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_post = BlogPost(title=form.title.data, content=form.content.data, image_filename=filename)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_post.html', form=form)

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000, debug=True)
