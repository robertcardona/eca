import numpy as np

class ECA:

    def __init__(self, rule, width, height, starting_configuration):

        self.debug = False
        self.rule = rule
        self.width = width
        self.height = height

        self.universe = [0] * (width * height)

        for i, bit in enumerate(starting_configuration):
            self.universe[i] = bit
            # print("" + str(i) + "|" + str(bit))

        # print(self.universe)

    def get_value(self, row_index, column_index):
        return self.universe[row_index * self.width + column_index];

    def set_value(self, row_index, column_index, value):
        self.universe[row_index * self.width + column_index] = value

    def increase_generation(self, current_row_index):

        if current_row_index == 0:
            return -1

        for i in range(0, self.width):
            radius = self.get_radius(current_row_index - 1, i);
            rule = radius[0] << 2 | radius[1] << 1 | radius[2];
            bit = self.rule_lookup(rule);

            self.set_value(current_row_index, i, bit)

    def generate(self):

        for current_row_index in range(1, self.height):
            self.increase_generation(current_row_index);

    def get_flattened_universe(self):
        """Assumes generate was run"""
        return 0

    def get_2d_universe(self):

        universe = np.zeros((self.height, self.width), np.dtype(np.uint8))

        for row_index in range(0, self.height):
            for column_index in range(0, self.width):
                universe[row_index][column_index] = self.get_value(row_index, column_index);

        return universe

    def make_csv(self):
        """Assumes generate was run"""
        return 0

    def rule_lookup(self, rule):
        bit = (self.rule & (1 << rule)) >> rule;
        return bit

    def get_radius(self, row_index, column_index):
        """Returns the radius around the given index, wrapping around."""

        is_periodic = False

        a = self.get_value(row_index, (column_index - 1) % self.width)
        b = self.get_value(row_index, column_index)
        c = self.get_value(row_index, (column_index) + 1 % self.width)

        if is_periodic == False:
            if (column_index - 1) % self.width == 0:
                a = (a ^ a) & 1
            if (column_index) + 1 % self.width == self.width - 1:
                c = (c ^ c) & 1

        return [a, b, c]
