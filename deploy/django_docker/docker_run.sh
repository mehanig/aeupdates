#!/bin/bash

UPLOADS_DIR=/aeupdates

set -e
# Create folders required by nginx upload module
mkdir -p $UPLOADS_DIR/docker_nginx_folder/upload/tmp/{0..9}
chmod -R 777 $UPLOADS_DIR/docker_nginx_folder

# Build Ember Project

# TODO: Simplify this logic.
if [[ $DEPLOYING_ENDPOINT == "production" ]]
then
    cd /aeupdates/apps/frontend && ember build -o /aeupdates/aeupdates/static/ember --environment=production
fi

if [[ $DEPLOYING_ENDPOINT == "staging" ]]
then
    mv -f /aeupdates/apps/frontend/config/staging_environment.js /aeupdates/apps/frontend/config/environment.js
    cd /aeupdates/apps/frontend && ember build -o /aeupdates/aeupdates/static/ember --environment=production
fi

/usr/local/nginx/sbin/nginx -c /aeupdates/nginx_conf/nginx.conf

source /aeupdates_venv/bin/activate && cd /aeupdates && uwsgi --socket aeupdates.sock --module aeupdates.wsgi --chmod-socket=666 --env DJANGO_SETTINGS_MODULE=aeupdates.production_settings
tail -f /dev/null
