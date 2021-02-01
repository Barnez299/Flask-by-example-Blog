import os
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from config import Configuration # import our configuration data




app = Flask(__name__)
app.config.from_object(Configuration) # use values from our configuration object
db = SQLAlchemy(app)
migrate = Migrate(app, db)

