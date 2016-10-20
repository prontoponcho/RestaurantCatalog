from catalog import app
from flask import flash, redirect, render_template, \
                  request, url_for
from catalog.views import session
from catalog.models.database_setup import Restaurant

category_order = ['American',
                  'Chinese',
                  'Indian',
                  'International',
                  'Italian',
                  'Mexican',
                  'Vegetarian']


@app.route('/')
@app.route('/restaurants/')
def restaurants():
    restaurants = session.query(Restaurant).order_by(Restaurant.name).all()

    print "***LENGTH OF RESTAURANTS: {}".format(len(restaurants))

    if len(restaurants) == 0:
        restaurants = None

    return render_template('restaurants.html', restaurants=restaurants)


@app.route('/restaurants/by-category')
def restaurantsByCategory():
    restaurants = session.query(Restaurant).all()
    restaurants_by_category = None

    if len(restaurants) != 0:
        restaurants_by_category = {category: [] for category in category_order}

    for r in restaurants:
        restaurants_by_category[r.category].append(r)

    return render_template('restaurants-by-category.html',
                           category_order=category_order,
                           restaurants_by_category=restaurants_by_category)


@app.route('/restaurants/add/',
           methods=['GET', 'POST'])
def addRestaurant():
    if request.method == 'POST':
        submit = request.form['submit']
        if submit == 'create':
            newRestaurant = Restaurant(name=request.form['name'],
                                       category=request.form['category'])
            session.add(newRestaurant)
            session.commit()

            flash("New Restaurant Created")

        return redirect(url_for('restaurants'))

    else:
        return render_template('add-restaurant.html',
                               category_order=category_order)


@app.route('/restaurants/<int:restaurant_id>/edit/',
           methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()

    if request.method == 'POST':
        submit = request.form['submit']
        if submit == 'edit':
            restaurant.name = request.form['name']
            restaurant.category = request.form['category']
            session.add(restaurant)
            session.commit()

            flash("Restaurant Successfully Edited")

        return redirect(url_for('restaurants'))

    else:
        return render_template('edit-restaurant.html',
                               restaurant=restaurant,
                               category_order=category_order)


@app.route('/restaurants/<int:restaurant_id>/delete/',
           methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        submit = request.form['submit']
        if submit == 'delete':
            session.delete(restaurant)
            session.commit()

            flash("Restaurant Successfully Delete")

        return redirect(url_for('restaurants'))

    else:
        return render_template('delete-restaurant.html', restaurant=restaurant)
