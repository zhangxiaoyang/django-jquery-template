#/usr/bin/env bash
printColorTitle() {
    title=$1
    echo -e "\033[0;33;1m${title}\033[0m"
}

printColorTitle "Init env"
virtualenv env
source env/bin/activate

printColorTitle "Install requirement"
pip install -r requirement.txt

cd ui

printColorTitle "Make data"
python manage.py syncdb
python makedata.py

printColorTitle "Generate key"
SECRET_KEY="$( echo -e "from django.utils.crypto import get_random_string\nchars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'\nprint(get_random_string(50,chars))" | ../env/bin/python )"
SECRET_KEY=$(sed 's/\&/\\\&/g' <<< $SECRET_KEY)
sed -i -e "s/INSERT_SECRET_KEY/$SECRET_KEY/g" ui/settings.py
