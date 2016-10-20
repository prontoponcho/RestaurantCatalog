from catalog import app
from catalog.views import session
from catalog.models.database_setup import Restaurant, MenuItem
from flask import jsonify


@app.route('/restaurants/JSON')
def getRestaurants():
    restaurants = session.query(Restaurant).order_by(Restaurant.name).all()

    return jsonify(Restaurants=[r.serialize for r in restaurants])


@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def getMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()

    return jsonify(Restaurant=[restaurant.serialize])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:item_id>/JSON')
def getMenuItem(restaurant_id, item_id):
    menu_item = session.query(MenuItem).filter_by(id=item_id).one()

    return jsonify(MenuItem=[menu_item.serialize])
