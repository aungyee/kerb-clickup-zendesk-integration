FROM python:3.9

WORKDIR /kerb_clickup_zendesk_integration

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY / .

CMD ["python","./app.py"]