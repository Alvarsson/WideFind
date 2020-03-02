# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

#
ENV FLASK_APP app.py
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
#CMD ["flask", "run"]
