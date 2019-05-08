"""Simple ansible API using Flask"""

import os
import subprocess
from flask import Flask, jsonify, request

from helpers import list_roles, get_funcdocs
from settings import ROLES_DIR, IGNORED_FILES


APP = Flask(__name__)


@APP.route("/", methods=["GET"])
def index():
    """Welcome to Ansible API"""
    return jsonify({
        "hello": "Welcome to Ansible API, try GET: /api/ for more information"
    })


@APP.route("/api/", methods=["GET"])
def api_index():
    """These are the available APIS."""
    return jsonify(get_funcdocs(app=APP))


@APP.route("/api/roles/", methods=["GET"])
def get_roles():
    """A list of installed Roles"""
    return jsonify(list_roles(ROLES_DIR, IGNORED_FILES))


# This could really stand to have some way to monitor the status of the
# subprocess and handle errors, currently they are masked by the static
# response. Storing them somewhere and then allowing another API call to
# retrieve status may be sufficient. Some sort of callback might be better
# for users, though. Better default response would be good as well.
# TODO: This needs a lot of error handling
@APP.route("/api/roles/github/", methods=["GET", "POST"])
def get_role():
    """Run an Ansible Playbook"""
    if request.method == "POST":
        username = request.values.get("username")
        role = request.values.get("role")
        _ = subprocess.Popen(["/usr/bin/git", "clone", "https://github.com/" +
                              str(username) + "/" + str(role) + ".git",
                              os.path.join(ROLES_DIR, role)])
        return jsonify({"RunningPlay": {"name": role}})
    return """Currently only github is supported, try:
                curl --request POST
                --url http://127.0.0.1:8080/api/run/
                --data 'username=username'
                --data 'role=ansible-rh-subscription-manager'
            """


# See the comment on get_role()
# TODO: This needs a lot of error handling
@APP.route("/api/run/", methods=["GET", "POST"])
def run_play():
    """Run an Ansible Playbook"""
    if request.method == "POST":
        play = request.values.get("play", None)
        role = request.values.get("role", None)
        host = request.values.get("host", None)
        _ = subprocess.Popen(["/usr/bin/ansible-playbook", "--limit=" +
                              str(host), os.path.join(ROLES_DIR, role, play)])
        return jsonify({"RunningPlay": {"name": play}})
    return """To use this API, try:
                curl --request POST 
                --url http://127.0.0.1:8080/api/run/ 
                --data 'role=test'
                --data 'play=hello.yml' 
                --data 'host=localhost'
            """


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8080, debug=True)
