from catalog import app
from catalog.views import session
from catalog.models.database_setup import Restaurant, MenuItem
from catalog.views.user import getUserInfo

from flask import flash, redirect, render_template, \
                  request, url_for
from flask import session as login_session

course_order = ['Appetizer',
                'Entree',
                'Beverage',
                'Dessert']


@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def viewMenu(restaurant_id, alert_type=None):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)

    items_by_course = {course: [] for course in course_order}
    num_items = 0
    for i in items:
        items_by_course[i.course].append(i)
        num_items += 1

    # Check if user created the restaurant.
    # If true, return fully editable menu, else return public menu.
    if restaurant.user_id == login_session.get('user_id'):
        return render_template('menu.html',
                               num_items=num_items,
                               restaurant=restaurant,
                               alert_type=request.args.get('alert_type'),
                               course_order=course_order,
                               items_by_course=items_by_course)
    else:
        return render_template('menu-public.html',
                               user=getUserInfo(login_session.get('user_id')),
                               num_items=num_items,
                               restaurant=restaurant,
                               alert_type=request.args.get('alert_type'),
                               course_order=course_order,
                               items_by_course=items_by_course)


@app.route('/restaurants/<int:restaurant_id>/menu/add/',
           methods=['GET', 'POST'])
def addMenuItem(restaurant_id):

    if 'username' not in login_session:
        flash("Log in to add menu items")
        return redirect(url_for('viewMenu',
                                restaurant_id=restaurant_id,
                                alert_type='alert-warning'))

    if request.method == 'POST':
        submit = request.form['submit']
        if submit == 'create':
            newItem = MenuItem(name=request.form['name'],
                               description=request.form['description'],
                               price=request.form['price'],
                               course=request.form['course'],
                               restaurant_id=restaurant_id,
                               user_id=login_session.get('user_id'))
            session.add(newItem)
            session.commit()
            flash("Menu Item Created")

        return redirect(url_for('viewMenu',
                                restaurant_id=restaurant_id,
                                alert_type="alert-success"))

    else:
        restaurant = session.query(Restaurant).\
                             filter_by(id=restaurant_id).one()
        return render_template('add-menu-item.html', restaurant=restaurant)


@app.route('/restaurants/<int:restaurant_id>/menu/<int:item_id>/edit/',
           methods=['GET', 'POST'])
def editMenuItem(restaurant_id, item_id):

    if 'username' not in login_session:
        flash("Log in to edit menu items")
        return redirect(url_for('viewMenu',
                                restaurant_id=restaurant_id,
                                alert_type='alert-warning'))

    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menuItem = session.query(MenuItem).filter_by(id=item_id).one()

    if menuItem.user_id != login_session.get('user_id'):
        flash("You cannot edit menu items created by other users.")
        return redirect(url_for('viewMenu',
                                restaurant_id=restaurant_id,
                                alert_type='alert-warning'))

    if request.method == 'POST':
        submit = request.form['submit']
        if submit == 'edit':
            menuItem.name = request.form['name']
            menuItem.description = request.form['description']
            menuItem.price = request.form['price']
            menuItem.course = request.form['course']
            session.add(menuItem)
            session.commit()

            flash("Menu Item Sucessfully Edited")

            return redirect(url_for('viewMenu',
                                    restaurant_id=restaurant_id,
                                    alert_type='alert-success'))
        else:
            return redirect(url_for('viewMenu',
                                    restaurant_id=restaurant_id,))

    else:
        return render_template('edit-menu-item.html',
                               restaurant=restaurant,
                               item=menuItem)


@app.route('/restaurants/<int:restaurant_id>/menu/<int:item_id>/delete/',
           methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, item_id):

    if 'username' not in login_session:
        flash("Log in to delete menu items.")
        return redirect(url_for('viewMenu',
                                restaurant_id=restaurant_id,
                                alert_type='alert-warning'))

    menuItem = session.query(MenuItem).filter_by(id=item_id).one()

    if menuItem.user_id != login_session.get('user_id'):
        flash("You cannot delete menu items created by other users.")
        return redirect(url_for('viewMenu',
                                restaurant_id=restaurant_id,
                                alert_type='alert-warning'))

    if request.method == 'POST':
        submit = request.form['submit']
        if submit == 'delete':
            session.delete(menuItem)
            session.commit()

            flash("Menu Item Successfully Deleted")

            return redirect(url_for('viewMenu',
                                    restaurant_id=restaurant_id,
                                    alert_type='alert-success'))
        else:
            redirect(url_for('viewMenu',
                             restaurant_id=restaurant_id))

    else:
        return render_template('delete-menu-item.html', item=menuItem)
