# TRACING

## SETUP Instrumentation

docker compose -f docker-compose-test-tracing2.yaml up jaeger redpanda mysql

## INSTALL PYTHON dependencies

    alias python=python3
    pip3 install faker
    pip3 install mysql-connector-python

## PREPARE DB

python put_data_mysql.py

### First Terminal

docker exec -it lib-mysql mysql -u root -p
use 4steps;
describe data;
select count(*) from data;

### Second Terminal

kafkacat -b localhost:9092 -t c_results

## RUN BENTHOS

docker compose -f docker-compose-test-tracing2.yaml up benthos

## DASHBOARDS

JAEGER: http://localhost:16686/
GRAFANA: http://localhost:3000/d/93nsGpYnk/benthos-profiling?orgId=1&refresh=5s
