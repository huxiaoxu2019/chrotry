#!/bin/sh

timestamp=$(date +%s)
cp $HOME/Library/Application\ Support/Google/Chrome/Default/History ./history_db_${timestamp}
#sqlite3 -csv ./history_db_${timestamp} ".headers on" ".separator _--_--_" "select * from urls where title like '%one%' order by last_visit_time desc" > urls_${timestamp}.csv
