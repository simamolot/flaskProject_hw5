from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)


    questions = db.relationship('Questions', backref='category', lazy=True)


class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_text = db.Column(db.String(255), nullable=False)


    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)



