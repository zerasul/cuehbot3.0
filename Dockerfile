FROM python:slim
RUN pip install pipenv
RUN mkdir cuehbot
WORKDIR /cuehbot
COPY . /cuehbot
RUN pipenv install
CMD [ "pipenv", "run", "startbot" ]