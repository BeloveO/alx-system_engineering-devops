# Install flask from pip3 using Puppet

package {'flask':
  ensure   => '2.1.1',
  provider => 'pip3',
}
