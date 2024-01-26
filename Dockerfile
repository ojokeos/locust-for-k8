# Use Python 3 base image
FROM python:3

# Install Locust using pip
RUN pip install locust

# Create a directory to store the Locust file
# RUN mkdir /locust-tasks

# Set the working directory
WORKDIR /locust-tasks/

# Copy the Locust file into the container
COPY ./locustfile.py /locust-tasks/
# COPY locustfile.py /locust-tasks/

# Expose the required Locust ports
EXPOSE 8089 5557 5558

# Run Locust with the specified file
CMD ["locust", "-f", "locustfile.py"]