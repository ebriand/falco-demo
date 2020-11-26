#!/usr/bin/env sh

helm repo add falcosecurity https://falcosecurity.github.io/charts
helm repo update

helm install -f falco-values.yaml falco falcosecurity/falco

kubectl apply -f ./response-engine/k8s/response-engine.yaml
