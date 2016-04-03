#!/bin/bash

UPLOADS_DIR=/aeupdates

set -e
# Create folders required by nginx upload module
mkdir -p $UPLOADS_DIR/nginx_folder/upload/tmp/{0..9}
chmod -R 777 $UPLOADS_DIR/nginx_folder

/usr/local/nginx/sbin/nginx -c /aeupdates/nginx_conf/nginx.conf
