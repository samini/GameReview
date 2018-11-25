from optparse import OptionParser
import sys

class FlagParser(object):

    def __init__(self):
        parser = OptionParser(usage='%s [options]\nUse -h for list of available options' % sys.argv[0])
        parser.add_option('-k', '--api-key', dest='api_key', help='Giant Bomb api key')
        parser.add_option('-i', '--input', dest='input_file', help='Input file in CSV format containing Game names in first column')
        parser.add_option('-v', '--verbose', action='store_true', default=False, dest='verbose', help='Run in verbose mode')
        self.parser = parser

    def parse_flags(self):
        options, args = self.parser.parse_args()
        if not options.api_key:
            self.parser.error('No API key passed')
            return None
        if not options.input_file:
            self.parser.error('No input file')
            return None
        return (options, args)
