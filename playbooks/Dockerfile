FROM PYTHON:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt


EXPOSE 80

CMD ['python','test_file.py']


# docker build -t test_file .

# docker run -p 4000:80 test_file

# docker stop container_name_or_id