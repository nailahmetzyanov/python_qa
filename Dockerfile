FROM python:3.9-alpine

RUN pip install -U pip

RUN pip install -r requirements.txt

CMD python3 -m pytest tests/test_auth_page.py --executor 0.0.0.0:4444