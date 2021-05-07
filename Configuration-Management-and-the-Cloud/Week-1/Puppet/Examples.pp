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



class ntp {
  package { 'ntp':
    ensure => latest,
  }
  file { '/etc/ntp.conf':
    source => 'puppet:///modules/ntp/ntp.conf'
    replace => true,
  }
  service { 'ntp':
    enable => true,
    ensure => running,
  }
}


# This piece of code is using the is-virtual fact
# together with a conditional statement to decide
# whether the smartmontools package should be installed or purged.


if $facts['is_virtual'] {
  package { 'smartmontools':
    ensure => purged,

  }
} else {
  package { 'smartmontools':
    ensure => installed,
  }
}


# This resource ensures that the /etc/issue file
# has a set of permissions and a specific line in it.

file { '/etc/issue':
  mode    => '0644',
  content => "Internal system \l \n",
}


# Using the onlyif attribute, we specified that this command
# should be executed only if the file that we want to move exists.

exec { 'move example file':
  command => 'mv /home/user/example.txt /home/user/Desktop',
  onlyif  => 'test -e /home/user/example.txt',
}
