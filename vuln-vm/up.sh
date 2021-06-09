#!/usr/bin/env sh

gcloud compute instances create old-vm \
  --tags=http-server \
  --image=debian-10-buster-v20210512 \
  --image-project=debian-cloud \
  --boot-disk-size=10GB \
  --boot-disk-type=pd-balanced \
  --boot-disk-device-name=old-vm \
  --metadata-from-file=startup-script=./cloud-init.sh


