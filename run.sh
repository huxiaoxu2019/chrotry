#!/bin/sh
BASEPATH=$(cd `dirname $0`; pwd)
cp $HOME/Library/Application\ Support/Google/Chrome/Default/History $BASEPATH/history_db
python $BASEPATH/migration.py $BASEPATH/history_db
