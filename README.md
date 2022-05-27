# 

## Python
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
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

## PSQL
Connect to psql
```
psql -U mandat -h 0.0.0.0 -p 5432
```

list db
```
\l
```

## MongoDB
Connect to mongodb
