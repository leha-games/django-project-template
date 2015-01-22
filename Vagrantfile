# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://vagrantcloud.com/ubuntu/boxes/trusty64/versions/1/providers/virtualbox.box"

  #config.vm.synced_folder ".", "/var/webapps/{{ project_name }}/code", owner: "{{ project_name }}", group: "{{ project_name }}"

  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 8001, host: 8002
  config.vm.network :private_network, ip: "192.168.33.10"

  config.cache.auto_detect = true

  config.vbguest.iso_path = "#{ENV['HOME']}/Downloads/VBoxGuestAdditions.iso"

end
