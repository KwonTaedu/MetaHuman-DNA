import logging

from ..config.character import Character
from ..util.error import DNAViewerError
from ..util.import_util import Import


class AdditionalAssemblyScript:

    @staticmethod
    def run_additional_assembly_script(config):

        if config.aas:
            logging.info("running after assembly script...")
            AdditionalAssemblyScript.run_script(
                config.aas.module_name,
                config.aas.path,
                config.aas.method,
                config.aas.parameter,
            )

    @staticmethod
    def run_script(module_name, path, method, parameter = None):

        try:
            script = Import.source_py_file(module_name, path)
            script_method = getattr(script, method)
            if parameter:
                script_method(parameter)
            else:
                script_method()
        except Exception as e:
            raise DNAViewerError("Can't run aas script. Reason: "+e)
        

