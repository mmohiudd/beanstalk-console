import 'default.pp'

exec { 
	'install beanstalkd':
    	command => 'apt-get -y install beanstalkd',
    	require => Exec['apt-get update'];

	# make sure beanstalkd is stopped - we will start it via supervisor
	"beanstalkd stop":
		command => '/etc/init.d/beanstalkd stop',
		require => Exec['install beanstalkd'];

	'install supervisor':
    	command => 'easy_install supervisor',
    	require => Exec['install python-setuptools'];
}

file { 
	'/etc/supervisord.conf':
		ensure => file,
		source => '/vagrant/provision/files/supervisord.conf',
		require => Exec['install supervisor'];
    
    '/etc/init/supervisor.conf':
        ensure => file,
        source => '/vagrant/provision/files/supervisor.conf',
        require => File['/etc/supervisord.conf'];
} 

service { 
	"supervisor":
		ensure => running,
		require => File['/etc/supervisord.conf', '/etc/init/supervisor.conf'];

}
