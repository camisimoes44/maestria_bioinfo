# Instructions:
1. Create and activate a virtual environment 'venv' with Python 3
	a. python3 -m venv venv
	b. source venv/bin/activate
2. Install requirements:
	a. pip install -r requirements.txt
3. Configure variables in config.py
4. Run Dash:
	a. Development: python index.py
	b. Production: gunicorn index:server
