# Ansible API
This is a really really simple ansible API written in Flask. It's meant to be lightweight and used in a distrubted manner to bring scale to Ansible and the capability to make REST based requests to a host. 

The code is not meant for production use in its current state. Its missing functions to protect your system from misuse.

If you are looking for a fully fledged API, take a look at the AWX project. 

This Flask app lets you look at your roles via the api, and lets you run playbooks via the API

To get started

      sudo pip install flask
      git clone https://github.com/donnydavis/ansible-api.git
      cd ansible-api
      python ansibleapi.py

##An example role is included to run a test to ensure the system is functioning

    curl --request POST \
      --url http://127.0.0.1:8080/api/run/ \
      --data 'role=test' \
      --data 'play=hello.yml' \
      --data 'host=localhost'


The role parameter relates to the directory your role is in

The play parameter is the Ansible playbook you want to run

The host parameter is the host you want to run the play against

##If you want to view the available roles, it looks like this

    curl --request GET \
      --url http://127.0.0.1:8080/api/roles/

The json output is configurable in the settings.py file

##AnsibleAPI can also fetch roles from github. Support for arbitary git repos will be in the next release.

    curl --request POST \
      --url http://127.0.0.1:8080/api/roles/github/get \
      --data 'username=donnydavis' \
      --data 'role=ansible-rh-subscription-manager'


The instructions for how to operate the POST methods of the API are in the GET methods.

##If you are unsure of how to run a POST, then do a GET on the same API and an example will be printed for you

    curl --request GET \
      --url http://127.0.0.1:8080/api/roles/github/get


###Thanks for checking out AnsibleAPI
