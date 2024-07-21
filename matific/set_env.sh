docker-compose up -d

# Wait for the backend container to be healthy
echo "Waiting for backend container to be healthy..."
until [ "$(docker inspect --format='{{.State.Health.Status}}' $(docker-compose ps -q backend))" == "healthy" ]; do
  sleep 5
done

echo "Backend container is healthy!"

docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py data_mock
