# will make 2000 requests to my server with 100 requests
exec 'change size the requests': {
	command => '/bin/sed -i "s/15/30000/g" /etc/default/nginx | service nginx restart'
     }
