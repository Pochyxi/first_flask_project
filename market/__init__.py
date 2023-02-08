from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

# inizializzare l'app flask
app = Flask(__name__)

# configurare il database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# collegare l'app al database
db = SQLAlchemy(app)

from market import routes
