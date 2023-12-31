from application import db
from datetime import datetime

class User(db.Model):

    __tablename__ = "users"
    id                = db.Column(db.Integer, primary_key  = True)
    status            = db.Column(db.Boolean, default      = True)
    username          = db.Column(db.Text(128), nullable   = False)
    fullname          = db.Column(db.Text(128), nullale    = False)
    profile_photo_url = db.Column(db.String(255), nullable = False)
    bio               = db.Column(db.String(128))
    created_date      = db.Column(db.DateTime(), default   = datetime.utcnow)
    email             = db.Column(db.Text(64), nullable = False)
    

class Relation(db.Model):

    __tablename__ = "relations"
    id            = db.Column(db.Integer, primary_key = True)
    follower_id   = db.Column(db.Interger, db.ForeignKey("users.id"), nullable = False)
    following_id  = db.Column(db.Interger, db.ForeignKey("users.id"), nullable = False)
    status        = db.Column(db.Boolean, default     = True)
    relation_date  = db.Column(db.DateTime, nullable  = False)

class Post(db.Model):

    __tablename__ = "posts"
    id           = db.Column(db.Integer, primary_key  = True)
    user_id      = db.Column(db.Interger, db.ForeignKey("users.id"), nullable = False)
    image_url    = db.Column(db.String(255), nullable = False)
    caption      = db.Column(db.Text, nullable        = False)
    post_date    = db.Column(db.DateTime, nullable    = False)
    status       = db.Column(db.Boolean, default      = True)

class Comment(db.Model): 

    __tablename__ = "comments"
    id            = db.Column(db.Interger, primary_key=True)
    user_id       = db.Column(db.Interger, db.ForeignKey("users.id"), nullable=False)
    content       = db.Column(db.Text, nullable=False)
    comment_date  = db.Column(db.DateTime, default=datetime.utcnow)
    post_id       = db.Column(db.Interger, db.ForeignKey("posts.id"))
    status        = db.Column(db.Boolean, default      = True) 

class Like(db.Model):

    __tablename__ = "likes"
    id            = db.Column(db.Interger, primary_key=True)
    user_id       = db.Column(db.Interger, db.ForeignKey("users.id"), nullable=False)
    date          = db.Column(db.DateTime, nullable=False)
    post_id       = db.Column(db.Interger, db.ForeignKey("posts.id"), nullable=False)
    created_date  = db.Column(db.DateTime, nullable=False)