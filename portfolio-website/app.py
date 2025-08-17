from flask import Flask, request, jsonify
from models import db, Homecontent, aboutcontent, project, contactmessage

app = Flask(__name__)
app.config['SQLALCHMEY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

# Home page content
@app.route('/api/home', methods=['GET'])
def get_home():
    content = Homecontent.query.first()
    return jsonify({
        ''
        'headline': content.headline,
        'subheadline': content.subheadline,
        'intro_text': content.intro_text
    }) if content else('', 404)

#about page content 
@app.route('/api/about', methods={'GET'})
def get_about():
    content = aboutcontent.query.first()
    return jsonify({
        'bio': content.bio,
        'profile_pic': content.profile_pic
    }) if content else ('', 404)

# project list
@app.route('/api/projects', methods=['GET'])
def get_prpjects():
      projects = project.query.all()
      return jsonify([{
        'title': p.title,
        'description': p.description,
        'image': p.image,
        'link':p.link
    } for p in projects])

# contact form submission
@app.route('/api/contact', method=['GET'])
def submit_contact():
     data = request.get_json()
     msg = contactmessage(
          name=data.get('name'),
          email=data.get('email'),
          message=data.get('message')
     )
     db.session.add(msg)
     db.session.commit()
     return jsonify({'message': 'contact message sent!'}), 201

db.init_app(app)

from flask_admin import admin
from flask_admin.contrib.sqla import modelview

admin = admin(app, name='portfolio'),
admin.add_view(modelview(Homecontent)),
admin.add_view(modelview(aboutcontent)),
admin.add_view(modelview(project)),
admin.add_view(modelview(contactmessage))

if __name__ == '__main__':
     with app.app_context():
          db.create_all()
          app.run(debug=True)
