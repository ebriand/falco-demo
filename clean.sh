#!/usr/bin/env bash

helm delete falco

kubectl delete deploy response-engine
