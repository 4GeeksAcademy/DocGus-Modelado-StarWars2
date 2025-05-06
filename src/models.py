from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    apellido: Mapped[str] = mapped_column(String(120), nullable=False)
    fecha_subscripcion: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow)
    
    favorites = relationship('Favorite', backref='user', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha_subscripcion": self.fecha_subscripcion.isoformat()
        }

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    especie: Mapped[str] = mapped_column(String(120), nullable=True)
    planeta_natal: Mapped[str] = mapped_column(String(120), nullable=True)
    descripcion: Mapped[str] = mapped_column(String(250), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "especie": self.especie,
            "planeta_natal": self.planeta_natal,
            "descripcion": self.descripcion,
        }

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    clima: Mapped[str] = mapped_column(String(120), nullable=True)
    terreno: Mapped[str] = mapped_column(String(120), nullable=True)
    poblacion: Mapped[str] = mapped_column(String(120), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "terreno": self.terreno,
            "poblacion": self.poblacion,
        }

class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey('planet.id'), nullable=True)
    character_id: Mapped[int] = mapped_column(ForeignKey('character.id'), nullable=True)

    planet = relationship('Planet', backref='favorites', lazy=True)
    character = relationship('Character', backref='favorites', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id,
        }