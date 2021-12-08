api_version=0.2.1
web_version=0.1.10

build:
	docker build -t k8s-fibonacci/api:dev-${api_version} api/
	docker build -t k8s-fibonacci/web:dev-${web_version} web/

run-api:
	docker run -p 5000:5000 k8s-fibonacci/api:dev-${api_version}

run-web:
	docker run -p 80:80 k8s-fibonacci/web:dev-${web_version}

apply:
	kubectl apply -f .k8s/

delete:
	kubectl delete -f .k8s/

browser:
	google-chrome http://192.168.49.2/