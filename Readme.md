# Blog-web-app

A blog web app that allows users to create an account, log in, post blogs, and see blogs posted by others.  This is a project in progress and is intended as a portfolio web app.

## Status
Core models and views in place, authentication and UI functional. 


## Built With
- Python 3.12
- Django 5.2
- PostgreSQL, SQLite
- Bootstrap CSS


## Current Progress
- Models: Projects, BlogPost, UserProfile -- implemented
- Admin: basic admin configured -- implemented
- Auth: registration + login -- implemented
- UI: prototype templates -- partial
- Account Settings: password reset, email verification, profile updates -- minimal
- Tests: unit tests for models -- minimal


## Getting Started
Prerequisites
```
pip install .
```

Database
```
python manage.py migrate
```

Create superuser
```
python manage.py createsuperuser
```

Run
```
python manage.py runserver
```


## Roadmap
Priority orders and checkpoints
- [x] Core models (Projects, BlogPost, UserProfile)
- [x] Admin + basic CRUD
- [x] Responsive frontend templates and layout polish
- [ ] Email integration
- [ ] Blog: rich text editor, comments, pagination
- [ ] User profiles edit UI


## Credits
Thanks to Corey Schafer for the [full feature Django web app tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU).
