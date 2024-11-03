FROM python:3.11.5
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY src ./src
EXPOSE 8083

WORKDIR /src

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["python", "server.py"]