#!/usr/bin/env node

/**
 * Run the gcc preprocessor on a C file and output the
 * result to a file named "c".
 */

const { execFileSync } = require('child_process');

/**
 * Program entry point.
 * 
 * @returns{number} Process exit code.
 */
const cfile = process.env.CFILE;

execFileSync(
    "gcc", ["-E", cfile, "-o", "c"], {stdio: "inherit",}
);