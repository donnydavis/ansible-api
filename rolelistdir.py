import os
from settings import *


def listRoles(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['playbooks'] = []
        paths = [
            os.path.join(path,x)
                for x in os.listdir(path)
                    if not x.startswith('.')
                    if not x.endswith(tuple(IGNORED_FILES))
                ]
        for p in paths:
            c = listRoles(p)
            if c is not None:
                d['playbooks'].append(c)
        if not d['playbooks']:
            return None
    else:
        d['type'] = "playbook"
    return d
