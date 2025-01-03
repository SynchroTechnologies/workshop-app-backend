import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS en la aplicación

database_host = os.getenv('DATABASE_HOST', 'localhost')
database_user = os.getenv('DATABASE_USER', 'synchro')
database_password = os.getenv('DATABASE_PASSWORD', 'synchro')
database_name = os.getenv('DATABASE_NAME', 'app')

port = os.getenv('PORT', 5000)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_user}:{database_password}@{database_host}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechaHora = db.Column(db.String(25), nullable=False)
    timezone = db.Column(db.String(50), nullable=False)
    podHostname = db.Column(db.String(200))
    agente = db.Column(db.String(200))
    idioma = db.Column(db.String(50))
    plataforma = db.Column(db.String(100))
    resolucion = db.Column(db.String(50))
    userId = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"fechaHora": self.fechaHora,
                "timezone": self.timezone,
                "podHostname": self.podHostname,
                "agente": self.agente,
                "idioma": self.idioma,
                "plataforma": self.plataforma,
                "resolucion": self.resolucion,
                "userId": self.userId}

@app.route('/send', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(fechaHora=data['fechaHora'],
                    timezone=data['timezone'],
                    agente=data['agente'],
                    idioma=data['idioma'],
                    plataforma=data['plataforma'],
                    resolucion=data['resolucion'],
                    userId=data['userId'],
                    podHostname=data['podHostname'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@app.route('/get', methods=['GET'])
def get_items():
    items = Item.query.order_by(Item.id.desc()).limit(5).all()
    items_list = [item.to_dict() for item in items]
    return jsonify(items_list), 200

if __name__ == '__main__':
    with app.app_context():
        print("intento 1 de crear base")
        db.create_all()  # Crea las tablas en la base de datos si no existen
    with app.app_context():
        print("intento 2 de crear base")
        db.create_all()  # Crea las tablas en la base de datos si no existen
    print("Corro la app")
    app.run(host='0.0.0.0',port=5000,debug=True)
