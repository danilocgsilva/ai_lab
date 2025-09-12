FROM debian:bookworm-slim

ARG GEMINI_KEY

ENV GEMINI_KEY=${GEMINI_KEY}

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN pip install Flask --break-system-packages
RUN pip install flask-cors --break-system-packages
RUN pip install pip-tools --break-system-packages

# CMD flask run --host=0.0.0.0 --debug
CMD while : ; do sleep 1000; done
