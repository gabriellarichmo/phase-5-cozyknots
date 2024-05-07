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

        category_sweaters_crochet = Category.query.filter_by(name="Sweaters", description="Crochet sweater patterns").first()
        if not category_sweaters_crochet:
            category_sweaters_crochet = Category(name="Sweaters", description="Crochet sweater patterns")
            db.session.add(category_sweaters_crochet)
            db.session.commit()

        category_sweaters_knit = Category.query.filter_by(name="Sweaters", description="Knit sweater patterns").first()
        if not category_sweaters_knit:
            category_sweaters_knit = Category(name="Sweaters", description="Knit sweater patterns")
            db.session.add(category_sweaters_knit)
            db.session.commit()

        category_mittens_crochet = Category.query.filter_by(name="Mittens", description="Crochet mitten patterns").first()
        if not category_mittens_crochet:
            category_mittens_crochet = Category(name="Mittens", description="Crochet mitten patterns")
            db.session.add(category_mittens_crochet)
            db.session.commit()

        category_mittens_knit = Category.query.filter_by(name="Mittens", description="Knit mitten patterns").first()
        if not category_mittens_knit:
            category_mittens_knit = Category(name="Mittens", description="Knit mitten patterns")
            db.session.add(category_mittens_knit)
            db.session.commit()

        category_hats_knit = Category.query.filter_by(name="Hats", description="Knit hat patterns").first()
        if not category_hats_knit:
            category_hats_knit = Category(name="Hats", description="Knit hat patterns")
            db.session.add(category_hats_knit)
            db.session.commit()

        category_hats_crochet = Category.query.filter_by(name="Hats", description="Crochet hat patterns").first()
        if not category_hats_crochet:
            category_hats_crochet = Category(name="Hats", description="Crochet hat patterns")
            db.session.add(category_hats_crochet)
            db.session.commit()

        category_socks_crochet = Category.query.filter_by(name="Socks", description="Crochet sock patterns").first()
        if not category_socks_crochet:
            category_socks_crochet = Category(name="Socks", description="Crochet sock patterns")
            db.session.add(category_socks_crochet)
            db.session.commit()

        category_socks_knit = Category.query.filter_by(name="Socks", description="Knit sock patterns").first()
        if not category_socks_knit:
            category_socks_knit = Category(name="Socks", description="Knit sock patterns")
            db.session.add(category_socks_knit)
            db.session.commit()

        category_scarves_crochet = Category.query.filter_by(name="Scarves", description="Crochet scarf patterns").first()
        if not category_scarves_crochet:
            category_scarves_crochet = Category(name="Scarves", description="Crochet scarf patterns")
            db.session.add(category_scarves_crochet)
            db.session.commit()

        category_scarves_knit = Category.query.filter_by(name="Scarves", description="Knit scarf patterns").first()
        if not category_scarves_knit:
            category_scarves_knit = Category(name="Scarves", description="Knit scarf patterns")
            db.session.add(category_scarves_knit)
            db.session.commit()

        category_amigurumi = Category.query.filter_by(name="Amigurumi", description="Crochet amigurumi patterns").first()
        if not category_amigurumi:
            category_amigurumi = Category(name="Amigurumi", description="Crochet amigurumi patterns")
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
            category_id=Category.query.filter_by(name="Sweaters", description="Knit sweater patterns").first().id
        )
        p3 = Pattern(
            title="Bubble Cardigan",
            description="Crochet bubble cardigan design. Pattern includes how to add button holes and offers different sizing based on preference or need.",
            price=4.99,
            author=fake.name(),
            image="bubble_cardi.JPEG",
            difficulty="Intermediate",
            type="Crochet",
            category_id=Category.query.filter_by(name="Sweaters", description="Crochet sweater patterns").first().id
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
