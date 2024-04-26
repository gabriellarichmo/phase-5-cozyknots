#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker
from werkzeug.security import generate_password_hash
# Local imports
from app import app
from models.user import User
from models.pattern import Pattern
from models.purchase import Purchase
from config import app, db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        Purchase.query.delete()
        User.query.delete()
        Pattern.query.delete()
        
        for _ in range(10):  # You can adjust the number of users you want to seed
            username = fake.user_name()
            email = fake.email()
            user = User(
                username=username,
                email=email,
                name=fake.name(),
                avatar=fake.image_url(),
                bio=fake.text(max_nb_chars=250),
                _password_hash=generate_password_hash(fake.password()),  # Using generate_password_hash
            )
            print(f"Adding user: {username}, {email}")
            db.session.add(user)
            
        db.session.commit()
            
            
            
            
    print("Finished seeding...")
            # Seed code goes here!
