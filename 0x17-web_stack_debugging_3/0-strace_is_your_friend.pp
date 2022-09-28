#Fixes typo in an apache config file. Replaces 'phpp' by 'php'

exec {'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php ':
  path  => '/bin/'
}
