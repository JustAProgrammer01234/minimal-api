FROM python:latest 
WORKDIR /app 
COPY . /app
RUN pip3 install fastapi uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]