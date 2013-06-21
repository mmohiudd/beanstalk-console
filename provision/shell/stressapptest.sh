#!/bin/bash

cd /vagrant/provision/files/

# download
wget https://stressapptest.googlecode.com/files/stressapptest-1.0.6_autoconf.tar.gz -O stressapptest-1.0.6_autoconf.tar.gz

# untar
tar zxvf /vagrant/provision/files/stressapptest-1.0.6_autoconf.tar.gz -C /vagrant/provision/files/

# start installing
cd stressapptest-1.0.6_autoconf
./configure
make
sudo make install
