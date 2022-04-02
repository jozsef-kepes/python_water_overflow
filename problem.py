# -----------------------------------------------------------
# Implementation of the Problem class for overflow problem using python
# email jozsef.la.kepes@gmail.com
# -----------------------------------------------------------


from typing import List
from glass import Glass


class Problem:
    """Water Overflow Problem class"""

    def __init__(self):
        self.content = []

    def pour(self, input_litres):
        """Input liquid in litres for overflow problem (main problem logic)"""

        self.check_positive_int_or_float(input_litres)

        input_millilitres = input_litres*1000
        iter_row = 0
        capacity = 250

        while input_millilitres > 0:
            num_glasses = iter_row+1

            # If the row of glasses cannot be completely filled by the liquid
            if input_millilitres >= (num_glasses*capacity):
                # Calculate row weight, including initial row.
                row = self.row_weight_calculation(
                    self.content[-1] if self.content else self.content)

                # Set trivial glasses to be at capacity (250ml)
                for glass in row:
                    glass.set_contents(capacity)

                self.content.append(row)
                input_millilitres -= (num_glasses*capacity)
                iter_row += 1
            else:
                # Generate weight for glasses in row
                row = self.row_weight_calculation(self.content[iter_row-1])

                # Calculate the standard unit liquid based on weight per row
                single_unit_input = input_millilitres/self.get_row_weight(row)

                # Input the standard 1 unit of liquid (calculates actual liquid based on glass weight)
                for glass in row:
                    glass.set_weighted_contents(single_unit_input)

                # Check if overflow row has cascading overflow
                weight_calcd = False
                next_row = []
                for index, glass in enumerate(row):
                    if glass.contents > 250:

                        # Do row weight calc for overflow row
                        if not weight_calcd:
                            next_row = self.row_weight_calculation(row)
                            weight_calcd = True

                        # Calc liquid split for child glasses
                        input_split = (glass.contents-250)/2
                        glass.set_contents(250)

                        next_row[index].add_contents(input_split)
                        next_row[index+1].add_contents(input_split)

                self.content.append(row)

                if next_row:
                    self.content.append(next_row)

                input_millilitres = 0

    def check_positive_int_or_float(self, value):
        """Check that argparse values are positive"""
        try:
            float(value)
        except ValueError:
            raise ValueError(
                f'\'{value}\' is an invalid non integer/float value')
        else:
            if float(value) < 0:
                raise ValueError(
                    f'\'{value}\' is an invalid positive int value')

        return float(value)

    def print_weight_calculation(self):
        """Print the 2D input list of glass weights"""
        for row in self.content:
            row_string = ""
            for glass in row:
                row_string += f' {glass.get_weight()} '
            print(row_string.center(3 * (len(self.content[-1]))))

    def print_content_calculation(self):
        """Print the 2D input list of glass weights"""
        for row in self.content:
            row_string = ""
            for glass in row:
                row_string += f' {glass.contents} '
            print(row_string.center(3 * (len(self.content[-1]))))

    def sum_glass_content(self):
        """Print the 2D input list of glass weights"""
        sum_millilitres = 0
        for row in self.content:
            for glass in row:
                sum_millilitres += glass.contents
        return sum_millilitres/1000

    def row_weight_calculation(self, previous_row: List):
        """Return a row of glasses with weight's calculated based on the previous row"""
        row_num = len(previous_row) + 1
        row = []

        num_glasses = len(previous_row) + 1
        iter_row = row_num

        if len(previous_row) <= 1:
            for glass in range(num_glasses):
                new_glass = Glass(0, 0, 1)
                row.append(new_glass)
                new_glass.set_contents(250)
            return row

        for glass in range(num_glasses):
            if (iter_row > 1) and (glass != 0) and (glass != num_glasses-1):
                weight = previous_row[glass-1].weight + \
                    previous_row[glass].weight
                new_glass = Glass(iter_row, glass, weight)
                row.append(new_glass)
            else:
                new_glass = Glass(iter_row, glass, 1)
                row.append(new_glass)

        return row

    def get_row_weight(self, row):
        """Return total weight per row of glasses"""
        sum_weight = 0
        for glass in row:
            sum_weight += glass.get_weight()
        return sum_weight

    def get_glass_content(self, row, glass):
        """Return contents in millilitres of glass at row i, glass j"""

        if row >= len(self.content):
            raise ValueError(
                f'Glass row {row} does not exist. Please choose a row between 0 and {len(self.content)}')

        if glass >= len(self.content[row]):
            raise ValueError(
                f'Glass number {glass} does not exist in row {row}. Please choose a glass between 0 and {len(self.content[row])}')

        return self.content[row][glass].get_contents()
