# falco-demo

## Setup

Spawn a VM with `vagrant up`

In the vm, start a minikube cluster:

```sh
$ sudo minikube start --vm-driver none
```

Deploy the response engine:

```sh
$ kubectl apply -f /vagrant/response-engine/k8s/
```

Deploy falco:

```sh
$ cd /vagrant
$ ./deploy-falco.sh
```
