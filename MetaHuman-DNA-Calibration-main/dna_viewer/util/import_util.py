import imp
import os

from ..util.error import DNAViewerError

class Import:
    @staticmethod
    def source_py_file(name, path):

        path_obj = os.path.abspath(path)
        if (
            path
            and os.path.exists(path)
            and os.path.isfile(path)
            and os.path.splitext(path)[1] == ".py"
        ):
            module = imp.load_source(name, path)

            return module
        raise DNAViewerError("File"+ path+" is not found!")
    
 