# base image
FROM python:3.9-alpine

# set working directory
WORKDIR /app

# copy app files
COPY requirements.txt .
COPY app.py .
COPY templates templates/
COPY static static/

# install dependencies
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# set environment variables
ENV FLASK_APP app.py
ENV FLASK_ENV production
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000

# expose port
EXPOSE 5000

# run app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
