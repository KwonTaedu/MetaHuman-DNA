class AdditionalAssemblyScript:
    def __init__(self,path = None,module_name = None, method="run_after_assemble" , parameter=None):
        self.path = path 
        self.module_name = module_name
        self.method = method if method else "run_after_assemble"
        self.parameter = parameter if parameter else {}

