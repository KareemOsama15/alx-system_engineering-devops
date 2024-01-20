package { 'python3-pip':
    ensure => 'installed',
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip',
    require  => Package['python3-pip'],
}

package { 'Werkzeug':
    ensure   => '2.1.1',
    provider => 'pip',
    require  => Package['python3-pip'],
}
