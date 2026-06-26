package main

import (
	"log"
	"os"
	"os/exec"
)

/*
Run the C preprocessor on a C file and output
the result to a file named "c".

Returns:
	Exit code 0 on success.
*/

func main() {
	cfile := os.Getenv("CFILE")

	cmd := excec.Command("gcc", "-E", cfile, "-o", "c")

	if err := cmd.Run(); err != nil {
		log.Fatal(err)
	}
}