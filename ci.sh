 find ./playbooks -maxdepth 1 -name "*.yml" -print |xargs -n1 ansible-playbook --list-task
 --list-hosts  -i tests/ansible_hosts
