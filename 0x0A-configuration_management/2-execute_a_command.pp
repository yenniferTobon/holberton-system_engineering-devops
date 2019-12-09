# create a manifest that kills a process named killmenow
exec { 'pkil_process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin'
}
