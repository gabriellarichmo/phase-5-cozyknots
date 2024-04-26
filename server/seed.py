#!/usr/bin/env python3

# Standard library imports
import random
from random import randint


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
        
        for _ in range(10): 
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
            
        for _ in range(10):
            title = fake.text(max_nb_chars=50)
            description = fake.text(max_nb_chars=250)
            # price = randint(1, 10)
            price = round(random.uniform(0, 10), 2)
            author = fake.name()
            difficulty = fake.random_element(elements=("Beginner", "Intermediate", "Advanced"))
            pattern = Pattern(
                title=title,
                description=description,
                price=price,
                author=author,
                difficulty=difficulty,
            )
            print(f"Adding pattern: {title}, {description}")
            db.session.add(pattern) 
            
        db.session.commit()
            
            
    print("Finished seeding...")
            # Seed code goes here!
