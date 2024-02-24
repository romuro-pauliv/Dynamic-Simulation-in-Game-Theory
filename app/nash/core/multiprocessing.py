# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        app/core/multiprocessing.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import multiprocessing

from typing import Callable
# |--------------------------------------------------------------------------------------------------------------------|


class CoreChunk(object):
    def __init__(self, cpu_off: int, processing_times: int) -> None:
        """
        Initialize the CoreChunk instance.
        Args:
            cpu_off (int): Inform qnt of cpus offs
            processing_times (int): Qnt times to processing the function
        """
        self.CPU                : int = multiprocessing.cpu_count()-cpu_off
        self.processing_times   : int = processing_times
        
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
    
    def _split_in_chunks(self) -> list[list[multiprocessing.Process]]:
        """
        Split the process list in chunks
        Returns:
            list[list[multiprocessing.Process]]: Process list in chunks
        """
        return [self.processes[i:i+self.CPU] for i in range(0, len(self.processes), self.CPU)] 

    def _start_processes(self, process_list: list[multiprocessing.Process]):
        for process in process_list:
            process.start()
    
    def _join_processes(self, process_list: list[multiprocessing.Process]):
        for process in process_list:
            process.join()
    
    def run(self) -> None:
        """
        Run with multiprocessing
        """
        self._generate_processes()
        chunks: list[list[multiprocessing.Process]] = self._split_in_chunks()
        
        for chunk in chunks:
            self._start_processes(chunk)
            self._join_processes(chunk)