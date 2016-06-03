# aeupdates
aeupdates.com


<h2>Centos Deployment:</h2>
<h4> something </h4>
    
<h4> dockers </h4>
    ....
    docker build -t aeupdates .
    docker run -it -p 8080:8080 -p 8084:8084 -t aeupdates
    ...


<h4>Deployment</h4>
ansible-playbook -l production -i deploy/hosts deploy/deploy.yml -vvvv


<h4>Changes, needed before deployment in production</h4>

1) Change HOST in /apps/frontend/config/enviroment.js:
    ENV.APP.API_HOST = 'http://37.139.30.9:8080';



<b>If instance is new or migrations needed</b>
1)python manage.py migrate
2)python manage.py createsuperuser


###Local installation for developers:

 1) create file `secret_config.py` near `public_config`
 2) run migrations - `python manage.py migrate`
 3) create superuser - `python manage.py migrate`