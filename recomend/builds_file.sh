echo "BUILD START"
python2.7 -m pip install -r reaquirements.txt
python2.7 manage.py collectstatic --noinput --clear
echo "BUILD END"
