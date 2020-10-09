# Web application
## Information
Dash multipage app with login.
Based in Russell Romney's *dash-auth-flow* (https://github.com/russellromney/dash-auth-flow).
Use web services from server.

## Deploy:
1. Create and activate a virtual environment 'venv' with Python 3
	1. `python3 -m venv venv`
	2. `source venv/bin/activate`
2. Install requirements:
	- `pip install -r requirements_dash-auth-flow.txt`
	- `pip install -r requirements.txt`
3. Create config from example:
    - `cp config.example.py config.py`
4. Configure variables in config.py
5. Run Dash:
	- Development:
		- `python app.py`
	- Production:
		- `gunicorn --bind 0.0.0.0:8000 app:server`
