#!/bin/bash
rm -rf /var/www/html/report.html
ls /var/log/httpd/*  | grep access_log- | xargs cat > /tmp/access_log.txt
cat /var/log/httpd/access_log >> /tmp/access_log.txt
/bin/goaccess -a -g -f /tmp/access_log.txt -o /var/www/html/report.html --real-time-html --log-format=COMBINED --ws-url goaccess
