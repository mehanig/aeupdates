FROM centos:centos7
MAINTAINER mehanig <mehanig@gmail.com>

RUN yum install -y epel-release \
 && yum install -y nginx \
 && yum clean all

RUN yum install -y git tar gcc pcre-devel zlib-devel openssl openssl-devel wget \
 && yum install -y python36 \
 && yum install -y python36-devel \
 && yum clean all

# create pyvenv with python34 and activate it
# one can't just create pyvenv because of bugs with pip
# workaround - http://www.ctlai.com/?p=124
RUN pyvenv-3.6 aeupdates_venv --without-pip \
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
# and Collect static
#RUN echo `date` > build_time.txt
#ADD  build_time.txt /.build_time.txt
RUN source /aeupdates_venv/bin/activate \
  && git clone https://github.com/mehanig/aeupdates \
  && cd aeupdates \
  && grep -v "^#" requirements.txt | xargs -n 1 -L 1 pip install \
  && python manage.py collectstatic --noinput

# Create dir for ember project
RUN mkdir -p /aeupdates/aeupdates/static/ember

# Generate all necessary adapters and install all stuff, buld project from run.sh
RUN cd /aeupdates/apps/frontend \
 && npm install \
 && bower install --allow-root
#  && ember install ember-django-adapter
# && ember build -o /aeupdates/aeupdates/static/ember \

# Create filder for nginx folder
RUN mkdir /aeupdates/docker_nginx_folder

ADD /deploy/django_docker/docker_run.sh /run.sh
ADD /aeupdates/production_settings.py /aeupdates/aeupdates/production_settings.py
RUN chmod +x /run.sh

EXPOSE 8080 8084 443 5432 27017

CMD /run.sh
