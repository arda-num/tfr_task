# TFR API Task

This repository consist of an Rest API made by *<b>Django Rest Framework</b>* to search places through latitude and longitude values.

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

![Screenshot from 2022-09-20 13-06-01](https://user-images.githubusercontent.com/78916039/191230526-52f79847-5fb7-4885-8e52-f9424bd5a5ab.png)

There are 1 search and 2 database purposes endpoints. 

- /api/v1/search endpoint is responsible for finding places.
- /api/v1/infodb endpoint returns the database so you can check the older found places.
- /api/v1/cleardb endpoint cleans the database.

