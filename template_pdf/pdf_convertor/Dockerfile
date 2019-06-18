FROM ubuntu:19.04

RUN apt-get update && \
    apt-get install python3-pip -y && \
    apt-get install libreoffice -y && \
    rm -r /var/lib/apt/lists/* && \
    mkdir /src

WORKDIR /src
COPY ./server.py /src/
COPY ./convertor /src/convertor

CMD bash -c "(soffice --nologo --nodefault \
            --nofirststartwizard --invisible \
            --headless --norestore --accept='socket,host=localhost,port=2002,tcpNoDelay=1;urp;StarOffice.ComponentContext' &) && \
            (python3 ./server.py --host 0.0.0.0 --libreoffice-host localhost)"
