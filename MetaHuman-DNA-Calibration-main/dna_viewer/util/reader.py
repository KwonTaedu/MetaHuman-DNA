import dna

class Reader:

    @staticmethod
    def create_stream_reader(dna_path):
        stream = dna.FileStream(
            dna_path, dna.FileStream.AccessMode_Read, dna.FileStream.OpenMode_Binary
        )

        reader = dna.BinaryStreamReader(stream, dna.DataLayer_All)
        reader.read()
        if not dna.Status.isOk():
            status = dna.Status.get()
            raise RuntimeError("Error loading DNA:"+ status.message)
        return reader