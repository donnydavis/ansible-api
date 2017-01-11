#### API Role Listing Setup
ROLES_DIR = "roles"
#This tuple is to prevent the api from pulling data from the roles you do not want to appear
#If you want to ignore an entire directory, enter the full name
#Anything that starts with a . will automatically be ignored
IGNORED_FILES = [".md", ".j2", "Vagrantfile", "meta", ".cfg", "handlers", "defaults", "vars", "LICENCE", "files", "templates", "spec", "Rakefile", "Gemfile"]
