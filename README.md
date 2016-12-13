# RestaurantCatalog -- in development
### Flask web app with 3rd party authentication, local permission system, object relational mapping, and REST API endpoints.
#### Contents:
<ul>
<li>project.py executes the web app.
<li>catalog/models/ contains code for creating and populating a SQL database using SQLAlchemy ORM.
<li>catalog/views/ contains handlers and REST API endpoints.
<li>catalog/templates/ contains html rendered with jinja2
<li>catalog/static/ contains css and images. 
</ul>

####To run the local developer version, the vagrant machine for Udacity's Full Stack Web Development Course must be installed. After starting up and logging into the vagrant machine, open the github project folder and run:
```
> python project.py
```
Then from a browser visit the base URL http://localhost:5000/

####REST API endpoints are accessible from the base URL through the following paths:
<ul>
<li> /restaurants/JSON
<li> /restaurants/[ID-OF-RESTAURANT]/menu/JSON
<li> /restaurants/[ID-OF-RESTAURANT]/menu/[ID-OF-ITEM]/JSON
</ul>

####Visit the live application at https://secret-crag-37115.herokuapp.com
