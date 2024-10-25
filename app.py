from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app  = Flask(__name__)

# DB Congif using sqlLite

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

# Initilize db
db=SQLAlchemy(app)

# Define database Model

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True, nullable=False)
    email=db.Column(db.String(150),unique=True,nullable=False)

    def __repr__(self):
        return f"User('{self.username}),'{self.email}')"


@app.route('/')
def home():
    return render_template('home.html')
    #add new user
    # user=User(username="Alghaliyah",email="g@gmail.com")
    # db.session.add(user)
    # db.session.commit()
    # return f"Added'{user.username} to database"

@app.route('/users')
def users():
    users=User.query.all()
    return render_template('users.html',users=users)


    
@app.route('/about')
def about():
    return "This is about page"

# @app.cli.command('create-db')
# def create_db():
#     with app.app_context():
#         db.create_all()
#         print("Database Created")


if __name__ == '__main__':
    app.run(debug=True)