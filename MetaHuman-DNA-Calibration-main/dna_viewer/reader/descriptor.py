print("descriptor")
#from dna import BinaryStreamReader

from ..model.descriptor import Descriptor as DescriptorModel


class Descriptor:

    def __init__(self, stream_reader):
        self.reader = stream_reader
        self.descriptor = None

    def read(self):
        self.descriptor = DescriptorModel()

        self.add_basic_data()
        self.add_metadata()
        self.add_geometry_data()
        self.add_db_data()

        return self.descriptor

    def add_basic_data(self):
        self.descriptor.name = self.reader.getName()
        self.descriptor.archetype = self.reader.getArchetype()
        self.descriptor.gender = self.reader.getGender()
        self.descriptor.age = self.reader.getAge()

    def add_metadata(self):
        for i in range(self.reader.getMetaDataCount()):
            self.descriptor.metadata[
                self.reader.getMetaDataKey(i)
            ] = self.reader.getMetaDataValue(self.reader.getMetaDataKey(i))

    def add_geometry_data(self):
        self.descriptor.translation_unit = self.reader.getTranslationUnit()
        self.descriptor.rotation_unit = self.reader.getRotationUnit()
        coordinate_system = self.reader.getCoordinateSystem()
        self.descriptor.coordinate_system = (
            coordinate_system.xAxis,
            coordinate_system.yAxis,
            coordinate_system.zAxis,
        )

    def add_db_data(self):
        self.descriptor.lod_count = self.reader.getLODCount()
        self.descriptor.db_max_lod = self.reader.getDBMaxLOD()
        self.descriptor.db_complexity = self.reader.getDBComplexity()
        self.descriptor.db_name = self.reader.getDBName()
