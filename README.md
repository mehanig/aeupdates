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
