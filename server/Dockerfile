# python container
FROM python:3.8.2-slim

# set the working dir
WORKDIR /app

# copy the project content into workdir
COPY ./server /app

# install dependencies
RUN pip install -r requirments.txt

# run the server
CMD ["python","run.py"]