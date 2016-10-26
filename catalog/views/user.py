from catalog.models.database_setup import User
from catalog.views import session


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


def getUserInfo(user_id):
    print "***getUserInfo user_id: {}".format(user_id)
    try:
        user = session.query(User).filter_by(id=user_id).one()
        return user
    except:
        return None


def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(
        email=login_session['email']).one()

    return user.id
