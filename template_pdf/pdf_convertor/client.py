from io import BytesIO
from socket import AF_INET, SHUT_WR, SOCK_STREAM, socket


def to_pdf(host, port, content):
    """
    Takes the host and port of the server as well as the contents of the LibreOffice document as
    parameters, and returns the associated pdf as a byte object.
    """
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, port))
    buffer = BytesIO(content)
    s.sendfile(buffer)
    s.shutdown(SHUT_WR)
    pdf_content = s.makefile(mode='rb').read()
    s.close()
    return pdf_content
