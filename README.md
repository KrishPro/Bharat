# Bharat (SilverFox)

It's a Blog Posting Site, Backed by Python (Django) \
**Note:** this project was written when i was 8-9yrs old. So, I may sound childish...at few places in this project.

# About
you can create account in the web app. you can post un-limited blogs from a account. 
you can change password of your account. you can search for posts in our site. you can contact us (responces are recorded in db). It's admin page is at `localhost:8000/admin`

**Technical**\
We've used sqlite as our DB, To store posts, user accounts and contact forms. This application is one of my fav. because I had never worked with DBs before it.
For Authentication, I've used Django's default Authentication.

# Were to look for the Code ?
 - [**HTML files**](/templates)
 - [**Static files like imgs, fonts**](/static)
 - **Python files** have thier own folder each page

# How to run ?
**Prerequest**
 - Mini-conda or Annaconda Setup
 - Yup, That's it

**Steps**\
In order to run this properly, Run the following CLI commands :
 - `conda create -n bharat python=3.9.5`
 - `conda activate bharat`
 - `pip install -r requirments.txt`
 - `python manage.py runserver`

Then go ahead, and browse `localhost:8000`
