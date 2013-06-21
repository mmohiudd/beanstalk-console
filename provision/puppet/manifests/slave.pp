import 'default.pp'

exec { 
    'install libzmq-dev':
        command => 'apt-get -y install libzmq-dev';

    'install pyzmq':
        command => 'easy_install pyzmq',
        require => Exec['install libzmq-dev'];

    'install circus':
        command => 'pip install circus',
        require => Exec['install libzmq-dev', 'install python-pip', 'install pip-requirements', 'install pyzmq'];

    'install libevent-dev':
        command => 'apt-get -y install libevent-dev';

    'install circus-web':
        command => 'pip install circus-web',
        require => Exec['install libevent-dev', 'install python-pip', 'install circus'];

    'install stressapptest':
        command => '/vagrant/provision/shell/stressapptest.sh',
        require => File['/vagrant/provision/shell/stressapptest.sh'];
}

file {
    '/etc/circus.ini':
        ensure => file,
        source => '/vagrant/provision/files/circus.ini',
        require => Exec['install circus'];

    '/etc/init/circus.conf':
        ensure => file,
        source => '/vagrant/provision/files/circus.conf',
        require => File['/etc/circus.ini'];

    '/vagrant/provision/shell/stressapptest.sh' :
        ensure => present,
        owner => "vagrant",
        group => "vagrant",
        mode => "0777",
        source => '/vagrant/provision/shell/stressapptest.sh';        
}

service { 'circus':
    ensure => running,
    require => File['/etc/init/circus.conf']
}