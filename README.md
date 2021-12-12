# Pythocker

This project is used to find the best way to use [Python on Docker](https://hub.docker.com/_/python)

Use this commands:

```
docker-compose build
docker-compose up -d
docker-compose exec py bash
docker-compose down
```

Inside docker (py bash):

```
source py-env/bin/activate
fab --list
fab hello
```
