# Social Media API | Portfolio Project 5



[Live site for frontend](https://lifeshare.herokuapp.com/)

[Live site for backend](https://drf-api-sam.herokuapp.com/)

## Project Goals
- Design an interactive Front-End web application using HTML, CSS and advanced JavaScript, based on component composition and separation of concerns.
   - For more information see [Front-End Repository](https://github.com/mikakallberg/cozycorner)
- Explain the key role that specialist Front-End developers perform in modern software development/delivery terms.
- Create an Application Programming Interface (current repository) for comsumption by 3rd party applications.
   - Create Unique models.
      - Number of models created four, two in contacts and two in imessages.
- Create an Interactive Front-End application that consumes API data.
#
## Technologies and Libraries
### Languages used
- [Django Rest Framework](https://www.django-rest-framework.org/) 

- [HTML](https://www.w3schools.com/html/html_intro.asp)

- [CSS](https://www.w3schools.com/css/css_intro.asp)

- [React JS](https://reactjs.org/)

### Databases and server gateways
- [Postgresql](https://www.postgresql.org/)
  - As database in Heroku
- [SQLite](https://www.sqlite.org/index.html)
  - As database for Gitpod, the initial thought was to use this for unittest.
  The setting is left as part of future features, to have automatic testing instead of manual testing
- [Daphne ASGI](https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/daphne/)

### Frameworks, tools and libraries
#### Back-End
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Channels-redis](https://channels.readthedocs.io/en/latest/index.html) 
   - Websocket tool
- [Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html)
   - To assist upload images to cloudinary
- [Psycopg2](https://pypi.org/project/psycopg2/)
   - PostgreSQL database adapter for python
- [JSON Web Tokens](https://jwt.io/)
   - Http-safety, web-tokens for kepping user logged in, authentication etc.
#### Front-End
- [React JS](https://reactjs.org/)
- [JSON Web Tokens](https://jwt.io/)
    - Web-tokens for kepping user logged in, authentication etc.
- [React Bootstrap](https://react-bootstrap-v4.netlify.app/)
   - Specilaize Bootstrap framework with React components
- [React Router](https://v5.reactrouter.com/web/guides/quick-start)
   - Assist in switches, routes and links for React apps.


### Cloud storage and deployment services
- [Cloudinary](https://cloudinary.com/)
- [Heroku](https://www.heroku.com/)
- [Gunicorn](https://gunicorn.org/)