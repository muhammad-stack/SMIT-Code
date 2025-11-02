from pympler import summary, muppy
import psutil
import os
import sys

def memory_usage_psutil():
    """Return the memory usage in MB using psutil."""
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / (2 ** 20)  # More efficient: removed float() wrapper
    return mem

def memory_usage_resource():
    """Return the memory usage using resource module (Unix-like systems only)."""
    import resource  # Import only when needed
    rusage_denom = 1024.
    if sys.platform == 'darwin':
        # macOS uses different units
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem
