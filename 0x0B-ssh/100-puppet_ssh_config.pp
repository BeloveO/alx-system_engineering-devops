# Using puppet for the client configuration
include stdlib

file_line { 'No passwd auth':
  ensure => 'present',
  path   => 'etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication'
}

file_line { 'Identity_file':
  ensure => 'present',
  path   => 'etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile'
}
