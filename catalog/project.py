from flask import Flask, render_template, url_for , request, redirect

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)





engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine



DBSession = sessionmaker(bind=engine)

session = DBSession()





@app.route('/')

@app.route('/restaurant/<int:restaurant_id>/')

def restaurantMenu(restaurant_id):

    rest = session.query(Restaurant).filter_by(id=restaurant_id).one()

    item = session.query(MenuItem).filter_by(restaurant_id=rest.id)

    return render_template("menu.html",restaurant_id = rest.id)


@app.route("/restaurant/new/<int:restaurant_id>/, methods =['GET','POST'])
def newMenuItem(restaurant_id):
           if request.method='POST':
                newItem=MenuItem(name=request.form['name'],restaurant_id = restaurant_id)
                session.add(newItem)
                session.commit()
                return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
           else:
                return render_for('newMenuItem',restaurant_id = restaurant_id)

    return "page to create a new menu item. Task 1 complete!"



# Task 2: Create route for editMenuItem function here




@app.route("/restaurant/edit/<int:restaurant_id>/<int:menu_id>/")

def editMenuItem(restaurant_id, menu_id):

    return "page to edit a menu item. Task 2 complete!"



# Task 3: Create a route for deleteMenuItem function here




@app.route("/restaurant/delete/<int:restaurant_id>/<int:menu_id>/")
def deleteMenuItem(restaurant_id, menu_id):

    return "page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':

    app.debug = True

    app.run(host='0.0.0.0', port=5000)