#!/usr/bin/env python

import yaml
import subprocess
import os
import re
import pprint


pp = pprint.PrettyPrinter(indent=4)
installed = 0
for root, dirs, files in os.walk('playbooks/roles'):
    for file in files:
        filePath = os.path.join(root, file)
        if re.findall("meta/main.yml$", filePath):

            stream = open(filePath, 'r')
            data = yaml.load(stream)

            process = subprocess.Popen(["ansible-galaxy", "list"], stdout=subprocess.PIPE)
            installedDeps = process.communicate()[0]
            installedDepsList = re.findall("^-\s([^,]*)", installedDeps, re.M)
            requiredDeps = data["dependencies"]
            if requiredDeps:
                for item in requiredDeps:
                    pp.pprint( item )
                    if isinstance(item, dict):
                        role_name=item["role"]
                    if not role_name in installedDepsList:
                        if not os.path.isdir("playbooks/roles/" + role_name):
                            subprocess.call(["sudo", "ansible-galaxy", "install", role_name])
                            installed += 1

if installed == 0:
    print "All Ansible galaxy dependencies already installed"
