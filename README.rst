
===========================================================
Udacity Full Stack Web Developer - Project 4 - Item Catalog
===========================================================
I developed this project using Python 3.6, Pipenv, and Pycharm 2018.2.4 on Ubuntu 18.04 LTS.

I based this project on the Movie Trailer project, which was the first project in this nanodegree.

Design - Front End
==================
I created the web pages using Bootstrap 4.1.

Design - Back End
=================
The example code provided by Udacity is outdated, convoluted, and not PEP8 compliant. I decided to use my previous Java development experience to create a better Python application than the Udacity example. I researched how to implement functionality in a `Flask <http://flask.pocoo.org/>`_ application and decided to use `Flask-Dance <https://github.com/singingwolfboy/flask-dance>`_, `Flask-Login <https://flask-login.readthedocs.io/en/latest/>`_, and `Flask-SQLAlchemy <http://flask-sqlalchemy.pocoo.org/>`_. I used the following YouTube tutorials as reference:

* `PrettyPrinted <https://prettyprinted.com/>`_
* `The Flask Mega-Tutorial <https://blog.miguelgrinberg.com/index>`_
* `RealPython <https://realpython.com/>`_

Using both Flask-Dance and Flask-Login provides third-party authentication and login session management.

Based on my experience with Java's `Hibernate <http://hibernate.org/>`_ ORM, I looked for an ORM that was more robust than SQLAlchemy. I decided to use Flask-SQLAlchemy, because I didn't need to do multiple queries or write a view to retrieve a Movie and its associated Category.

Future iterations of this project will include proper error handling, logging, and unit tests.

This README file is in RST format for two reasons: 1) I know rST markup because I'm the Docs PTL for Acumos, an Open Source project under the Linux Foundation's Deep Learning umbrella; and 2) rST is a much better choice if the goal is to publish documentation on `ReadTheDocs <https://readthedocs.org/>`_.

Object Model
------------
There are four objects, which equates to four database tables. All inherit from flask_sqlalchemy.SQLAlchemy.Model. See the `docs <http://flask-sqlalchemy.pocoo.org/2.3/models/>`_ for more on creating object models.

* User - basic user info; also extends `flask_login.UserMixin <https://flask-login.readthedocs.io/en/latest/_modules/flask_login/mixins.html#UserMixin>`_
* OAuth - provider info; extends flask_dance.consumer.backend.sqla.OAuthConsumerMixin
* Catagory - name, id
* Movie - id, title, description, poster URL, trailer URL

Project Structure
=================

    .. image:: docs/project-dir.png
       :width: 75%

* Python files

    * ``application.py`` - the main file
    * ``movie_data.py`` - populates the database

* Templates (HTML)

    * ``layout.html`` - file that lays out the structure of the web pages
    * ``index.html`` - the Home page file
    * ``item_view.html`` - view Movie details
    * ``item_edit.html`` - add and update movies
    * ``item_delete.html`` - delete a movie

* Misc

    * ``catalog.db`` - SQLite database
    * ``client_secret.json`` file that contains client id and secret for Github oauth
    * ``Pipfile`` - file used by pipenv to create the virtual environment needed to run the application

Third-Party Authentication
==========================
I decided to use Flask-Dance with Github, since Github seems to be the least complicated of the providers that Flask-Dance supports. Follow the Flask-Dance `instructions <https://flask-dance.readthedocs.io/en/latest/quickstarts/github.html>`_ for setting up your application for Github authentication.

Note that Github requires HTTPS, so for development you will need to ``export OAUTHLIB_INSECURE_TRANSPORT=1`` or modify your IDE's RUN configuration.

**Example Run Configuration From PyCharm**

    .. image:: docs/pycharm.png
       :width: 75%

Installation
============

Prerequisites
-------------
* Python 3.6
*  `pipenv <https://pipenv.readthedocs.io/>`_


Install and Run
---------------

    .. image:: docs/install-and-run.png

1. Clone the repo using anonymous HTTPS

    .. code-block:: bash

        $ git clone https://github.com/aimeeu/udacity_fsnd_proj4_item_catalog.git

2. ``cd`` to the u* directory to create a virtual environment and install the application's dependencies

     .. code-block:: bash

        $ cd u*
        $ pipenv install

3. Create and load the database; a default user ("admin") is created with no OAuth data; the admin user is the User who is associated with the supplied Category and Movie records

    .. code-block:: bash

        $ pipenv run python application.py --setup

    Records created:

    .. image:: docs/database-records.png
       :width: 75%


4. Update the client_secret.json file with the Client ID and Client Secret values from Github

    .. image:: docs/github-secrets.png
       :width: 75%

5. Because this is a dev environment **without** certificates and Github expects HTTPS, export the Flask-Dance OAUTHLIB_INSECURE_TRANSPORT=1 environment variable to enable running without HTTPS

    .. code-block:: bash

        $ export OAUTHLIB_INSECURE_TRANSPORT=1

6. Run the application

    .. code-block:: bash

        $ pipenv run python application.py

Open your browser and access ``http://localhost:5000``.

Test Required Functionality
===========================
    .. note::

        The images contain records I created while testing

Unauthenticated Users
---------------------
Unauthenticated users may access the Home and View Details pages.

    .. image:: docs/home-notLoggedIn.png
       :width: 75%

1. Click **Github Log In** to authenticate via GitHub
2. Click **Movies JSON** to view all the movies in JSON format

    .. image:: docs/movies-json.png
       :width: 75%

**View Movie Details - User Not Authenticated**

    .. image:: docs/movie-detailsNotLoggedIn.png
       :width: 75%

Authenticated Users
-------------------

Logging In - Github Auth
------------------------
Clicking **Github Log In** redirects the user to the Github oauth page.

    .. image:: docs/github-auth.png
       :width: 75%

Click **authorize** to authenticate via Github. The application then processes the authentication, creates User and OAuth records if they don't exist, and logs the user into the app.

Home Page View - User Authenticated
...................................

    .. image:: docs/home-loggedIn.png
       :width: 75%

1. Username is displayed
2. Log Out link displayed
3. Categories: all categories are listed; clicking a category link displays the movies for that category
4. Selecting **All Categories Recent Movies** loads the 10 most recently modified movies on the right; the column header changes to display the selected category
5. **Click the movie's title** to view details
6. Click **Edit** to edit the movie's details; **note**: only visible if the authenticated user is the person who created the movie record
7. Click **Delete** to edit the movie's details; **note**: only visible if the authenticated user is the person who created the movie record
8. Click **Add Movie** to add a new movie; **note**: only visible if the user is authenticated
9. Click **Home** to return to the Home page
10. Click **Movies JSON** to display a JSON list of all movies in the database; opens in a new tab

**View of Action Movies:**

    .. image:: docs/home-actionMovies.png
       :width: 75%

View Movie Details
..................

    .. image:: docs/movie-viewDetails.png
       :width: 75%

1. Click **Trailer** to open a new tab and watch the trailer
2. Click **Edit** to edit details; click **Delete** to delete the movie; both **Edit** and **Delete** redirect to new pages; **note**: **Edit** and **Delete** are only visible to an authenticated user who is also the creator of the movie record
3. Click **JSON** to open a new tab that displays the movie data in JSON format

    .. image:: docs/movie-json.png
       :width: 75%

Edit Movie Details
..................

    .. image:: docs/movie-edit.png
       :width: 75%

All fields are required, as specified by ``required="true"`` in the form fields. Click the **Submit** button to save changes.

**Security risk**: no fields are sanitized before being added to the database, which leaves this application open to scripting attacks.

**Field validation**: neither URL field is validated at this time; in future, use RFC3987 and Regex libraries for this

    .. image:: docs/movie-updatedMsg.png
       :width: 75%

After submitting the form, you return to the Home page, where a success message is displayed.

Add Movie
.........
Click **Add Movie** on the top menu bar.

    .. image:: docs/movie-add.png
       :width: 75%

All fields are required, as specified by ``required="true"`` in the form fields. Click the **Submit** button to save changes.

    .. image:: docs/movie-addMsg.png
       :width: 75%

After submitting the form, you return to the Home page, where a success message is displayed.

Delete Movie
............
Select **Delete** from either the Home page or View Movie page.

    .. image:: docs/movie-delete.png
       :width: 75%


Press **Delete** on the confirmation page. You then return to the Home page.


    .. image:: docs/movie-deleteMsg.png
       :width: 75%
