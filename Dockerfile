FROM python:3.7.3-slim

# RUN apt-get update
# RUN apt-get update && apt-get install -y libpq-dev

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # lint
# RUN pip install --upgrade pip


ENV ARGO_HOME=/opt/dtv

RUN mkdir $ARGO_HOME
# set work directory
WORKDIR $ARGO_HOME

# COPY main $ARGO_HOME/main
# COPY app.py $ARGO_HOME
COPY requirements.txt $ARGO_HOME

RUN pip install -r requirements.txt

# CMD ["gunicorn", "--workers" ,"10", "--max-requests", "3", "-b", "0.0.0.0:8000", "app:app", "--timeout", "10800"]
