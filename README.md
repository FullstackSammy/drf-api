# Social Media API | Portfolio Project 5

![Am I responsive](/images/responsive.jpg)

[Live site for frontend](https://lifeshare.herokuapp.com/)

[Live site for backend](https://drf-api-sam.herokuapp.com/)

## Project Goals
- Design an interactive Front-End web application using HTML, CSS and advanced JavaScript (React), based on component composition and separation of concerns.
   - For more information see [Front-End Repository](https://github.com/FullstackSammy/lifeshare)
- Explain the key role that specialist Front-End developers perform in modern software development/delivery terms.
- Create an Application Programming Interface (current repository) for comsumption by third party applications.
- Create Unique models
- Create an Interactive Front-End application that consumes API data.
#
## Technologies and Libraries
### Languages used
- [Django Rest Framework](https://www.django-rest-framework.org/) 

- [HTML](https://www.w3schools.com/html/html_intro.asp)

- [CSS](https://www.w3schools.com/css/css_intro.asp)

- [React JS](https://reactjs.org/)

### Databases and server gateways
- [ElephantSQL](https://www.elephantsql.com/)
  - As database in Heroku


### Frameworks, tools and libraries
#### Back-End
- [Django Rest Framework](https://www.django-rest-framework.org/)
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

## Existing Features
### Profile
- Anonymous User can register and create a profile
- Users can log in to their profile
- Users can see registered profiles
- Users can see a list of other Users
- Users can see the a detail view of other users
#
### Post
- Anonymous User and registered Users can see public posts
- Users can create posts with or without images
- Users can edit posts that they own
- Users can delete posts that they own
#
### Comments
- Anonymous User and Users can see public comments
- Users can create a comment on a post
- Users can edit a comment they have created
- Users can delete a comment they have created
#
### Likes
- Anonymous User and Users can see likes on posts
- Users can like a post
- Users can unlike a post
#
### Followers
- Anonymous User and Users can see followers
- Users can follow a User
- Users can unfollow a User
#
## Testing in development
- After creation of a superuser.
   -Test to see that /admin worked and that admin view is running correctly
   - created 9 other profiles
      - Test if default image works
      - Test if password requirements work
- Testing responsiveness with [AmIResponsive](https://ui.dev/amiresponsive?url=https://lifeshare.herokuapp.com/)
- When trying to test for PEP8 conformity, the webpage http://pep8online.com/ is no longer active.
    - However the code conforms to the way taught in lesson material from Code Institute
#
## Profile
- Manual testing done on profile (no written tests done):
   - Possible for superuser to edit user profile in UI
      - Other non-superusers cannot change info on other users
      - Other non-superusers cannot access admin-panel
      - Testing done on profile 1, 3 and 5 after adding authentication. Testing also in logged out state. Only owner can access edit tool for profile
   -After refactoring:
      - test delete profile, successfull
      - No access to delete other users profiles
   - Test filtering profiles:
       - after which profile is following who and order in descending and ascending order for follow count, post count, owner following created at
       - profiles following other profiles or not and then ordering then differently ascending and descending order.
   - Access non existent profile
      - 404 does not exist
#
## Post
- Tests I wrote for the Posts app (see testfile in app):
   - test_post_creation (Test that a Post instance can be created and saved to the database)
   - test_post_deletion (Test that a Post instance can be deleted from the database)
   - test_post_update (Test that a Post instance can be updated)
#
## Comments
- Tests I wrote for the Comments app (see testfile in app):
   - test_str_method (Test that the string representation of a comment is its content)
   - test_owner_field (Test that the owner field of a comment is set correctly)
   - test_post_field (Test that the post field of a comment is set correctly)
   - test_content_field (Test that the content field of a comment is set correctly)
   - test_ordering (Test that comments are ordered by descending creation date)
#
## Likes
- Testing done on like (No written tests done):
   - Manual tests:
   - Unauthenticated users
      - No access to liking posts
   - Authenticated users can like posts
      - Successfull
      -Error if duplicate like attempted
   - Authenticated and authorized user can delete like
      - Successfull
   - Access non existent like
      - 404 does not exist
#
## Followers
- Manual testing done on followers (no written tests done):
   - Test following authenticated users as a authenticated user
   - No access to follow authenticated user while not logged in
   - Successful unfollowing a authentictated user as a logged in user
   - A user can't remove an authenticated User from their followers list
      - Possible improvement
   - Access non existent follow
      - 404 does not exist
#
## Private Messages
- Tests I wrote for the Private Messages app (see testfile in app):
   - test_str_method (Test that the string representation of a message is its content)
   - test_sender_field (Test that the sender field of a message is set correctly)
   - test_recipient_field (Test that the recipient field of a message is set correctly)
   - test_content_field (Test that the content field of a message is set correctly)
   - test_get_list (Test that a GET request to the private message list returns all messages)
#
## Bugs in development
- In initial deployment to Heroku, app did not launch. 
  - Looked through code to spot typos and typos in heroku settings. Found a couple, with the help of [Stackhawk](https://www.stackhawk.com/blog/django-cors-guide/), also hard set the allowed hosts to the heroku url.
#
## Bugs left unsolved
    - 4 line to long on line 136, 139, 142 and 145. 
      - These can't be modified, since doing so will create a more serious error that affects functionality.
#
## Final Deployment
- Following the walkthrough on deployment.
    - Redownloading all the applications.
    - Download:
       - [Corsheaders](https://pypi.org/project/django-cors-headers/)
       - [DJ-REST-AUTH](https://dj-rest-auth.readthedocs.io/en/latest/introduction.html)
    - Enable crossorigin communication between the current back end and future front end apps, with settings in settings.py:
        - if-statements for CLIENT_ORIGIN_DEV, for using different urls in deployment and production.
    - CORS_ALLOWED_CREDENTIALS, to enable cookie authetication so the User is able to automatically be logged from the same source within a 24 hour window.
       - This project will only collect cookies so that the user can log in automatically during a 24 hour window. It will not collect any statistics or any other information on the user.
       - A serializer-file was created in project app to serialize the cookie information.
    -Debug is set to a os.environ variable, so that when in production debug will be true, but not in production.
    - Allowed hosts are set to a os-environ variable to allow multiple outside projects to use this API.
    - Change Allowed hosts in Heroku config vars to match the name string used in settings.py..
    - Deploy page in Heroku successful.
    - Ensure that all apps with functions exists in the final deployed version as in development version.
        - exists in JSON-data
#
## Credits
## Thank you
- Antonio for always being there and being a fantastic mentor.
- Tutors at Code Institute
- Code Institute Slack-channel community for being the good and funny bunch of people I need!


### Content credits
- The biggest credit has to go Code Institute, I followed the Walkthroughs given, and developed a little on top of it.
- To Mikaela (fellow student), for readme.md template

### Media
- Every media image that was used, came from my personal library and the free resource [Unsplash](https://unsplash.com/)

#
* [Back to top](#)
#