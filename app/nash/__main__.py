# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app/__main__.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from resources.generate_data_dir    import GenDataDir
from core.multiprocessing           import CoreChunk
from simulation.nash                import simulate
# |--------------------------------------------------------------------------------------------------------------------|


if __name__ == "__main__":
    generate_data_dir: GenDataDir = GenDataDir()
    generate_data_dir.delete(), generate_data_dir.create()
    
    
    core_chunk: CoreChunk = CoreChunk()
    core_chunk.define_function(simulate)
    core_chunk.run()