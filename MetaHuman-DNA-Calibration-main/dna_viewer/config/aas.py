class AdditionalAssemblyScript:
    def __init__(self,path = None,module_name = None, method= None,parmeter=None):
        self.path = path 
        self.module = module_name
        self.method = method if method else "run_after_assemble"
        self.parmeter = parmeter if parmeter else {}


