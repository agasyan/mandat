# 

## Python
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 generate.py
```

## Docker
Start DB
```
docker-compose up
```

Remove All containers
```
docker rm -f $(docker ps -a -q)
```

Remove All volumes (including db data)
```
docker volume rm $(docker volume ls -q)
```

Check size
```
docker system df -v
docker ps --size
```

## PSQL
Connect to psql
```
psql -U mandat -h 0.0.0.0 -p 5432
```

list db
```
\d
```

list relations
```
\l
```

Quit
`ctrl+D`

How to run:
- Run `schema.sql`
- Run `out.sql` / `sample.sql`

## MongoDB
Install Mongosh `https://www.mongodb.com/docs/mongodb-shell/install/#std-label-mdb-shell-install`
Insert `https://www.mongodb.com/docs/manual/reference/method/db.collection.insertMany/#mongodb-method-db.collection.insertMany`

Connect to mongodb
```
mongosh "mongodb://localhost:27017" --username mandat --password mandat --authenticationDatabase admin
```

check dbs / collections
```
show dbs
show collections
```

create new database
```
use mandatdbs
```

Quit
`ctrl+D`