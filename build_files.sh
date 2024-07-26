echo "BUILD START"
python3.9 pip install -r reqirements.txt
python3.9 manage.py makemigration
python3.9  manage.py migrate
python3.9  manage.py collectstatic
echo "BUILD END"