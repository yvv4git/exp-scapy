FROM debian:10
MAINTAINER Eliseev Vladimir "yvv4recon@gmail.com"

RUN apt-get update && \
    apt-get -qq -y install \
    tshark && \
    apt-get clean