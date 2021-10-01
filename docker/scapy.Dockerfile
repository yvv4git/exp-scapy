FROM python
MAINTAINER Eliseev Vladimir "yvv4recon@gmail.com"

RUN apt-get update && \
    apt-get -qq -y install \
    gcc python-dev tcpdump graphviz imagemagick \
    swig libpcap0.7 libpcap-dev iputils-ping && \
    apt-get clean

# Download scapy
WORKDIR /scapy
ADD https://github.com/secdev/scapy/archive/master.zip .
RUN unzip master.zip -d /scapy

# Install scapy
WORKDIR /scapy/scapy-master
RUN python setup.py install

WORKDIR /scapy/src
ENTRYPOINT ["bash"]