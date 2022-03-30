# -----------------------------------------------------------
# Implementation of the water overflow problem using python
# email jozsef.la.kepes@gmail.com
# -----------------------------------------------------------


from glass import Glass
from typing import List


def print_calculation(input: List):
    """Print the 2D input list of glass weights"""
    for row in input:
        for glass in row:
            print(glass.weight, end = " ")
        print()

def pour(jug_capacity):
    """Return the 2D list after pouring jug_capacity into overflow problem"""
    # logic to display and pour
    content = []
    iter_row = 0

    while (jug_capacity > 0):
        num_glasses = iter_row+1
        capacity = 250
        if jug_capacity<(num_glasses*capacity):
            # calc ratio using weights (possibly recursive? might only need to take into account previous row)

            # for loop that traverses up till the top for each glass in the row.

            # divide the pour over by weight.

            # check if two next to each other are greater than capacity.

            # if they are greater -> # for loop that traverses up till the top for each glass in the row. 

            # specifically handle the excess per glass above

            iter_row+=1
            break
        else:
            jug_capacity-=(num_glasses*capacity)
            row = []
            for glass in range(num_glasses):
                if len(row) > 3:
                    weight = content[iter_row-1][glass].weight + content[iter_row-1][glass+1].weight
                    row.append(Glass(iter_row, glass, weight))
                else:
                    row.append(Glass(iter_row, glass, 1))

            content.append(row)
            iter_row+=1
    
    return content

def main():
    print_calculation(pour(1.5))

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        raise exc