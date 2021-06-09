# Export values from Redis and Prometheus metrics

This project is a prototype of data pipeline that would export values from Redis as prometheus metrics with http exporter (pull strategy)

# Build and run
`bash up.sh` will 
- build docker image 
- start Redis
- initialize Redis with values (redis/init_redis.sh)
- access metrics from exporter with curl 

Then it will remain there - so that you could connect Prometheus to it, or simply `bash down.sh`
