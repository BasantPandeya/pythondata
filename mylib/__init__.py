from os.path import dirname, basename, join, isfile
import glob

load_file = glob.glob(join(dirname(__file__), "*.py"))

__all__ = [basename(file)[:-3] for file in load_file
           if isfile(file) and not file.endswith('__init__.py')
           ]

# print(load_file)
# print(__all__)


