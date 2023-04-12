FROM python:3.8

    #set a directory fro the application
    WORKDIR /usr/src/app 

    # copy all the files to the container
    COPY . .

    # install dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    #tell the port number the container should expose
    EXPOSE 5000

    #run the CMD
    CMD ["python", "./app.py"]