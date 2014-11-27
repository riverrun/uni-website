from passlib.context import CryptContext
from website import db
from sqlalchemy.dialects.postgresql import JSON


pwd_ctx = CryptContext(schemes=['bcrypt', 'sha512_crypt', 'pbkdf2_sha256'],
        default='sha512_crypt')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))
    answer_page = db.Column(JSON)

    def __init__(self, username, password, answer_page='{}'):
        self.username = username
        self.hash_password(password)
        self.answer_page = answer_page

    def hash_password(self, password):
        self.password_hash = pwd_ctx.encrypt(password)

    def check_password(self, password):
        return pwd_ctx.verify(password, self.password_hash)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.String())
    content = db.Column(JSON)

    def __init__(self, content_id, content):
        self.content_id = content_id
        self.content = content

    def __repr__(self):
        return '<Content {}>'.format(self.content_id)

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.String())
    section_id = db.Column(db.String())
    question_page = db.Column(JSON)

    def __init__(self, exam_id, section_id, question_page):
        self.exam_id = exam_id
        self.section_id = section_id
        self.question_page = question_page

    def __repr__(self):
        return '<Exam {}, section {}>'.format(self.exam_id, self.section_id)
