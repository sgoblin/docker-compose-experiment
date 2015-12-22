FROM quay.io/sgoblin/base-alpine

WORKDIR /root
RUN apk add python3 ca-certificates wget && wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && rm get-pip.py
ADD app /root
RUN pip install -Ur requirements.txt && ls
CMD gunicorn -b 0.0.0.0:8000 app:app
