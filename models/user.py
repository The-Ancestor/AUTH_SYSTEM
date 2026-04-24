from db.database import db
from datetime import datetime, timedelta

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())


class RefreshToken(db.Model):
    __tablename__ = "refresh_tokens"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False)
    revoked = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    expires_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
