# Use the official Alpine base image with Python
FROM python:3.11-alpine

# Install dependencies and Java (required for Jenkins agent)
RUN apk update && \
    apk add --no-cache openjdk11-jdk curl && \
    apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    build-base \
    && pip install --upgrade pip \
    && pip install pylint flake8 black pytest

# Create a Jenkins user
RUN adduser -D jenkins
USER jenkins

# Set the working directory
WORKDIR /home/jenkins

# Download the Jenkins agent JAR file
RUN curl -o agent.jar -L "https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/4.13/remoting-4.13.jar"

#RUN curl -o agent.jar -L "https://repo.jenkins-ci.org/public/org/jenkins-ci/main/agent/4.0.2/agent-4.0.2.jar"

# Define the entrypoint (Jenkins agent JAR is typically launched)
ENTRYPOINT ["java", "-jar", "agent.jar"]
