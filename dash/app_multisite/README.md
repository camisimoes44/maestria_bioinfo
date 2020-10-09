# Instructions:
1. Create and activate a virtual environment 'venv' with Python 3
	1. `python3 -m venv venv`
	2. `source venv/bin/activate`
2. Install requirements:
	- `pip install -r requirements.txt`
3. Configure variables in config.py
4. Run Dash:
	- Development:
		- `python index.py`
	- Production:
		- `gunicorn --bind 0.0.0.0:8000 index:server`
