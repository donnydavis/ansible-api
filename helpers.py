"""Helpers for ansible-api"""

import os


# TODO: additional error handling may be required
# TODO: docstring needs work
def list_roles(path, ignored_files):
    """Takes a path and list of ignored files and returns a dictionary.

    :param string path:
        The filesystem path to look for playbooks.
    :param collections.list ignored_files:
        The list of strings to filter path contents.
    :returns: collections.dict containing path contents and other data.
    """
    directory = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        directory['type'] = "directory"
        directory['playbooks'] = []
        paths = [os.path.join(path, x) for x in os.listdir(path)
                 if not x.startswith('.')
                 if not x.endswith(tuple(ignored_files))]
        for this_path in paths:
            contents = list_roles(this_path, ignored_files)
            if contents is not None:
                directory['playbooks'].append(contents)
        if not directory['playbooks']:
            return None
    else:
        directory['type'] = "playbook"
    return directory


# TODO: additional error handling may be required
# TODO: docstring needs work
def get_funcdocs(app=None):
    """Takes an app and returns a list of handler paths and descriptions.

    :param Flask.app app:
        The Flaks app containing the handlers.
    :returns: collections.dict containing API paths and short descriptions.
    :raises: None
    """
    func_list = {}
    if app:
        try:
            for rule in app.url_map.iter_rules():
                if rule.endpoint != "static":
                    # I am not completely sure if this is the best way to get
                    #   the docs, but it seems to work.
                    func_list[rule.rule] = \
                        app.view_functions[rule.endpoint].__doc__
        except KeyError:
            pass
    return func_list
