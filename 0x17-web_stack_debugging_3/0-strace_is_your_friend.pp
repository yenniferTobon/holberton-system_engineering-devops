# change .phpp to php
exec { 'change phpp':
  command  => 'sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php && sudo service apache2 restart',
  provider => shell,
}
