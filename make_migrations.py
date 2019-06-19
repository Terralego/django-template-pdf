import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_template_pdf.settings")
    from django.core.management import execute_from_command_line
    args = sys.argv + ["makemigrations", "template_pdf"]
    execute_from_command_line(args)
