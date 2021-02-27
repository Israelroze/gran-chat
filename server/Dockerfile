# python container
FROM python:3.8.2-slim

# set the working dir
WORKDIR /gran-chat

# copy the project content into workdir
COPY .. /gran-chat

# install dependencies
RUN pip install -r requirments.txt

# run the server
CMD ["python","run.py"]