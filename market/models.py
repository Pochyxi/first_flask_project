from market import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)


# Creazione del modello che rappresenterà la tabella nel database
class Item(db.Model):
    # id è la primary key ed è obbligatoriamente richiesta
    id = db.Column(db.Integer(), primary_key=True)

    # Column specifica che questa proprietà è una colonna della tabella
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    # String specifica il tipo di dato che viene accettato, lengh limita la lunghezza a 30 caratteri
    price = db.Column(db.Integer(), nullable=False)
    # Nullable indica che questa proprietà non può eseere omessa
    barcode = db.Column(db.String(length=30), nullable=False, unique=True)
    # Unique specifica che non possono esserci altri nomi uguali a questo
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    # si riferisce all'entità User
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
