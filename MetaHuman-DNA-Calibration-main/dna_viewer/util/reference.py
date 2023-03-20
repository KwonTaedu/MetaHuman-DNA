from ..reader.geometry import Geometry

def get_geometry_reader(mesh_index, dna_path = None) :
    return Reference.get_geometry_reader(mesh_index=mesh_index, dna_path=dna_path)

def set_geometry_reader(dna_path, geometry_reader):
    return Reference.set_geometry_reader(dna_path=dna_path, geometry_reader=geometry_reader)


class Reference:
    geometry_readers= {}

    @staticmethod
    def get_geometry_reader(mesh_index, dna_path = None):

        if dna_path is None:  # defaults to first one
            geometry_readers_for_dna = next(iter(Reference.geometry_readers.values()))
            return geometry_readers_for_dna[mesh_index]
        return Reference.geometry_readers[dna_path][mesh_index]

    @staticmethod
    def set_geometry_reader(dna_path, geometry_reader):

        if dna_path not in Reference.geometry_readers:
            Reference.geometry_readers[dna_path] = []

        Reference.geometry_readers[dna_path].append(geometry_reader)
