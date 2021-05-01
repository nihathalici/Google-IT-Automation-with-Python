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



# In this example, we're using a file resource to configure the contents of etc/timezone, a file,
# that's used in some Linux distributions to determine the time zone of the computer.
# This resource has three attributes. First, we explicitly say that this will be a file instead of a directory or a symlink
# then we set the contents of the file to the UTC time zone.
# Finally, we set the replace attribute to true, which means that the contents of the file will be replaced
# even if the file already exists

class timezone {

  file { 'etc/timezone':
    ensure => file,
    content => "UTC\n",
    replace => true,
  }
}
