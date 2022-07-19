import os
import json
import pandas as pd
import numpy as np
import time

from src.utils.execution_time import print_current_execution_time


if __name__ == '__main__':
    # get the start time
    start_time = time.time()
    start_process_time = time.process_time()

    print('Started processing files')
    print('Finished processing files')
    print_current_execution_time(start_time, start_process_time)
