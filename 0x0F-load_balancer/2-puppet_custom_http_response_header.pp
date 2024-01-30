# Add a custom HTTP header with Puppet

exec { 'update packages':
    provider => shell,
    command  => 'sudo apt-get update',
    before   => Exec['install nginx'],
}

exec { 'install nginx':
    provider => shell,
    command  => 'sudo apt-get -y install nginx',
    before   => Exec['add header'],
}

exec { 'add header':
    provider => shell,
    command  => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
    before   => Exec['retsart nginx']
}

exec { 'retsart nginx':
    provider => shell,
    command  => 'sudo service nginx retsart'
}

file_line { ' creating a custom HTTP header response':
  path  => '/etc/nginx/sites-available/default',
  line  => '		add_header X-Served-By $hostname;',
	after  => '^\s*server\s*\{',
  ensure => present,
}