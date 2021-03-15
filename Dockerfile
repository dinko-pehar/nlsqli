# Pull offical python alpine image to reduce size
FROM python:3.9-alpine
# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TERM xterm
RUN pip install requests rich
WORKDIR /tmp
COPY . .
# Install package as "executable"
RUN pip install .
ENTRYPOINT ["nlsqli"]
