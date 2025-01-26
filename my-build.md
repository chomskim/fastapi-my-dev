# My Build Settings

## Create FastAPI Venv with Python 3.12

```sh
conda create --name fastapi-312 python=3.12
conda activate fastapi-312
pip install -r requirements.txt

sudo apt update
sudo apt install libpq-dev
pip install psycopg2-binary

pip freeze >> requirements.txt

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


```
