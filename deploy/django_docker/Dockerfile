FROM centos:centos7
MAINTAINER mehanig <mehanig@gmail.com>

RUN yum install -y http://dl.iuscommunity.org/pub/ius/stable/CentOS/7/x86_64/ius-release-1.0-14.ius.centos7.noarch.rpm \
 && yum install -y http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-1.el7.nux.noarch.rpm \
 && yum install -y epel-release \
 && yum clean all

RUN yum install -y git tar gcc pcre-devel zlib-devel openssl openssl-devel wget \
 && yum install -y python34 \
 && yum install -y python34-devel \
 && yum install -y ffmpeg \
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

# create pyvenv with python34 and activate it
# one can't just create pyvenv because of bugs with pip
# workaround - http://www.ctlai.com/?p=124
RUN pyvenv-3.4 aeupdates_venv --without-pip \
  && wget https://bootstrap.pypa.io/get-pip.py \
  && source /aeupdates_venv/bin/activate \
  && python get-pip.py

# for psycopg2
RUN yum -y install postgresql-devel

# Install Node and Ember.js
RUN curl --silent --location https://rpm.nodesource.com/setup_5.x | bash - \
 && yum -y install nodejs \
 && yum clean all

RUN npm install -g ember-cli@2.4
RUN npm install -g bower

# Invalidate cache and clone aeupdates repo and install python requirements
RUN echo `date` > build_time
ADD  build_time /.build_time
RUN source /aeupdates_venv/bin/activate \
  && git clone https://github.com/mehanig/aeupdates \
  && cd aeupdates \
  && grep -v "^#" requirements.txt | xargs -n 1 -L 1 pip install

# Create dir for ember project
RUN mkdir -p /aeupdates/aeupdates/static/ember

# Generate all necessary adapters and install all stuff, buld project from run.sh
RUN cd /aeupdates/apps/frontend \
 && npm install \
 && bower install --allow-root \
 && ember install ember-django-adapter
# && ember build -o /aeupdates/aeupdates/static/ember \

# Create filder for nginx folder
RUN mkdir /aeupdates/docker_nginx_folder

ADD docker_run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 8080 8084 443 5432 27017

CMD /run.sh
