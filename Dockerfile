# Use Python 3.12 base image
FROM python:3.12

# Define environment variable with modern format
ENV HOMELAKE=/personal-assistant

# Set working directory
WORKDIR $HOMELAKE

# Copy current directory contents into the container
COPY . .

# Install required Python packages
RUN pip install -r requirements.txt

# Expose port 3000 for the application
EXPOSE 3000

# Specify the command to run the application
ENTRYPOINT ["python", "menu.py"]
