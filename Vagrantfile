# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.synced_folder "scripts/", "/home/vagrant/scripts/"
  
  config.vm.define :master1 do |master1|
    master1.vm.hostname = "master1"
    master1.vm.network :private_network, ip: "192.168.102.11"
    master1.vm.network :private_network, ip: "192.168.102.111"
    master1.vm.network :private_network, ip: "192.168.102.112"
    master1.vm.network :private_network, ip: "192.168.102.113"

    master1.vm.provision :puppet do |puppet|
      puppet.manifests_path = "provision/puppet/manifests"
      puppet.module_path = "provision/puppet/modules"
      puppet.manifest_file = "master.pp"
      puppet.options = ['--verbose']
    end
  end

  config.vm.define :slave1 do |slave1|
    slave1.vm.hostname = "slave1"
    slave1.vm.network :private_network, ip: "192.168.102.21"
    
    slave1.vm.provision :puppet do |puppet|
      puppet.manifests_path = "provision/puppet/manifests"
      puppet.module_path = "provision/puppet/modules"
      puppet.manifest_file = "slave.pp"
      puppet.options = ['--verbose']
    end
  end

  config.vm.define :slave2 do |slave2|
    slave2.vm.hostname = "slave2"
    slave2.vm.network :private_network, ip: "192.168.102.22"
    
    slave1.vm.provision :puppet do |puppet|
      puppet.manifests_path = "provision/puppet/manifests"
      puppet.module_path = "provision/puppet/modules"
      puppet.manifest_file = "slave.pp"
      puppet.options = ['--verbose']
    end    
  end
end