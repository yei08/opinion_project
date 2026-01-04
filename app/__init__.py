from flask import Flask

app = Flask(__name__)

from app import routes # Imported at the end to avoid circular imports