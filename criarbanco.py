from site_pinterest import app, database
from site_pinterest.models import Usuario, Foto

with app.app_context():
    database.drop_all()
    database.create_all()