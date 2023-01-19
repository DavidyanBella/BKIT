Feature: Test of sort.py with string list
  descr

  Scenario: SortTestStr.py without reverse of the result
    Given the list is [1, 2, 1, 1, 3, 2, 1, 2] and reverse is False
    When I sort the list
    Then I expect the result to be [1, 1, 1, 1, 2, 2, 2, 3]

  Scenario: SortTestStr.py with reverse of the result
    Given the list is [1, 2, 1, 1, 3, 2, 1, 2] and reverse is True
    When I sort the list
    Then I expect the result to be [3, 2, 2, 2, 1, 1, 1, 1]