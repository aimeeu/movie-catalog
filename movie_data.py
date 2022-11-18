#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ===============LICENSE_START================================================
# Apache-2.0
# ============================================================================
# Copyright (C) 2018 Aimee Ukasick. All rights reserved.
# ============================================================================
# This software file is distributed by Aimee Ukasick
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END==================================================
"""
This file is used to populate the database for the app.
The three objects/tables are defined in application.py.
Tables are created by application.py.
A default "admin" user is created with no OAuth entry.
Categories and movies are created with the admin user.
"""

from application import Category, Movie, User


#  db.session from application
def load_data(session):
    """
    Calls create user
    Calls create categories
    Calls create movies
    Finally commits newly created objects to database
    """
    try:
        user1 = create_admin_user(session)
        categories = create_categories(session, user1)
        create_movies(session, user1, categories)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise e


def create_admin_user(session):
    """
    Creates a single "admin" user and adds it to the session
    :return: user
    """
    user1 = User(username='admin')
    session.add(user1)
    return user1


def create_categories(session, user1):
    """
    Creates multiple Category objects and adds them to the session
    :return: categories
    """
    drama = Category(name="Drama", user=user1)
    scifi = Category(name="Science Fiction", user=user1)
    action = Category(name="Action", user=user1)
    kids = Category(name="Kids", user=user1)
    horror = Category(name="Horror", user=user1)
    fantasy = Category(name="Fantasy", user=user1)
    comedy = Category(name="Comedy", user=user1)
    categories = dict()
    categories["drama"] = drama
    categories["scifi"] = scifi
    categories["action"] = action
    categories["kids"] = kids
    categories["horror"] = horror
    categories["fantasy"] = fantasy
    categories["comedy"] = comedy

    for cat in categories.values():
        session.add(cat)

    return categories


def create_movies(session, user1, categories):
    """
    Creates multiple Movie objects and adds them to the session
    """
    movies=[]

    movie1 = Movie(title="Toy Story",
                   description="A story of a boy and his toys that come to life",
                   poster_img_url="http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                   trailer_url="https://www.youtube.com/watch?v=4KPTXpQehio",
                   user=user1, category=categories["kids"])
    movies.append(movie1)

    movie2 = Movie(title="Avatar",
                   description="A marine on an alien planet infiltrates the local lifeforms",
                   poster_img_url="http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                   trailer_url="https://www.youtube.com/watch?v=d1_JBMrrYw8",
                   user=user1,  category=categories["action"])
    movies.append(movie2)

    movie3 = Movie(title="Ratatouille",
                   description="A rat is a chef in Paris",
                   poster_img_url="http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                   trailer_url="https://www.youtube.com/watch?v=1yKqLNnxGZw",
                   user=user1, category=categories["kids"])
    movies.append(movie3)

    movie4 = Movie(title="Midnight in Paris",
                   description="Going back in time to meet authors",
                   poster_img_url="http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                   trailer_url="https://www.youtube.com/watch?v=irLRpuUx3jk",
                   user=user1,  category=categories["drama"])
    movies.append(movie4)

    movie4 = Movie(title="Hunger Games",
                   description="Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
                   poster_img_url="http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                   trailer_url="https://www.youtube.com/watch?v=GWU-xLViib0",
                   user=user1, category=categories["action"])
    movies.append(movie4)

    movie5 = Movie(title="Incredibles 2",
                   description="Bob Parr (Mr. Incredible) is left to care for the kids while Helen (Elastigirl) is out saving the world",
                   poster_img_url="https://m.media-amazon.com/images/M/MV5BMTEzNzY0OTg0NTdeQTJeQWpwZ15BbWU4MDU3OTg3MjUz._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                   trailer_url="https://www.youtube.com/watch?v=ZJDMWVZta3M",
                   user=user1, category=categories["kids"])
    movies.append(movie5)

    movie6 = Movie(title="Stargate",
                   description="An interstellar teleportation device, found in Egypt, leads to a planet with humans resembling ancient Egyptians who worship the god Ra.",
                   poster_img_url="https://m.media-amazon.com/images/M/MV5BYWEyYTQzNzQtZTg5OS00NDhkLTg1NjYtMzA5Y2MyYjYzNWQ5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
                   trailer_url="https://www.youtube.com/watch?v=_mucMCddPy0",
                   user=user1, category=categories["scifi"])
    movies.append(movie6)

    movie7 = Movie(title="Requiem for a Dream",
                   description="The drug-induced utopias of four Coney Island people are shattered when their addictions run deep.",
                   poster_img_url="https://m.media-amazon.com/images/M/MV5BOTdiNzJlOWUtNWMwNS00NmFlLWI0YTEtZmI3YjIzZWUyY2Y3XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                   trailer_url="https://www.youtube.com/watch?v=0nU7dC9bIDg",
                   user=user1, category=categories["drama"])
    movies.append(movie7)

    for mov in movies:
        session.add(mov)

