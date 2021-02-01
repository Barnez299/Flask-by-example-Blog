import datetime, re
from app import db

def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True)
    body = db.Column(db.Text)
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

def __init__(self, *args, **kwargs):
    super(Post, self).__init__(*args, **kwargs) # Call parent constructor
    self.generate_slug()

def generate_slug(self):
    self.slug = ''
    if self.title:
        self.slug = slugify(self.title)

def __repr__(self):
    return '<Post: %s>' % self.title