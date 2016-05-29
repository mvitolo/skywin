# Sky Win App - Server side


Web bot: https://skywin.herokuapp.com/polls/


Telegram bot: https://web.telegram.org/#/im?p=@SkyWinBot


API: https://skywin.herokuapp.com/api/


Admin: https://skywin.herokuapp.com/admin/


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


## API


```
https://skywin.herokuapp.com/api/
```
    
Example:

```
https://skywin.herokuapp.com/api/matches/?format=json
```


## Setup data

To get a token create a Telegram bot https://core.telegram.org/bots.

Go to admin and create:

 - Bot (token is the only required field)
 
 - Questions
 
 - Choices

Remember to configure the SITE_ID in settings.


