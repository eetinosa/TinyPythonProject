#!/usr/bin/env python3
"""
Author : etinosa <etinosa@localhost>
Date   : 2020-11-04
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = "an" if word[0].lower() in "aeiou" else "a"
    print(f"Ahoy, Captain, {article} " + word + " off the larboard bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
