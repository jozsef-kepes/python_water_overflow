# -----------------------------------------------------------
# Implementation of the water overflow problem using python
# email jozsef.la.kepes@gmail.com
# -----------------------------------------------------------


import argparse
from problem import Problem


def check_positive_int_or_float(value):
    """Check that argparse values are positive"""
    try:
        float(value)
    except ValueError:
        raise PARSER.error(
            f'\'{value}\' is an invalid non integer/float value')
    else:
        try:
            if float(value) < 0:
                raise ValueError
        except:
            raise PARSER.error(
                f'\'{value}\' is an invalid positive int value')
    return float(value)


def main():
    """Main function for water overflow problem"""
    global PARSER  # pylint: disable=global-statement
    PARSER = argparse.ArgumentParser(description="Run the overflow problem")
    PARSER.add_argument(
        'input',
        type=check_positive_int_or_float,
        help='a float for the input liquid (in litres)',
    )
    PARSER.add_argument(
        'row',
        type=int,
        help='row number that glass is located',
    )
    PARSER.add_argument(
        'glass',
        type=int,
        help='glass number that liquid contents are located',
    )
    PARSER.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='include verbose debug print statements',
    )

    args = PARSER.parse_args()

    # Do calculation
    run_1 = Problem()
    run_1.pour(args.input)

    # # Get result
    print(f'Row:{args.row}, Glass:{args.glass}, Contents(ml):{run_1.get_glass_content(args.row, args.glass)}')

    # Verbose output for debugging purposes
    if args.verbose:
        run_1.print_weight_calculation()
        run_1.print_content_calculation()
        print(run_1.sum_glass_content())


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        raise exc
