FROM python:3-slim

RUN pip install flask

ADD main.py /main.py
RUN chmod u+x /main.py

ENTRYPOINT ["/main.py"]
