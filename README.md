# RestaurantCatalog
### Flask web app with 3rd party authentication, local permission system, and object relational mapping styled with Bootstrap.
#### Contents:
<ul>
<li>runserver.py executes the web app.
<li>catalog/models/ contains code for creating and populating a SQLite database using SQLAlchemy ORM.
<li>catalog/views/ contains handlers and REST API endpoints.
<li>catalog/templates/ contains html rendered with jinja2
<li>catalog/static/ contains css and images. 
</ul>
#### To run the web app in developer mode, Flask and SQLAlchemy must be installed. Then from the command line run:
```
> python runserver.py
```
Then use a browser to visit http://localhost:5000/restaurants
