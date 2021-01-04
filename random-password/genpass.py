# genpass - generates a random password
import argparse
from pass_module import Pass, MIN_PASSLEN, MAX_PASSLEN, DEFAULT_LEN

PROGRAM_DESCRIPTION = 'Returns random password. Default is 16-character password \
    with password complexity enabled.'
HELP_PASSLEN = f'Password lengh must be an integer between {MIN_PASSLEN} and {MAX_PASSLEN}.'
HELP_NO_COMPLEXITY = f'Eliminate complexity requirements.'
HELP_NO_SPECIAL_CHARS = 'Exclude special characters.'


def cmd_arguments():
    parser = argparse.ArgumentParser(description=PROGRAM_DESCRIPTION)
    parser.add_argument('-l', '--passlength', nargs='?', const=0, type=int, help=HELP_PASSLEN, \
        default=DEFAULT_LEN)
    parser.add_argument('-c', '--nocomplexity', action='store_false', help=HELP_NO_COMPLEXITY)
    parser.add_argument('-n', '--nospecialchars', action='store_false', help=HELP_NO_SPECIAL_CHARS)

    return parser.parse_args()


## executable starts here ##
clArgs = cmd_arguments()

password = Pass(clArgs.passlength, clArgs.nocomplexity, clArgs.nospecialchars)

print(password.get_password())
