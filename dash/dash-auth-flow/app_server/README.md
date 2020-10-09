# Server
## Information
Flask server with web services and persistence in MySQL.

## Requirements
Developed with:
- Python 3
- MySQL 8

## Deploy:
1. Create and activate a virtual environment 'venv' with Python 3
	1. `python3 -m venv venv`
	2. `source venv/bin/activate`
2. Install requirements:
	- `pip install -r requirements.txt`
3. Configure variables in config.py
4. Run Dash:
	- Development:
		- `python app_server.py`
	- Production:
		- `gunicorn --bind 0.0.0.0:5000 app_server:server`
