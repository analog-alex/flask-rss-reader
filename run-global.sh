echo 'Launching Flask Application (Python 3.7)'

export FLASK_APP=main.py
export FLASK_ENV=production

flask run -h 0.0.0.0