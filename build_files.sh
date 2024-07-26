echo "BUILD START"
python -m pip install -r reqirements.txt
python manage.py collectstatic
echo "BUILD END"