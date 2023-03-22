import logging

from ..model.dna import DNA
from ..util.error import DNAViewerError
from ..util.mesh import get_mesh_indices_containing_string, get_mesh_lods


def print_meshes(dna):

    mesh_indices_by_lods = get_mesh_lods(dna)

    for lod, mesh_indices in enumerate(mesh_indices_by_lods):
        logging.info("LOD_"+lod)
        for mesh_index in mesh_indices:
            logging.info("\t"+mesh_index+"->"+dna.get_mesh_name(mesh_index))


def print_mesh_indices_containing_string(mesh_name_part, lod, dna):

    try:
        results = get_mesh_indices_containing_string(mesh_name_part, lod, dna)
        for mesh_index in results:
            logging.info("\t"+dna.get_mesh_name(mesh_index)+"->"+mesh_index)
    except DNAViewerError as e:
        logging.error(e)
        raise DNAViewerError(e)
    except Exception as e:
        logging.error("Unhandled exception, "+e)
        raise DNAViewerError(e)
