#!/bin/sh
BASEPATH=$(cd `dirname $0`; pwd)
cp $HOME/Library/Application\ Support/Google/Chrome/Default/History $BASEPATH/history_db
/usr/local/bin/python $BASEPATH/migration.py $BASEPATH/DB $BASEPATH/history_db
