from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///catalog_database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user1 = User(name="zeshan", email="shaikhzeshan@gmail.com",picture="")
session.add(user1)
session.commit()

# Create category #1 and add items to the category
category1 = Category(name="Electronic", user_id=1)
session.add(category1)
session.commit()

item1 = Item(user_id=1, name='Lenovo yoga 360',
                     description="The definition of versatility, this ultralight 2-in-1 adapts to your business with 4 flexible modes to work, present, create, and connect. Features a stunning display with intense color and deep contrast. Even a dockable, rechargeable stylus pen. Plus, the fastest, advanced mobile broadband technology available.",
                     category=category1)
session.add(item1)
session.commit()

# Create category #2 and add items to the category
category2 = Category(name="Sport", user_id=1)
session.add(category2)
session.commit()

item2 = Item(user_id = 1, name = "Soccar",
                     description ="Developed with a durable TPU cover and vibrant panel details for quality visibility on the field, the Nike\
                     Pitch Soccer Ball is made to handle the rigors \
                     of intense practice drills and ready yourself for official match play.",
                     category=category2)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Cricket",
             description="great starter kit for your young cricketer, the Gun\
                n and  Moore Youth Six Cricket Set comes complete with a bat, ball, b\
                ail, stumps, and a set of gloves to lay down\
                the games core fundamentals\
                and help them build their skills.",
             category=category2)
session.add(item3)
session.commit()

# Create category #3 and add items to the category
category3 = Category(name="fashion", user_id=1)
session.add(category3)
session.commit()

item4 = Item(user_id=1, name="Men Jeans Diesel",
             description="Whiskering at the upper thighs provides subtle texture\
             to the front of bootcut jeans crafted from clean, dark-dyed indigo denim.",
             category=category3)
session.add(item4)
session.commit()

# Create category #4 and add items to the category
category4 = Category(name="House Hold Electronic", user_id=1)
session.add(category4)
session.commit()

item5 = Item(user_id=1, name="MicroWave",
             description="1.4 cu. ft. Countertop Microwave with Sensor Cook Technology in Stainless Steel",
             category=category4)
session.add(item5)
session.commit()

