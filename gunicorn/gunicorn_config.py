import os
import multiprocessing
import sylvia


def num_cpus():
    cpus = 0
    try:
        cpus = os.sysconf("SC_NPROCESSORS_ONLN")
    except:
        cpus = multiprocessing.cpu_count()
    return cpus or 3


name = 'django'
bind = '0.0.0.0:8000'
workers = num_cpus() * 2 + 1
debug = True
daemon = False
loglevel = 'debug'
