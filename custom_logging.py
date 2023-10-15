import coloredlogs
import logging
from functools import partial, partialmethod
import functools
import inspect
import os
import time
import sys
import copy
        
class CustomLogger():
    def __init__(self, **kwargs):
        """
        kwargs:
        
        log_files = ['main_log.log']
        
        log_dir = 'log'
        
        log_to_console = True
        """
        self.add_custom_levels()
        self.name = None
        log_files = kwargs.get('log_files', ['main_log.log'])
        log_dir = kwargs.get('log_dir', 'log')
        log_to_console = kwargs.get('log_to_console', True)

        self.make_logging_pretty()

        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        self.log_filepaths = [os.path.join(log_dir, log_file) for log_file in log_files]
        
        self.create_log_filepaths()


        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        self.file_handlers = [logging.FileHandler(log_filepath) for log_filepath in self.log_filepaths]
        self.console_handler = logging.StreamHandler()

        self.setup_handlers(log_to_console)

    def create_log_filepaths(self):
        for log_filepath in self.log_filepaths:
            if not os.path.exists(log_filepath):
                #open the file to create it
                with open(log_filepath, 'w') as _:
                    continue
        
    def add_name_to_log_format(self, name):
        name_without_spaces = name.replace(' ', '_')
        new_log_format = f'[%(asctime)s] %(funcName)s %(levelname)s-({name_without_spaces})  %(message)s'
        self.set_new_log_format(new_log_format)

    def set_new_log_format(self, new_log_format):
        """
        Sets the logging format to the provided `log_format`.

        Args:
            log_format (str): Custom log format string.

        Example usage:
            logger = CustomLogger()
            logger.set_log_format('%(asctime)s [%(levelname)s]: %(message)s')
        """
        new_colored_formatter = self.create_colored_formatter(new_log_format)

        self.logger.removeHandler(self.console_handler)

        self.console_handler.setFormatter(new_colored_formatter)
        self.logger.addHandler(self.console_handler)

        for file_handler in self.file_handlers:
            file_handler.setFormatter(new_colored_formatter)
                  

    def add_custom_levels(self):        
        """
        Adds custom levels to the logger. Change this yourself depending on which levels you want.

        """
        self.add_custom_level("send", 37, "yellow")
        self.add_custom_level("recv", 38, "cyan")
        self.add_custom_level("checkpoint", 39, "magenta")
        
    
    def add_custom_level(self, levelName: str, levelNum: int, levelColor: str):
        """
        Adds a custom logging level with the given `levelName`, `levelNum`, and `levelColor`. 
        
        """
        levelNameUpper = levelName.upper()
        levelNameLower = levelName.lower()

        setattr(logging, levelNameUpper, levelNum)
        logging.addLevelName(getattr(logging, levelNameUpper), levelNameUpper)

        setattr(logging.Logger, levelNameLower, partialmethod(logging.Logger.log, getattr(logging, levelNameUpper)))

        setattr(logging, levelNameLower, partial(logging.log, getattr(logging, levelNameUpper)))

        logging.getLogger().setLevel(getattr(logging, levelNameUpper))

        coloredlogs.DEFAULT_LEVEL_STYLES[levelNameLower] = {"color": levelColor, "bold": True}
        
    def setup_handlers(self, log_to_console):
        colored_formatter = self.create_colored_formatter()
        for handler in self.file_handlers:
            handler.setFormatter(colored_formatter)
            self.logger.addHandler(handler)

        if log_to_console:
            self.console_handler.setFormatter(colored_formatter)
            self.logger.addHandler(self.console_handler)
        
    def make_logging_pretty(self):
        self.default_log_fmt = '[%(asctime)s] %(funcName)s %(levelname)s %(message)s'
        self.field_styles = {'levelname': {'color': 'cyan'}, 'asctime': {'color': 'white'},
                                            'funcName': {'color': 'yellow'}}
        self.date_fmt = '%H:%M:%S'

        self.level_styles = copy.deepcopy(coloredlogs.DEFAULT_LEVEL_STYLES)
        
        additonal_level_styles = {
            "info": {'color': 'green'}, "debug": {'color': 'red'}
            }

        self.level_styles.update(additonal_level_styles)
        
    def create_colored_formatter(self, log_fmt = None):
        new_fmt = log_fmt or self.default_log_fmt
        colored_formatter = coloredlogs.ColoredFormatter(fmt=new_fmt,
                                                datefmt=self.date_fmt,
                                                level_styles=self.level_styles,
                                                field_styles=self.field_styles)
        return colored_formatter
        
    def clear_logs(self):
        """
        Clears the contents of the log file located at the specified file path.
        """
        for log_filepath in self.log_filepaths:
            with open(log_filepath, 'w') as log_filepath:
                log_filepath.truncate(0)
            
    def set_new_log_files(self, new_log_filenames):
        """
        Will log to the new files given after calling this function. 

        """
        new_log_filepaths = [os.path.join(self.log_dir, log_file) for log_file in new_log_filenames]
        
        for handler in self.file_handlers:
                self.logger.removeHandler(handler)

        for filepath in new_log_filepaths:
            file_handler = logging.FileHandler(filepath)
            file_formatter = self.create_colored_formatter()
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)

        self.log_filepaths = new_log_filepaths

    
def debug_vars(*to_print):
    prev_func_name = inspect.currentframe().f_back.f_code.co_name
    
    name_val_list = []
    
    callers_local_vars = inspect.currentframe().f_back.f_locals
    id_to_local_var = {id(value) : (name, value)  for name, value in callers_local_vars.items()}
    
    for var in to_print:
        name, value = id_to_local_var[id(var)]
        name_val_list.append( (name, value) )
    
    toLog =  ", ".join([f"{name}={val}" for name, val in name_val_list])
    logging.debug(f"From {prev_func_name}- {toLog}")
    
    
def time_code(func):
    @functools.wraps(func)
    def code_timer(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        logging.timestamp(f"Finished {func.__name__!r} in {execution_time:.4f} secs")
        return result
    return code_timer

    
def newline_before_after(func):
    def funcInfo(*args, **kwargs):
        print()
        result = func(*args, **kwargs)
        print()
        return result
    return funcInfo


@newline_before_after
def bigCheckpoint(to_print: str):
    logging.checkpoint(to_print) 
                       
                       
def log_calls(func):
    @functools.wraps(func)
    def funcInfo(*args, **kwargs):
        beginning = f"Beginning of {func.__name__} function"
        
        print()
        logging.debug(beginning)
        print()
        result = func(*args, **kwargs)
        
        print()
        logging.debug(f"End of {func.__name__} function")
        print()
        return result
    return funcInfo


def log_calls_args(func):
    def funcInfo(*args, **kwargs):
        args_str = ", ".join(map(str, args))
        kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        beginning = f"Beginning of {func.__name__} function with args ({args_str}) and kwargs ({kwargs_str})"
        logging.debug(beginning)
        result = func(*args, **kwargs)
        logging.debug(f"End of {func.__name__} function")
        return result
    return funcInfo


def get_next_counter(filename = "counter_num.txt"):
    """
    Returns a counter that starts at 1. In order to reset, call a file with 'reset' in the command line arguments.
    """
    if "reset" in sys.argv:
        reset_counter(filename)

    if os.path.exists(filename):
        with open(filename, "r") as f:
            counter_num = int(f.read())
    else:
        counter_num = 1

    with open(filename, "w") as f:
        f.write(str(counter_num + 1))

    return counter_num

def reset_counter(filename= "counter_num.txt"):
    """
    Reset the counter number to 1.
    """
    with open(filename, "w") as f:
        f.write("1")
    logging.debug("Counter number reset to 1.")

    


    

