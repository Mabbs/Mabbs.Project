#!/system/bin/sh
mkdir -p ~/www/cgi-bin
cp ./wiki.cgi ~/www/cgi-bin/wiki.cgi
echo '<a href=/cgi-bin/wiki.cgi>Mabbs&Wiki</a>'>~/www/index.html
echo 'httpd -p 8080 -h ~/www
telnetd -p 2323 -l ~/www/cgi-bin/wiki.cgi'>/run
echo 'killall httpd
killall telnetd'>~/stop
chmod 755 ~/www/cgi-bin/wiki.cgi
chmod 755 ~/www/index.html
chmod 755 ~/run
chmod 755 ~/stop
~/www/cgi-bin/wiki.cgi