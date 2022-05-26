FROM centos
RUN yum install python3 -y
RUN pip3 install numpy pandas sklear
COPY taskLR.py taskLR.py
COPY dataset.csv dataset.csv
ENTRYPOINT ["python3" , "taskLR.py"]
