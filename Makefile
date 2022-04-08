start:
	docker-compose up -d
	docker exec -it exp-scapy bash

stop:
	docker-compose down
