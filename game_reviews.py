#!/usr/bin/env python

from flag_parser import FlagParser
import sys

if __name__ == "__main__":
  fp = FlagParser()
  options, args = fp.parse_flags()
  if not options:
    sys.exit(1)
  if options.verbose:
    print("API Key: %s" % options.api_key)
    print("Input file: %s" % options.input_file)
