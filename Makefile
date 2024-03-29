setup-web-app:
	docker-compose up -d
	docker exec welbex-test_web-app_1 python manage.py migrate
	docker exec welbex-test_web-app_1 python manage.py load_locations
	docker exec welbex-test_web-app_1 python manage.py generate_trucks -20

run-web-app:
	docker-compose up -d

tests:
	docker-compose up -d
	docker exec welbex-test_web-app_1 pytest -s
