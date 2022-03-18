# Nested loops

import umpyutl as umpy


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # CHALLENGE 01

    # Get articles
    articles = None # TODO Call function

    # print(f"\nCh 01 Articles (n={len(articles)})")

    subject_counts = {}

    # TODO Implement loop

    # Sort by value (reversed = -x[1]), then by key (x[0])
    subject_counts = None # dict comp

    # Write to file
    # TODO write to file


    # CHALLENGE 02

    authors = []

    # TODO Implement loop

    # print(f"\nauthors (n={len(authors)})")

    # Sort Authors
    # WARN: convert None to empty string to avoid runtime exception (middlename value)
    # str(x or '') returns '' if x is falsy
    # TypeError: '<' not supported between instances of 'NoneType' and 'str'
    authors = None # TODO list comp

    # print(f"\nAuthors = {authors}")

    # TODO write to file


    # CHALLENGE 03

    citations = {}

    # TODO Implment loop

    # Sort Authors
    citations = None # TODO dict comp

    # TODO write to file



    # CHALLENGE 04

    # TODO Refactor Challenge 03 loop

    # print(f"\nCh 03 Benedict Carey authored articles = {len(citations['Carey_Benedict'])}")


if __name__ == '__main__':
    main()