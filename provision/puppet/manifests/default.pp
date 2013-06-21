group { 'puppet':
    ensure => present,
}

# default path value in the global scope
Exec { path => '/usr/bin:/bin:/usr/sbin:/sbin' }

exec { 
    'apt-get update': 
        command => 'apt-get update';

    'install gcc build-essential':
        command => 'apt-get -y install gcc build-essential';

    'install python-pip':
        command => 'apt-get -y install python-pip';

    'install python-dev':
        command => 'apt-get -y install python-dev';

    'install python-setuptools':
        command => 'apt-get -y install python-setuptools';

    'update hosts':
        command => '/vagrant/provision/shell/network.sh',
        require => File['/vagrant/provision/shell/network.sh'];

}

file { 
    '/vagrant/provision/shell/network.sh' :
        ensure => present,
        owner => "vagrant",
        group => "vagrant",
        mode => "0777",
        source => '/vagrant/provision/shell/network.sh';
}
