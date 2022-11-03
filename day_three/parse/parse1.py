import optparse


parser = optparse.OptionParser()
# Etxra functionality goes here
help = """Usage: 
%prog [options] directories...

Visit listed directories and process
the data in them."""
parser.add_option(
    '-o',
    '--output',
    help = "Name of output file",
    dest = 'output_file',
    default = 'output.dat'
)

parser.set_usage(help)














(opts , args )= parser.parse_args()