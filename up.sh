docker-compose up -d --build -V
echo "Initialize Redis values"
docker-compose exec redis bash /app/init_redis.sh

curl http://localhost:8000
