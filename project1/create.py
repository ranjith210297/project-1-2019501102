import os
from flask import Flask, render_template, request
from register import *

if not os.getenv("DATABASE_URL"):
	raise RuntimeError("DATABASE_URL IS NOT SET")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
	db.create_all()

if __name__ == "__main__":
	 with app.app_context():
	 	main()