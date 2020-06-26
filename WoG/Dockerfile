FROM python:alpine
RUN mkdir dev
RUN cd dev
WORKDIR dev
ADD . ./
RUN pip install selenium
CMD python MainScores.py 
