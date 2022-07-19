import time


def print_current_execution_time(start_time, cpu_start_time):
    # get the end time
    end_time = time.time()
    cpu_end_time = time.process_time()
    # get the execution time
    elapsed_time = end_time - start_time

    elapsed_cpu_time = cpu_end_time - cpu_start_time

    print('Execution time:', time.strftime(
        "%H:%M:%S", time.gmtime(elapsed_time)))
    print('CPU Execution time:', time.strftime(
        "%H:%M:%S", time.gmtime(elapsed_cpu_time)))
