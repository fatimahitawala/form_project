FROM python:3.10-slim
WORKDIR /app
COPY app.py ./
COPY requirements.txt ./
VOLUME /app/data  
RUN  apt update -y && apt install python3-pip -y && pip install --no-cache-dir -r requirements.txt
RUN  mkdir data 
EXPOSE 80 
CMD ["python", "app.py"]




