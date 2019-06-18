FROM ubuntu:19.04

RUN apt-get update && \
    apt-get install python3-pip -y && \
    apt-get install libreoffice -y && \
    apt-get install git-core -y && \
    rm -r /var/lib/apt/lists/* && \
    pip3 install -e git+https://github.com/Terralego/django-template-pdf.git@master#egg=django-template-pdf

CMD bash -c "(soffice --nologo --nodefault \
            --nofirststartwizard --invisible \
            --headless --norestore --accept='socket,host=localhost,port=2002,tcpNoDelay=1;urp;StarOffice.ComponentContext' &) && \
            (convertor --host 0.0.0.0)"
