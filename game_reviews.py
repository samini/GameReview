#!/usr/bin/env python

from file_utils import read_game_names
from flag_parser import FlagParser
from review_endpoint import ReviewEndpoint
import sys

def print_games(games):
  if games:
    print('\nHere are your games:')
    for game in games:
      print game

if __name__ == "__main__":
  fp = FlagParser()
  options, args = fp.parse_flags()
  if not options:
    sys.exit(1)
  v = options.verbose
  if v:
    print("\nAPI Key: %s" % options.api_key)
    print("Input file: %s" % options.input_file)
  games = read_game_names(options.input_file)
  if v:
    print_games(games)
  re = ReviewEndpoint(options.api_key, v)
  for game in games:
    print(re.get_review(game))
