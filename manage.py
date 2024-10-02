
import os
import sys
import subprocess
import socket

def check_opensearch_running():
    try:
        socket.create_connection(("localhost", 9200))
        print("OpenSearch is already running.")
    except socket.error:
        print("Starting OpenSearch...")
        subprocess.Popen(["/home/swayam/opensearch-2.9.0/bin/opensearch"], stdout=subprocess.PIPE)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rapidious_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    check_opensearch_running()  
    main()
