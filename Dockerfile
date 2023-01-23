FROM python:3.8
ADD . .

RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
CMD [ "python","app.py" ]