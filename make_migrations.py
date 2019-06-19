import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "template_pdf.tests.settings")
    from django.core.management import execute_from_command_line
    args = sys.argv + ["makemigrations", "template_pdf"]
    execute_from_command_line(args)
