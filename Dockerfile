FROM amazon/aws-cli:latest

RUN yum update -y && yum install -y python3 python3-pip

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY . /tools
WORKDIR /tools

CMD ["python3", "-m", "tools"]