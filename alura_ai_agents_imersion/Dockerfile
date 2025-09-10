FROM debian:bookworm-slim

ARG GEMINI_KEY

ENV GEMINI_KEY=${GEMINI_KEY}

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN pip install langchain --break-system-packages
RUN pip install langchain-google-genai --break-system-packages
RUN pip install google-generativeai --break-system-packages

CMD while : ; do sleep 1000; done