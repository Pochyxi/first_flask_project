from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# inizializzare l'app flask
app = Flask(__name__)

# configurare il database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'dba43639487b75d5ac62d9f4'

# collegare l'app al database
db = SQLAlchemy(app)

from market import routes

# aprire il terminale nella cartella di progetto e scrivere python
# poi digitare le seguenti righe di codice per creare i database
# >>> from market import app, db
# >>> app.app_context().push()
# >>> db.create_all()

# per creare il vostro primo item sul db digitare nel terminale python
# >>> item1 = Item(name='iphone 10', price=500, barcode='83833738738', description='desc')
# >>> db.session.add(item1)
# >>> db.session.commit()
# >>> Item.query.all()
# risultato atteso -----> [<Item 1>]

# ricercare tutti gli elementi nel database
# Item.query.all() ----> ritorna una list di Item

# ricercare con un filtro tutti gli elementi nel database
#  Item.query.filter_by(price=500)

# per resettare il database :
# >>> app.app_context().push()
# >>> db.drop_all()
# >>> db.create_all()

# filtrare un utente per nome utente e ritornarne solo 1 elemento:
# i1.owner = User.query.filter_by(username='jsc').first().id

# flask-wtf
# pip install wtforms
