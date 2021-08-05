FROM python:3.5

RUN mkdir /app

RUN pip install numpy

RUN pip install pandas

copy src.py  /app

WORKDIR /app

EXPOSE 80
EXPOSE 3088
EXPOSE 8080
EXPOSE 8066

CMD ["python", "src.py"]
