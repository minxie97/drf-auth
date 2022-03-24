# Authentication & Production Server
Moving our API closer to production grade by adding Authentication and switching to a Production Server

## Deployment
N/A (for now)

## PR Link
[Pull Request](https://github.com/minxie97/drf-auth/pull/2)

## Testing with httpie
1. install http either with a pip install or poetry add depending on your virtual environment
2. Be sure to docker compose up and migrate
3. Create a super user using `docker compose run web python manage.py createsuperuser`
4. Go into the site and create some data. Make some games using your new log in
5. Check first that the authentication is working by running `http :8000/api/games`. This should return something that says you are not authorized
6. Next get some tokens: run `http POST :8000/api/token username='USERNAME YOU CREATED' password='PASSWORD YOU CREATED'`. This should return you an access token and refresh token
7. Now try `http :8000/api/games 'Authorization: Bearer ACCESS TOKEN'`. Now you should be able to see the data you created.
