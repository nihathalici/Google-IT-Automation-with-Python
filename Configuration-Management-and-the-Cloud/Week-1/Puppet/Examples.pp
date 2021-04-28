# This block is saying that the package 'sudo' 
# should be present on every computer 
# where the rule gets applied.
class sudo {

  package { 'sudo':
    ensure => present,
  }
}

class sysctl {
  # Make sure the directory exists
  file { '/etc/sysctl.d':
    ensure => directory,
  } 
}
