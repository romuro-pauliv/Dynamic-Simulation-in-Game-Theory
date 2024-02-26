# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        app/core/multiprocessing.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import multiprocessing

from config.config_files import configfiles
from log.genlog import genlog

from typing import Callable
# |--------------------------------------------------------------------------------------------------------------------|


class CoreChunk(object):
    def __init__(self) -> None:
        """
        Initialize the CoreChunk instance.
        Args:
            cpu_off (int): Inform qnt of cpus offs
            processing_times (int): Qnt times to processing the function
        """
        cpu_off: int = int(configfiles.dot_ini['simulation']['simulate:cores']['core_off'])
        
        self.CPU                : int = multiprocessing.cpu_count()-cpu_off
        self.processing_times   : int = int(configfiles.dot_ini['simulation']['simulate:samples']['times'])
        
    def define_function(self, function: Callable[[None], None]) -> None:
        """
        Inform the function to be processed
        Args:
            function (Callable[[None], None]): The function
        """
        self.func: Callable[[None], None] = function
    
    def _generate_processes(self) -> None:
        """
        Generate the process list
        """
        self.processes: list[multiprocessing.Process] = []
        for _ in range(self.processing_times):
            self.processes.append(multiprocessing.Process(target=self.func))
        genlog.report(True, f"Generated [{len(self.processes)}] Process")
    
    def _split_in_chunks(self) -> list[list[multiprocessing.Process]]:
        """
        Split the process list in chunks
        Returns:
            list[list[multiprocessing.Process]]: Process list in chunks
        """
        return [self.processes[i:i+self.CPU] for i in range(0, len(self.processes), self.CPU)] 

    def _start_processes(self, process_list: list[multiprocessing.Process]):
        genlog.report(True, f"Starting [{len(process_list)}] child process...")
        for process in process_list:
            process.start()
    
    def _join_processes(self, process_list: list[multiprocessing.Process]):
        for process in process_list:
            process.join()
            process.close()
        genlog.report(True, f"Joined [{len(process_list)}] child process")
    
    def run(self) -> None:
        """
        Run with multiprocessing
        """
        self._generate_processes()
        chunks: list[list[multiprocessing.Process]] = self._split_in_chunks()
        chunk_len: int = len(chunks)
        
        for n, chunk in enumerate(chunks):
            genlog.report("DEBUG", f"Process chunk [{n}|{chunk_len}]")
            self._start_processes(chunk)
            self._join_processes(chunk)