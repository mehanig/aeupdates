FROM centos:centos7
MAINTAINER mehanig <mehanig@gmail.com>

RUN yum install -y http://dl.iuscommunity.org/pub/ius/stable/CentOS/7/x86_64/ius-release-1.0-14.ius.centos7.noarch.rpm \
 && yum install -y http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-1.el7.nux.noarch.rpm \
 && yum install -y epel-release \
 && yum clean all

RUN yum install -y git tar gcc pcre-devel zlib-devel openssl openssl-devel \
 && yum install -y ffmpeg \
 && yum clean all

RUN yum-builddep -y python \
 && curl -O https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz \
 && tar xf Python-3.5.1.tgz \
 && cd Python-3.5.1 \
 && ./configure \
 && make \
 && make install \
 && yum clean all

# Compile and install nginx with upload module
RUN curl -o nginx.tar.gz http://nginx.org/download/nginx-1.9.1.tar.gz \
 && tar xvzf nginx.tar.gz \
 && pushd nginx-1.9.1 \
 && curl -L -o nginx-upload-module.tar.gz https://github.com/vkholodkov/nginx-upload-module/archive/2.2.tar.gz \
 && tar xvzf nginx-upload-module.tar.gz \
 && ./configure --add-module=./nginx-upload-module-2.2 \
 && make \
 && make install \
 && popd \
 && rm -rf nginx-1.9.1 nginx.tar.gz

# create pyvenv with python35 and activate it
RUN pyvenv aeupdates_venv && source /aeupdates_venv/bin/activate

# Invalidate cache and clone video compressor repo and install python requirements
RUN echo `date` > build_time
ADD  build_time /.build_time
RUN git clone https://github.com/mehanig/aeupdates \
  && pip3 install -r aeupdates/requirements.txt

ADD docker_run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 8080 8084 443

CMD /run.sh
