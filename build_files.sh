echo "BUILD START"
python3.11 -m pip install -r reqirements.txt
python3.11 manage.py collectstatic
echo "BUILD END"