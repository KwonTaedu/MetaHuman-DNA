class AdditionalAssemblyScript:
    def __init__(self,path = None,module_name = None, method="run_after_assemble",parmeter={}):
        self.path = path
        self.module = module_name
        self.method = method
        self.parmeter = parmeter


