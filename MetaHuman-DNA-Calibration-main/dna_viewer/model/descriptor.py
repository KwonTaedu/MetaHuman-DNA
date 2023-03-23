class Descriptor:
    def __init__(self,name=None,archetype = None,gender=None,age=None,metadata=None,translation_unit=None,
                 rotation_unit=None,coordinate_system=None,lod_count=None,db_max_lod= None,db_complexity=None,db_name=None):

        self.name = name
        self.archetype = archetype
        self.gender = gender
        self.age = age
        self.metadata = metadata if metadata else {}
        self.translation_unit = translation_unit
        self.rotation_unit = rotation_unit
        self.coordinate_system = coordinate_system
        self.lod_count = lod_count
        self.db_max_lod = db_max_lod
        self.db_complexity = db_complexity
        self.db_name = db_name
