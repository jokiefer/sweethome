#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
NOCOLOR='\033[0m'
/opt/sweethome/.bash_scripts/wait_db.sh

echo "django migrate"
python manage.py migrate

if [ $? != 0 ]; 
then
  exit 1
  printf "${RED}failed to migrate database${NOCOLOR}\n"
else
  printf "${GREEN}database migrations applied${NOCOLOR}\n"
fi

echo 'Application server is starting now.'

exec "$@"