import sys
from argparse import ArgumentParser
from multiprocessing import Process
from socket import SHUT_WR
from socketserver import StreamRequestHandler, TCPServer

from magic import from_buffer
from weasyprint import HTML

from template_pdf.pdf_convertor.convertor import Convertor, logger
from template_pdf.utils import LibreOfficeMimeTypes


class PdfGeneratorHandler(StreamRequestHandler):

    def handle(self):
        self.data = self.rfile.read()
        mime_type = from_buffer(self.data, mime=True)
        if LibreOfficeMimeTypes.is_member(mime_type):
            pdf = self.server.convertor.convert(self.data)
        elif mime_type == 'text/html':
            pdf = HTML(string=self.data.decode()).write_pdf()
        else:
            logger.error('Mime type unknown: %s' % mime_type)
            sys.exit(2)
        self.wfile.write(pdf)
        self.request.shutdown(SHUT_WR)


class PdfGeneratorTcpServer(TCPServer):

    def __init__(self, server_address, RequestHandlerClass, convertor, bind_and_activate=True):
        self.convertor = convertor
        super().__init__(server_address, RequestHandlerClass, bind_and_activate=bind_and_activate)


def run_server(host, port, libreoffice_host, libreoffice_port):
    """
    Takes as parameters the host and port with which the server is to be run, as well as the host
    and port of the soffice server, and then starts the server.
    """
    convertor = Convertor(server=libreoffice_host, port=libreoffice_port)
    server = PdfGeneratorTcpServer((host, port), PdfGeneratorHandler, convertor)
    logger.info('The server is running.')
    server.serve_forever()


def main():
    parser = ArgumentParser()

    parser.add_argument('--host', default='localhost', help='The server host.')
    parser.add_argument('--port', default=9999, type=int, help='The server port.')

    libreoffice_group = parser.add_argument_group('Libreoffice')
    libreoffice_group.add_argument('--libreoffice-host', default='localhost',
                                   help='The libreoffice server host.')
    libreoffice_group.add_argument('--libreoffice-port', default='2002',
                                   help='The libreoffice server port.')

    parsed_data = parser.parse_args()

    exit_code = -1

    while exit_code != 0 and exit_code != 1:
        p = Process(target=run_server, args=(parsed_data.host, parsed_data.port,
                                             parsed_data.libreoffice_host,
                                             parsed_data.libreoffice_port))
        p.start()
        p.join()
        exit_code = p.exitcode

    if exit_code:
        logger.error('The server crashed.')
        sys.exit(1)
    else:
        logger.info('The server closed.')
        sys.exit(0)


if __name__ == "__main__":
    main()
