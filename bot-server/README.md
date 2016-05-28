# Sky Win App - Server side

## Heroku

Deploy on Heroku (NB: pay attention to subfolder!!)

```
git subtree push --prefix bot-server/ heroku master
```

### Database
If this was your first deploy we need to set up the db. Heroku allows to run commands through its toolbelt `run` command.

1. (Optional) Syncdb

    ```
    heroku run python manage.py syncdb
    ```
    

2. Migrate
    
    ```
    heroku run python manage.py migrate
    ```
    


3. (Optional) Create additional super user
    
    ```
    heroku run python manage.py createsuperuser
    ```
