# -----------------------------------------------------------
# Implementation of the water overflow problem using python
# email jozsef.la.kepes@gmail.com
# -----------------------------------------------------------

from typing import List
from glass import Glass


def print_weight_calculation(glass_array: List):
    """Print the 2D input list of glass weights"""
    for row in glass_array:
        row_string = ""
        for glass in row:
            row_string += f' {glass.get_weight()} '
        print(row_string.center(3 * (len(glass_array[-1]))))


def print_content_calculation(glass_array: List):
    """Print the 2D input list of glass weights"""
    for row in glass_array:
        row_string = ""
        for glass in row:
            row_string += f' {glass.contents} '
        print(row_string.center(3 * (len(glass_array[-1]))))


def sum_glass_content(glass_array: List):
    """Print the 2D input list of glass weights"""
    sum_millilitres = 0
    for row in glass_array:
        for glass in row:
            sum_millilitres += glass.contents
    return sum_millilitres


def row_weight_calculation(glass_row: List):
    return []


def pour(jug_capacity):
    """Return the 2D list after pouring jug_capacity into overflow problem"""
    # logic to display and pour
    content = []
    iter_row = 0
    input_millilitres = jug_capacity*1000

    while input_millilitres > 0:
        num_glasses = iter_row+1
        capacity = 250
        if input_millilitres < (num_glasses*capacity):
            row = []
            next_row = []

            for glass in range(num_glasses):
                if (iter_row > 1) and (glass != 0) and (glass != num_glasses-1):
                    weight = content[iter_row-1][glass-1].weight + \
                        content[iter_row-1][glass].weight
                    new_glass = Glass(iter_row, glass, weight)
                    row.append(new_glass)
                else:
                    new_glass = Glass(iter_row, glass, 1)
                    row.append(new_glass)

            sum_weight = 0
            for glass in row:
                sum_weight += glass.get_weight()

            single_unit_input = input_millilitres/sum_weight

            for glass in row:
                glass.set_weighted_contents(single_unit_input)

            # do >250ml check for current row
            weight_calcd = False
            for index, glass in enumerate(row):
                if glass.contents > 250:

                    # do next row weight calc
                    if not weight_calcd:
                        for next_row_glass in range(num_glasses+1):
                            if (next_row_glass != 0) and (next_row_glass != num_glasses):
                                weight = row[next_row_glass-1].weight + \
                                    row[next_row_glass].weight
                                new_glass = Glass(
                                    iter_row, next_row_glass, weight)
                                next_row.append(new_glass)
                            else:
                                new_glass = Glass(iter_row, next_row_glass, 1)
                                next_row.append(new_glass)
                        weight_calcd = True

                    # calc child split
                    input_split = (glass.contents-250)/2
                    glass.set_contents(250)

                    next_row[index].add_contents(input_split)
                    next_row[index+1].add_contents(input_split)

            content.append(row)

            if next_row:
                content.append(next_row)

            iter_row += 1
            break
        else:
            input_millilitres -= (num_glasses*capacity)
            row = []
            for glass in range(num_glasses):
                if (iter_row > 1) and (glass != 0) and (glass != num_glasses-1):
                    weight = content[iter_row-1][glass-1].weight + \
                        content[iter_row-1][glass].weight
                    new_glass = Glass(iter_row, glass, weight)
                    row.append(new_glass)
                    new_glass.set_contents(0.25 * 1000)
                else:
                    new_glass = Glass(iter_row, glass, 1)
                    row.append(new_glass)
                    new_glass.set_contents(0.25 * 1000)

            content.append(row)
            iter_row += 1

    return content


def main():
    """Main function for water overflow problem"""
    result = pour(2.4)
    print_weight_calculation(result)
    print_content_calculation(result)
    print(sum_glass_content(result))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        raise exc
