print("asd")
import logging
from ..model.behavior import Behavior as BehaviorModel
from ..model.definition import Definition as DefinitionModel
from ..model.descriptor import Descriptor as DescriptorModel
from ..model.dna import DNA as DNAModel
from ..model.geometry import Geometry as GeometryModel
from ..model.geometry import Mesh
print("start66") 
from ..reader.behavior import Behavior as BehaviorReader 
print("end")
from ..reader.definition import Definition as DefinitionReader 
from ..reader.descriptor import Descriptor as DescriptorReader 
from ..reader.geometry import Geometry as GeometryReader
from ..util.reader import Reader 
from ..util.reference import set_geometry_reader


def load_dna(dna_path = None):
    return DNA.load_dna(path = dna_path)

class DNA:
    @staticmethod
    def load_dna(path):
        logging.info("loading DNA" + path)
        reader = DNA(path)
        return reader.read()

    def __init__(self, path):
        self.stream_reader = Reader.create_stream_reader(path)
        self.path = path
        self.dna = None

    def read(self):
        self.dna = DNAModel(path=self.path)
        self.read_base()
        self.load_meshes()
        return self.dna

    def read_base(self):
        self.dna.descriptor = self.read_descriptor()
        self.dna.definition = self.read_definition()
        self.dna.behavior = self.read_behavior()
        self.dna.geometry = GeometryModel()

    def load_meshes(self):
        for lod in range(self.dna.descriptor.lod_count):
            for mesh_index in self.dna.definition.meshes.indices_for_lod[lod]:
                self.dna.geometry.meshes[mesh_index] = self.load_mesh(
                    mesh_index=mesh_index
                )

    def load_mesh(self, mesh_index):
        return self.read_geometry_for_mesh_index(mesh_index=mesh_index)

    def read_descriptor(self):
        return DescriptorReader(self.stream_reader).read()

    def read_definition(self):
        return DefinitionReader(self.stream_reader).read()

    def read_behavior(self):
        return BehaviorReader(self.stream_reader).read()

    def read_geometry_for_mesh_index(self, mesh_index):
        reader = GeometryReader(stream_reader=self.stream_reader, mesh_index=mesh_index)
        set_geometry_reader(dna_path=self.path, geometry_reader=reader)
        return reader.read()
