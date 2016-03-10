flask-template
===

Large Application Example.

### Features

- ORM for flask-sqlalchemy, sqlalchemy
- Testing for pyunit


### Test

```sh
./manage.py test
```


### Deploy to GAE

```sh
mkdir lib
pip install -r requirements.txt -t lib
gcloud app deploy app.yaml
```


### TODO
- [ ] replace flask-script to flask.cli ( http://flask.pocoo.org/docs/0.11/cli/#custom-scripts )
