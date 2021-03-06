from .. import db
from werkzeug.security import generate_password_hash, check_password_hash
import random, string

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, unique=True)
	first_name = db.Column(db.String)
	last_name = db.Column(db.String)
	pw_hash = db.Column(db.String)
	editor = db.Column(db.String)
	fontsize = db.Column(db.String)
	confirmed = db.Column(db.Boolean, nullable=False, default=False)

	def __init__(self, email, first_name=None, last_name=None,password=None,
				confirmed=False):
		self.email = email.lower()
		self.first_name = first_name
		self.last_name = last_name
		self.set_password(password)
		self.confirmed = confirmed
		self.editor = "NONE"
		self.fontsize = "12"


	def set_password(self, password):
		# If the password was not specified (Login from Facebook/Google then
		# create a random 32 charachter password)
		# Otherwise users can login by entering empty string as password
		if password is None:
			password = ''.join(random.choice(string.ascii_uppercase +
				string.digits) for _ in range(32))
		self.pw_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pw_hash, password)

	# These four methods are for Flask-Login
	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

	def get_editor(self):
		return self.editor

	def set_editor(self, ed):
		self.editor = ed

	def get_email(self):
		return self.email

	def get_first_name(self):
		return self.first_name

	def get_fontsize(self):
		return self.fontsize

	def set_fontsize(self, fs):
		self.fontsize = fs

	def is_email_confirmed(self):
		return self.confirmed
