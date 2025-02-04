# fastapi-my-dev
**"fastapi-my-dev"** is my dev of  **REST API** backend development project which I created by following the youtube tutorial by @Sanjeev-Thiyagarajan . 

# My Build Settings

## Create FastAPI Venv with Python 3.12

```sh
conda create --name fastapi-312 python=3.12
conda activate fastapi-312
pip install -r requirements.txt

sudo apt update
sudo apt install libpq-dev
sudo apt install python3-dev
sudo apt install build-essential libffi-dev

# sudo apt remove --purge libffi7 libffi-dev
# pip uninstall psycopg2 psycopg2-binary

# pip install psycopg2  # error
# pip install psycopg2 --no-binary :all: # error
conda install -c conda-forge psycopg2

pip freeze > requirements.txt

```
## Run main.py 

```sh
edit main.py
uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
---
export PYTHONPATH=$(pwd) # Or pythonpath=.

pythonpath=. python -m app.main

http http://172.25.118.154:8000/docs
```

## Not install pyjwt, instead use python-jose

```py
# import jwt
# from jwt.exceptions import InvalidTokenError
from jose import JWTError, jwt

# InvalidTokenError --> JWTError
```

## Get JWT from Postman

```js
// Login URL test-->script
pm.environment.set("JWT", pm.response.json().access_token);

```

## Alembic

```sh
alembic init albembic

alembic revision -m "create start"
Generating /home/cskim/git-repo/fastapi-project1/albembic/versions/9220749ef457_create_start.py ...  done

alembic current
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.

alembic upgrade 9220749ef457

alembic current
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
9220749ef457 (head)

alembic revision --autogenerate -m "create all table auto"
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'users'
INFO  [alembic.autogenerate.compare] Detected added table 'posts'
INFO  [alembic.autogenerate.compare] Detected added table 'votes'
  Generating /home/cskim/git-repo/fastapi-project1/albembic/versions/4a0b7adc4a95_create_all_table_auto.py ...  done

alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 9220749ef457 -> 4a0b7adc4a95, create all table auto

```

## Test CORS

```js
fetch('http://localhost:8000')
  .then(res=>res.json())
  .then(console.log)

```

## Using Github

```sh
git init
git add --all
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/chomskim/fastapi-my-dev.git
git push origin main

```

## Use gunicorn

```sh
pip install gunicorn
# pip install httptools
pip install uvloop
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000

sudo apt install httpie

http http://172.25.118.154:8000
HTTP/1.1 200 OK
content-length: 27
content-type: application/json
date: Sun, 26 Jan 2025 13:58:55 GMT
server: uvicorn

{
    "message": "Hello World!!"
}

```

## make service

```sh
vi gunicorn.service
cd /etc/systemd/system
sudo vi api.service #[=gunicorn.service]
sudo systemctl start api
sudo systemctl enable api
```

## Run nginx

```sh
sudo apt install nginx -y
sudo systemctl start nginx
cd /etc/nginx/sites-available
cat default
...
roor /var/www/html
...

sudo vi default
...
server_name _;

location / {/
                proxy_pass http://localhost:8000;
                proxy_http_version 1.1;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection 'upgrade';
                proxy_set_header Host $http_host;
                proxy_set_header X-NginX-Proxy true;
                proxy_redirect off;
}
-- exit --

sudo systemctl restart nginx

# in web browser, we redirected to fastapi server
http http://172.25.118.154
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 27
Content-Type: application/json
Date: Sun, 26 Jan 2025 14:09:05 GMT
Server: nginx/1.18.0 (Ubuntu)

{
    "message": "Hello World!!"
}

```

## Use HTTPS 

- domain name 구입
- name service -- DNS 

```sh
snap --version
snap    2.67
snapd   2.67
series  16
ubuntu  20.04
kernel  5.15.167.4-microsoft-standard-WSL2

sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx
....??

```

## CI/CD

```sh
# Dev Server
git add --all
git commit -m "change something"
git push origin main

# Deploy Server
cd /app_folder
git pull
sudo systemctl restart api

```

## Docker

```sh
# Use docker
# config.py should be changed -- no .env use

vi Dockerfile

docker build -t fastapi .
[+] Building 520.6s (12/12) FINISHED   
...
 => [3/6] RUN apt-get update && apt-get install -y libpq-dev gcc python3-dev --no-install-recommends && rm -rf /var/lib/apt/lists/     9.6s
 => [4/6] COPY requirements.txt .                                                                                                      0.0s 
 => [5/6] RUN pip install --upgrade pip && pip install -r requirements.txt                                                           189.0s 
 => [6/6] COPY . .                                                                                                                     0.9s 
 => exporting to image                                                                                                               318.9s 
 => => exporting layers                                                                                                              272.9s 
...
 => => unpacking to docker.io/library/fastapi:latest                                                                                  46.0s

docker run -d -p 8000:8000 --env-file .env --name fastapi-co -v $(pwd):/app:ro fastapi

# Use docker-compose
docker compose -f docker-compose-dev.yml up -d
[+] Running 0/0
[+] Running 0/1                                                                                                  0.0s 
[+] Building 1.7s (13/13) FINISHED         
...
[+] Running 3/3g to docker.io/library/fastapi-my-dev-api:latest                                                  0.0s
 ✔ Service api                      Built                                                                       1.8s 
 ✔ Network fastapi-my-dev_default   Created                                                                     0.0s 
 ✔ Container fastapi-my-dev-api-1   Started                                                                     0.3s 


docker exec -it fastapi-my-dev-api-1 bash

docker compose -f docker-compose-dev.yml down
[+] Running 3/3
 ✔ Container fastapi-my-dev-api-1       Removed                                                                  0.4s 
 ✔ Container fastapi-my-dev-postgres-1  Removed                                                                  0.4s 
 ✔ Network fastapi-my-dev_default       Removed                                                                  0.2s

docker exec -t fastapi-my-dev-api-1 bash
root@a23ef6275975:/app# ls -al
total 32
drwxr-xr-x 1 root root 4096 Feb  2 12:49 .
drwxr-xr-x 1 root root 4096 Feb  2 12:49 ..
-rw-r--r-- 1 root root  142 Feb  2 12:49 .dockerignore
drwxr-xr-x 4 1000 1000 4096 Jan 22 22:58 app
-rw-r--r-- 1 root root 4812 Jan 27 03:09 requirements.txt
-rw-r--r-- 1 root root  149 Jan 27 02:52 start.py
drwxr-xr-x 2 root root 4096 Jan 22 01:57 test

docker compose -f docker-compose-dev.yml down
[+] Running 2/2
 ✔ Container fastapi-my-dev-api-1  Removed                                                                       0.6s 
 ✔ Network fastapi-my-dev_default  Removed                                                                       0.2s 

# Upload fastapi image to DockerHub
docker login
docker tag fastapi chomskim/fastapi
docker push chomskim/fastapi

```

## PyTest

```sh
pytest -p --disable-warnings
pytest -v -s --disable-warnings  # -s for print() output
pytest -v -s -x --disable-warnings # stop after fail 
pytest -v -s --disable-warnings tests/test_users.py

```


