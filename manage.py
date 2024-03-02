#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def custom():
    """sync between react & django"""
    if sys.argv[1] == 'sync':
        subprocess.run("rm -rf dist", shell=True, check=True, cwd="frontend")
        subprocess.run("npm run build", shell=True, check=True, cwd="frontend")
        subprocess.run("python manage.py collectstatic --noinput", shell=True, check=True, cwd=".")
        subprocess.run("python manage.py runserver", shell=True, check=True, cwd=".")
        print("----------------\nSUCCESS\n----------------")


if __name__ == '__main__':
    custom()
    main()
