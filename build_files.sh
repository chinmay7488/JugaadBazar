echo "BUILD START"
pip install -r reqirements.txt
python3.11 manage.py makemigration
python3.11 manage.py migrate
python3.11 manage.py collectstatic
echo "BUILD END"