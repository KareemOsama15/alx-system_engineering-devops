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
