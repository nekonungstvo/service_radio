FROM python:3.6
ENV IS_PROD 1
RUN apt update && apt install -y gcc build-essential libshout3
WORKDIR /usr/src/app
COPY . .
RUN python -m pip install -U .
CMD ["radio"]
EXPOSE 8080