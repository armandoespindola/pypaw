#!/usr/bin/env python
import matplotlib as mpl
mpl.use('Agg')  # NOQA

import argparse                 # NOQA
from pypaw import AttenuationAdjointASDF # NOQA

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store', dest='params_file',
                        required=True, help="parameter file")
    parser.add_argument('-f', action='store', dest='path_file', required=True,
                        help="path file")
    parser.add_argument('-r', "--reference-frequency", type=float,
                        required=True,
                        help="referency frequency fro attenuation adjoint source")
    parser.add_argument('-v', action='store_true', dest='verbose',
                        help="verbose flag")
    args = parser.parse_args()

    proc = AttenuationAdjointASDF(
        args.path_file, args.params_file,
        reference_frequency=args.reference_frequency,
        verbose=args.verbose)
    proc.smart_run()


if __name__ == '__main__':
    main()
