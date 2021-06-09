#!/usr/bin/env bash

if [[ $1 == "gke" ]]; then
  TARGET=gke
else
  TARGET=minikube
fi

helm repo add falcosecurity https://falcosecurity.github.io/charts
helm repo update

helm install -f "falco-values.${TARGET}.yaml" falco falcosecurity/falco

kubectl apply -f ./response-engine/k8s/response-engine.yaml
