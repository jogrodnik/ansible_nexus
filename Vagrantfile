# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "bento/centos-7.2"

  config.vm.define "nexus1" do |machine|
    machine.vm.hostname = "nexus1"
    machine.vm.network "private_network", ip: "192.168.56.101"
    machine.vm.network "forwarded_port", guest: 8081, host:8081
    machine.vm.provider "virtualbox" do |v|
        v.memory = 2048
        v.cpus = 2
    end
    machine.vm.synced_folder "./", "/vagrant", disabled: true
  end

  config.vm.define 'controller' do |machine|
    machine.vm.hostname = "controller"
    machine.vm.network "private_network", ip: "192.168.56.200"
    machine.vm.provider "virtualbox" do |v|
        v.memory = 1024
        v.cpus = 1
    end
    machine.vm.synced_folder "./", "/vagrant", disabled: true
    machine.vm.synced_folder "./", "/home/vagrant/ansible_nexus",owner: "vagrant",mount_options: ["dmode=775,fmode=600"]
    machine.vm.provision :ansible_local do |ansible|
        ansible.provisioning_path = "/home/vagrant/ansible_nexus"
		ansible.playbook = "playbooks/controller.yml"
		ansible.verbose = true
		ansible.install = true
		ansible.limit = "nexus"
		ansible.inventory_path = "ansible_hosts"
    end
  end
end
