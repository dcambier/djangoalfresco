from pathlib import Path
from functools import partial
from io import DEFAULT_BUFFER_SIZE
from .models import Document

def clear_database():
    for document in Document.objects.all():
        document.file.delete()
        document.delete()

def get_file_content(path):
    """given a path, return an iterator over the file
    that lazily loads the file
    """
    path = Path(path)
    with path.open('rb') as file:
        reader = partial(file.read1, DEFAULT_BUFFER_SIZE)
        file_iterator = iter(reader, bytes())
        for chunk in file_iterator:
            for byte in chunk:
                yield byte
        
def percentage(percent, whole):
  return (percent * whole) / 100.0