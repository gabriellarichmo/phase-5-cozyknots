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
        {"name": "Sweaters", "description": "Sweater patterns"},
        {"name": "Mittens", "description": "Mitten patterns"},
        {"name": "Hats", "description": "Hat patterns"},
        {"name": "Socks", "description": "Sock patterns"},
        {"name": "Scarves", "description": "Scarf patterns"},
        {"name": "Amigurumi", "description": "Amigurumi patterns"},
        {"name": "Other", "description": "Miscellaneous patterns"},
    ]
    for cat_data in categories:
        category = Category.query.filter_by(name=cat_data["name"], description=cat_data["description"]).first()
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

        category_sweaters = Category.query.filter_by(name="Sweaters", description="Sweater patterns").first()
        if not category_sweaters:
            category_sweaters = Category(name="Sweaters", description="Sweater patterns")
            db.session.add(category_sweaters)
            db.session.commit()

        category_mittens = Category.query.filter_by(name="Mittens", description="Mitten patterns").first()
        if not category_mittens:
            category_mittens = Category(name="Mittens", description="Mitten patterns")
            db.session.add(category_mittens)
            db.session.commit()

        category_hats = Category.query.filter_by(name="Hats", description="Hat patterns").first()
        if not category_hats:
            category_hats = Category(name="Hats", description="Hat patterns")
            db.session.add(category_hats)
            db.session.commit()

        category_socks = Category.query.filter_by(name="Socks", description="Sock patterns").first()
        if not category_socks:
            category_socks = Category(name="Socks", description="Sock patterns")
            db.session.add(category_socks)
            db.session.commit()

        category_scarves = Category.query.filter_by(name="Scarves", description="Scarf patterns").first()
        if not category_scarves:
            category_scarves = Category(name="Scarves", description="Scarf patterns")
            db.session.add(category_scarves)
            db.session.commit()

        category_amigurumi = Category.query.filter_by(name="Amigurumi", description="Amigurumi patterns").first()
        if not category_amigurumi:
            category_amigurumi = Category(name="Amigurumi", description="Amigurumi patterns")
            db.session.add(category_amigurumi)
            db.session.commit()

        category_other = Category.query.filter_by(name="Other", description="Miscellaneous patterns").first()
        if not category_other:
            category_other = Category(name="Other", description="Miscellaneous patterns")
            db.session.add(category_other)
            db.session.commit()
        
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

        p1 = Pattern(
            title="Oh Scrap!",
            description="This crochet pattern is a fun way to use up your stash of scrap yarn! Depending on how much scrap yarn you have, you can make a tote bag, dinner placemat, or even a blanket! Let your creativity be the diamond in the scrap!",
            price=0.99,
            author=fake.name(),
            image="oh_scrap.JPEG",
            difficulty="Beginner",
            type="Crochet",
            category_id=Category.query.filter_by(name="Other").first().id
        )
        p2 = Pattern(
            title="Raglan Sweater",
            description="Knit your first raglan with this beginner friendly knit pattern. Using super bulky yarn and 15 mm needles, this is a quick way to stay warm and cozy all winter. Even your furry friends will be wanting one of their own!",
            price=2.75,
            author=fake.name(),
            image="raglan.JPEG",
            difficulty="Beginner",
            type="Knit",
            category_id=Category.query.filter_by(name="Sweaters", description="Sweater patterns").first().id
        )
        p3 = Pattern(
            title="Bubble Cardigan",
            description="Crochet bubble cardigan design. Pattern includes how to add button holes and offers different sizing based on preference or need.",
            price=4.99,
            author=fake.name(),
            image="bubble_cardi.JPEG",
            difficulty="Intermediate",
            type="Crochet",
            category_id=Category.query.filter_by(name="Sweaters", description="Sweater patterns").first().id
        )
        p4 = Pattern(
            title="Mushroom Keychain",
            description="Crochet pattern for this fun mushroom keychain that is also a secret holder for your tube of lip balm or even a lighter! The straps are adjustable and you can attach this keychain to your bag, belt loops, and more!",
            price=0.99,
            author=fake.name(),
            image="mush_keychain.JPEG",
            difficulty="Beginner",
            type="Crochet",
            category_id=Category.query.filter_by(name="Other").first().id
        )
        patterns = [p1, p2, p3, p4]
        db.session.add_all(patterns)
        db.session.commit()


        # for _ in range(10):
        #     title = fake.text(max_nb_chars=50)
        #     description = fake.text(max_nb_chars=250)
        #     price = round(random.uniform(0, 10), 2)
        #     author = fake.name()
        #     difficulty = fake.random_element(elements=("Beginner", "Intermediate", "Advanced"))
        #     category = random.choice(categories)
        #     pattern = Pattern(
        #         title=title,
        #         description=description,
        #         price=price,
        #         author=author,
        #         difficulty=difficulty,
        #         category_id=category.id
        #     )
        #     print(f"Adding pattern: {title}, {description}")
        #     db.session.add(pattern) 
            
        # db.session.commit()
            
    print("Finished seeding...")
            # Seed code goes here!
