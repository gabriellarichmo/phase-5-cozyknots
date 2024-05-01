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
from models.category import Category
from config import app, db

def seed_cat():
    categories = [
        {"name": "Knit", "description": "Knitting patterns"},
        {"name": "Crochet", "description": "Crochet patterns"},
        {"name": "Sweaters", "description": "Crochet sweater patterns"},
        {"name": "Sweaters", "description": "Knit sweater patterns"},
        {"name": "Mittens", "description": "Crochet mitten patterns"},
        {"name": "Mittens", "description": "Knit mitten patterns"},
        {"name": "Hats", "description": "Knit hat patterns"},
        {"name": "Hats", "description": "Crochet hat patterns"},
        {"name": "Socks", "description": "Crochet sock patterns"},
        {"name": "Socks", "description": "Knit sock patterns"},
        {"name": "Scarves", "description": "Crochet scarf patterns"},
        {"name": "Scarves", "description": "Knit scarf patterns"},
        {"name": "Amigurumi", "description": "Crochet amigurumi patterns"},
    ]
    for cat_data in categories:
        category = Category.query.filter_by(name=cat_data["name"]).first()
        if not category:
            category = Category(**cat_data)
            db.session.add(category)
    db.session.commit()

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        Purchase.query.delete()
        User.query.delete()
        Category.query.delete()
        Pattern.query.delete()

        seed_cat()
        categories = Category.query.all()
        
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
            price = round(random.uniform(0, 10), 2)
            author = fake.name()
            difficulty = fake.random_element(elements=("Beginner", "Intermediate", "Advanced"))
            category = random.choice(categories)
            pattern = Pattern(
                title=title,
                description=description,
                price=price,
                author=author,
                difficulty=difficulty,
                category_id=category.id
            )
            print(f"Adding pattern: {title}, {description}")
            db.session.add(pattern) 
            
        db.session.commit()
            
    print("Finished seeding...")
            # Seed code goes here!
