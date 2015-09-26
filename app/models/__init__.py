from sqlalchemy import func

from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

    created_at = db.Column(db.DateTime(timezone=False), default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=False), default=func.now(), onupdate=func.now(), nullable=False)
