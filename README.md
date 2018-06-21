# udacityCatalogProject
This is a simple catalog app built with Python, Flask and SQLAlchemy. The app supports user authentication and authorization using OAuth 2.0 and Facebook Login API. Logged in users can add categories and items, as well as edit, delete categories and items that they have created. Users who are not logged in can view the contents of the catalog but cannot make changes.


HOW TO RUN To run the web application:

install git for better control of code  from https://git-scm.com/downloads

#Install Vagrant https://www.vagrantup.com/ and Virtual Box https://www.virtualbox.org

#Clone this repository git clone http://github.com//fullstack-nanodegree-vm fullstack

Launch the Vagrant VM (by typing vagrant up in the directory then vagrant ssh then cd /vagrant then cd catalog).

From directory catalog, initialize the application database by typing python database_setup.py follows by python fake.py.

From directory fullstack/vagrant/catalog, run the application within the VM by typing python project.py into the Terminal.

Access the application by visiting http://localhost:5000 locally on your favourite browser
