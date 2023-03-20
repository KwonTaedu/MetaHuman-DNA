from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader
from pathlib import Path


from ..util.error import DNAViewerError


class Import:

    @staticmethod
    def source_py_file(name, path):

        path_obj = Path(path.strip())
        if (
            path
            and path_obj.exists()
            and path_obj.is_file()
            and path_obj.suffix == ".py"
        ):
            spec = spec_from_loader(name, SourceFileLoader(name, path))
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        raise DNAViewerError(f"File {path} is not found!")
