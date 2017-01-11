from flask import *
import os
from rolelistdir import listRoles
from settings import *
import subprocess

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    """Welcome to Ansible API"""
    return jsonify({'hello': 'What would you like to automate today?'})


@app.route('/api/', methods = ['GET'])
def apiIndex():
    """These are the available APIS."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)

@app.route('/api/roles/', methods = ['GET'])
def getRoles():
    """A list of installed Roles"""
    return jsonify(listRoles(ROLES_DIR))

@app.route('/api/run/', methods = ['GET','POST'])
def runPlay():
    """Run an Ansible Playbook"""
    if request.method == 'POST':
        p = request.values.get("play")
        r = request.values.get("role")
        h = request.values.get("host")
        process = subprocess.Popen(["/usr/bin/ansible-playbook", "--limit=" + str(h), os.path.join(ROLES_DIR,r,p)])
        return jsonify({'RunningPlay': {'name': p}})
    else:
       return '''To use this API
curl --request POST \
  --url http://127.0.0.1:8080/api/run/ \
  --data 'role=test' \
  --data 'play=hello.yml' \
  --data 'host=localhost'
       '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
