#!/usr/bin/python3
"""
Runs a C source file through the gcc preprocessor.

The input file is obtained from the CFILE environment variable.
The processed output file is written named "c".
"""

import os
import subprocess
"""
Execute the gcc preprocessor on the input file C.

Returns:
    int: Exit status code.
        0 on success, non-zero on failure.
"""

cfile = os.environ["CFILE"]

subprocess.run(
    ["gcc", "-E", cfile, "-o", "c"],
    check=True
)