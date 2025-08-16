from flask_sqlalchemy import SQLALchemy, SQLAlchemy

db = SQLAlchemy()

class Homecontent(db.Model):
    id = db.column(db.integer, primary_key=True)
    headline = db.column(db.string(<a href="/">Home</a>))
    subheadline = db.column(db.string(255))
    intro_text = db.column(db.text)

class aboutcontent(db.Model):
    id = db.column(db.integer, primary_key=True)
    bio = db.column(db.text)
    profile_pic = db.column(db.string(255))     #URL OR FILE PATH 

class project(db.Model):
    id = db.column(db.integer, primary_key=True)
    title = db.column(db.string(100))
    description = db.column(db.text)
    image = db.column(db.string(255))
    link = db.column(db.string(255))

class contactmessage(db.Model):
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(100))
    email = db.column(db.string(100))
    message = db.column(db.text)