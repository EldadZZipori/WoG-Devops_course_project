FROM python:3-alpine
RUN mkdir dev_files
RUN cd dev_files
WORKDIR dev_files
ADD . ./
RUN pip install selenium
RUN pip install flask
RUN pip pymysql
CMD python MainScores.py 
