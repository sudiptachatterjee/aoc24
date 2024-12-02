"""Advent of Code 2024, Problem 01: Location pairs.
https://adventofcode.com/2024/day/1
"""

import aoc_utils
from unittest import TestCase, main

class TotalDistanceBetweenLists(TestCase):
    """Find the total distance between two lists as defined by the problem."""

    def extract_lists(self, input_file):
        """Extract two lists from a file."""
        lines = aoc_utils.read_input(input_file)
        return [int(x) for x in lines[0].split()], [int(x) for x in lines[1].split()]

    def distance_between_lists(self, list1, list2):
        """Return the total distance between two lists."""
        list1.sort()
        list2.sort()
        return sum([abs(a - b) for a, b in zip(list1, list2)])

    def solve_problem(self, input_file):
        """Solve the problem."""
        list1, list2 = self.extract_lists(input_file)
        return self.distance_between_lists(list1, list2)

    def test_distance_between_same_list_returns_zero(self):
        """Test the distance between two lists."""
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertEqual(self.distance_between_lists(list1, list2), 0)

    def test_distance_between_different_lists_accurate(self):
        """Test the distance between two lists."""
        list1 = [1, 2, 3]
        list2 = [6, 5, 4]
        self.assertEqual(self.distance_between_lists(list1, list2), 9)

if __name__ == '__main__':
    # main()
    solver = TotalDistanceBetweenLists()
    print(solver.solve_problem('aoc24_01_input.txt'))