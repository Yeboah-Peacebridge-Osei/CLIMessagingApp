FROM ubuntu:latest

WORKDIR /

# Copy everything in the current directory to the root directory of the image
COPY . .

# Install Python 3.7 and pip
RUN apt-get update && \
    apt-get install -y python3 && \
    apt install -y python3-pip && \
    pip3 install virtualenv && \
    python3 -m virtualenv venv && \
    /bin/bash -c "source venv/bin/activate" && \
    pip3 install -r requirements.txt

# Set the default command to activate the virtual environment and run the app
CMD [ "/bin/bash"]
