from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reptile(db.Model):
    __tablename__ = 'reptiles'

    id = db.Column(db.Integer, primary_key = True)
    common_name = db.Column(db.String(250))
    sci_name = db.Column(db.String(250))
    habitat = db.Column(db.String(250))
    fun_fact = db.Column(db.Text)