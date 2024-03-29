# aeupdates
aeupdates.com

## DEV

<h2>Local docker</h2>
- create file `production_settings.py` in `/aeupdates`, similar as `settings.py`
```
cd deploy/django_docker
docker build -t aeupdates -f deploy/django_docker/Dockerfile
docker run -it -p 8080:8080 -p 8084:8084 -t aeupdates
```

<h4>Deployment</h4>

 1) stop old main contaier `docker stop <container_id>`

 2) `ansible-playbook -l production -i deploy/hosts deploy/deploy.yml -vvvv --extra-vars "DEPLOYING_ENDPOINT=production"` or
 `ansible-playbook -l staging -i deploy/hosts deploy/deploy.yml -vvvv --extra-vars "DEPLOYING_ENDPOINT=staging"`

<h4>Changes, might needed before deployment in production</h4>

  1) Change HOST in `/apps/frontend/config/enviroment.js`:
    `ENV.APP.API_HOST = 'http://37.139.30.9:8080'`;
    
  2) Fix static files for django: `python manage.py collectstatic` (also done by every build)



<b>If instance is new or migrations needed</b>
1)python manage.py migrate
2)python manage.py createsuperuser


###Local installation for Mac developers:

### virtualenvwrapper Installation

```bash
pip install virtualenvwrapper
```

add the following lines to your `~/.bashrc` file:

```bash
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

then run

```bash
source ~/.bashrc
mkvirtualenv -p /path/to/python3.4 aeupdates
```


- install psql: `brew install postgresql`
- install mongodb: `brew install mongodb`
- install requirements: `pip install -r requirements.txt`
- create file `secret_config.py` near `public_config`
- run migrations - `python manage.py migrate`
- create superuser - `python manage.py createsuperuser`
- install ember if not installed `npm install -g ember-cli@2.4`
- install bower if not installed `npm install -g bower`

## Build docker and push to Hub

```bash
cd aeupdates/depoloy
docker build -t aeupdates django_docker
```
then push to hub - `https://docs.docker.com/engine/getstarted/step_six/`

## Problems with migrations?
`python manage.py --settings=aeupdates.production_settings makemigrations corsheaders`
`python manage.py --settings=aeupdates.production_settings migrate`

## Problems with database?
1) `docker exec -it <image_id> bash`
2) `psql -U postgres`

## Problems with disk space?
```bash
# Delete all stopped containers
docker rm $( docker ps -q -f status=exited)
# Delete all dangling (unused) images
docker rmi $( docker images -q -f dangling=true)
# Delete all non-tagged images
docker rmi $(docker images | grep "^<none>" | awk "{print $3}")
```

### Problems with SSL ?
 - `/usr/sbin/nginx -s stop`
 - `certbot certonly --standalone -d aeupdates.com`
 - `service nginx start`

### Problems with metrics agents?

If you ever want to stop the Agent, run:
```
    sudo /etc/init.d/datadog-agent stop
```
And to run it again run:
```
    sudo /etc/init.d/datadog-agent start
```

### Problems with Nginx?

look for processes `ps -aux | grep "nginx"`
stop processes `/usr/sbin/nginx -s stop`
read logs `cat /var/log/nginx/error.log`


### Get mongo stats ?
`docker exec -i -t <id> /bin/bash`
`mongodump --out /mongodb_dumped_db`
`tar -zcvf mongodbdumped.tar.gz /mongodb_dumped_db/`
exit from container
`docker cp <id>:/mongodbdumped.tar.gz mongodbdumped.tar.gz`
exit from ssh session
`scp user@<ip>:~/mongodbdumped.tar.gz ~/mongodumped.tar.gz`
`cd ~ && tar -zxvf mongodumped.tar.gz && mongorestore mongodb_dumped_db`
