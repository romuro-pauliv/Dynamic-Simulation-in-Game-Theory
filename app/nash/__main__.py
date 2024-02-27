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
    
    
    # Analysis |--------------------------------------------------------------|
    from graph.read_all_bin import ReadAllBin
    read_all_bin: ReadAllBin = ReadAllBin()
    
    from graph.analysis.dist import Dist
    dist: Dist = Dist(read_all_bin.data)
    dist.plot_payoff_dist()
    dist.plot_cumsum_dist()
    dist.plot_boxplot_cumsum_dist()
    dist.show()
    # |-----------------------------------------------------------------------|