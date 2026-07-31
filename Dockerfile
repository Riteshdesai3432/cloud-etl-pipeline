#use the official python image

FROM python:3.11-slim

#set working directory

WORKDIR /app

# copy requirements file

COPY requirements.txt .

#install python dependencies

RUN pip install --no-cache-dir -r requirements.txt

#copy the entire project

COPY . .

#run the ETL pipeline

CMD ["python", "-m", "scripts.main"]