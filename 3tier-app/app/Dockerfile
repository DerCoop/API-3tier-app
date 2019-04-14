# Builds a base Docker image to run a Flask application using the uWSGI
# application server.
#
#  (1) Declare a CMD instruction to start the uWSGI application server.
#      For example:
#        CMD ["uwsgi", "--http :5000 --wsgi-file app.py --callable app --processes 2 --threads 4"]
#
#        If running behind a webserver using the uwsgi protocol (like nginx)
#        then use `--socket` instead of `--http`.
#
#      For more info, see:
#        https://uwsgi-docs.readthedocs.org/en/latest/WSGIquickstart.html
#        http://uwsgi-docs.readthedocs.org/en/latest/Nginx.html
#
#  (2) Expose the port uWSGI will run on.
#      For example:
#        EXPOSE 5000
#
FROM ubuntu:18.04
MAINTAINER Cooper <onkelcoop@gmail.com>

# Get and install required packages.
RUN apt-get update && apt-get install -y \
    build-essential \
    python-dev \
    python-pip

# Install required dependencies (includes Flask and uWSGI)
ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# copy te app dir to the comtainer, for devel purposes this will be overwritten
# later by a bind mount
ADD . /var/www/app

WORKDIR /var/www/app
# Expose the port where uWSGI will run
EXPOSE 5000

# If running this app behind a webserver using the uwsgi protocol (like nginx),
# then use --socket.  Otherwise run with --http to run as a full http server.
#CMD ["uwsgi", "--http", ":5000",         "--wsgi-file", "app.py", "--callable", "app", "--processes",  "2", "--threads", "4"]
CMD ["uwsgi", "--socket", "0.0.0.0:5000", "--wsgi-file", "app.py", "--callable", "app", "--processes",  "2", "--threads", "4"]
