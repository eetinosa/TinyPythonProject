#!/usr/bin/env python3
"""
Author : etinosa <etinosa@localhost>
Date   : 2020-11-23
Purpose: Jumping the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input Text')

    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """main program"""

    args = get_args()
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
'6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
    
    answer = ''
    for char in args.text:
        answer += jumper.get(char, char)
    print(answer)

   

# --------------------------------------------------
if __name__ == '__main__':
    main()
