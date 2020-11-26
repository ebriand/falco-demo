FROM debian:buster as sudo

RUN apt-get update && apt-get install -y gcc

COPY sudo.c /root/sudo.c

RUN gcc -o /root/sudo /root/sudo.c -static \
  && chmod +s /root/sudo


FROM hmlio/vaas-cve-2014-6271

COPY --from=sudo /root/sudo /usr/local/bin

