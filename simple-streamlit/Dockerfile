FROM public.ecr.aws/docker/library/python:3.9-slim

RUN pip3 install --upgrade pip
RUN apt update && apt install unattended-upgrades -y
RUN apt-get update

# Exposing Default Port
EXPOSE 8501

# Set Working Directory
WORKDIR /simple-streamlit

# Copy Function Code

COPY /app.py app.py
COPY /unhrc_offices.csv unhrc_offices.csv

# Install functions dependencies from requirements.txt
RUN pip3 install wheel
COPY /requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Entrypoint for app
CMD [ "streamlit" , "run" , "app.py", "--server.address=0.0.0.0" ]
