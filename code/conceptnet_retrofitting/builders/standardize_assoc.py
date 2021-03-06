import numpy as np

from conceptnet_retrofitting.standardization import standardize


def standardize_assoc(assoc_in, assoc_out):
    """
    Take in a tab-separated file containing items that are associated with
    each other, and write it out in a form that is compatible with
    conceptnet5.csv.
    """
    with open(assoc_out, 'w', encoding='utf-8') as out:
        for line in open(assoc_in, encoding='utf-8'):
            line = line.rstrip('\n')
            if line:
                item1, item2 = line.split('\t')
                s1 = standardize(item1)
                s2 = standardize(item2)
                transformed = '\t'.join([s1, s2, '1', 'external', '/r/RelatedTo'])
                print(transformed, file=out)


def main(assoc_in, assoc_out):
    standardize_assoc(assoc_in, assoc_out)


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
