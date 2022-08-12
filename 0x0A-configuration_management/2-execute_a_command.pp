# Kill a process name "killmenow". Poor thing..
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
