# TFR API Task

This repository consist of an Rest API made by Django Rest Framework to search places through latitude and longitude values.

# Set up the environment

Navigate to the root of the application and install all dependencies.

```ruby
pip install -r requirements.txt
```

# Start the django app

```ruby
python manage.py runserver
```

# Swagger Documentation and testing the endpoints

You can easily test the endpoints from swagger ui. After starting the app, navigate to the link at your browser.

```ruby
http://127.0.0.1:8000/api/swagger/
```
This will end up with an api interface that you can try the endpoints.

# Brief explanation of the endpoints

![screenshot_from_2022-08-18_21-08-31](https://user-images.githubusercontent.com/78916039/191230283-6e833223-af15-4269-85f2-a7567fbed4f5.png)

There are 1 search and 2 database purposes endpoints. 

- /api/v1/search endpoint is responsible for finding places.
- /api/v1/infodb endpoint returns the database so you can check the older found places.
- /api/v1/cleardb endpoint cleans the database.

