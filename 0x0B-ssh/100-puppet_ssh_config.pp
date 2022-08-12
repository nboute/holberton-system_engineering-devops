# Configure ssh server to not use a password

file_line { 'Delete line password auth':
  ensure => absent,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication yes'
}

file_line { 'Disable line password auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
}

file_line { 'Set path for ssh key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school'
}
