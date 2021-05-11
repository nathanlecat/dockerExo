FROM python:3.8
WORKDIR /PyAPP
COPY requirements.txt /PyAPP
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /PyAPP
ENTRYPOINT ["python"]
CMD ["JustePrix.py"]
