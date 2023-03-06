FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 7844
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7844"]