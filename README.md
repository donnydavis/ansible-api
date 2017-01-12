# Ansible API
This is a really really simple ansible API written in Flask.

The code is crappy at best, and not meant for production use in any way shape or form

This code is insecure, and not suitable for any system outside of a confined test enviroment

If you are looking for a fully fledged API, take a look at Ansible Tower by Red Hat.

This Flask app lets you look at your roles via the api, and lets you run playbooks via the API

To get started

      git clone https://github.com/donnydavis/ansible-api.git
      cd ansible-api
      python server.py

An example role is included to run a test to ensure the system is functioning

    curl --request POST \
      --url http://127.0.0.1:8080/api/run/ \
      --data 'role=test' \
      --data 'play=hello.yml' \
      --data 'host=localhost'


The role parameter relates to the directory your role is in

The play parameter is the Ansible playbook you want to run

The host parameter is the host you want to run the play against

This is honestly just some code I threw together to see if I could write an

API that actually does something, as it turns out I can but not very well

Thanks for checking it out

~D
