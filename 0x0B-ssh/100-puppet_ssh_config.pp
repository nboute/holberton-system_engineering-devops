# Configure ssh server to not use a password

file_line { 'Remove Password Auth':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no'
}

file_line { 'Set default path for ssh keys':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school'
}
