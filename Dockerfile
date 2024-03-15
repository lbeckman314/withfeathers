FROM python

WORKDIR /app
COPY . /app/withfeathers

RUN python --version
RUN which python3

RUN ls -la /app        # List the contents of /app
RUN python -m venv /app/venv
RUN . /app/venv/bin/activate
RUN pip install -r /app/withfeathers/requirements.txt

# Set environment variables
ENV FLASK_APP=withfeathers/server.py

# Make port 8000 available to the world outside this container
EXPOSE 8000

ENV VIRTUAL_ENV /app/venv
ENV PATH /app/venv/bin:$PATH

# Run the Flask development server when the container launches
CMD ["gunicorn", "--chdir", "withfeathers/withfeathers", "-b", "0.0.0.0:8000", "server:app"]

