# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
yum install -y epel-release
yum install -y mc htop rpmdevtools mock createrepo
usermod -aG mock vagrant
SCRIPT

Vagrant.configure(2) do |config|
  config.vm.box = "subuk/centos7"
  config.ssh.forward_agent = true
  config.vm.hostname = "pushpin-rpmbuild"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 4096
    vb.cpus = 4
  end
  config.vm.provision "shell", inline: $script
end
