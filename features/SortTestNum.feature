Feature: Test of sort.py with number list
  descr

  Scenario: SortTestNum.py without reverse of the result
    Given the list is [1, 2, 1, 1, 3, 2, 1, 2] of type Integer and reverse is False
    When I sort the list
    Then I expect the result to be [1, 1, 1, 1, 2, 2, 2, 3]

  Scenario: SortTestNum.py with reverse of the result
    Given the list is [1, 2, 1, 1, 3, 2, 1, 2] of type Integer and reverse is True
    When I sort the list
    Then I expect the result to be [3, 2, 2, 2, 1, 1, 1, 1]

  Scenario: SortTestNum.py without reverse of the result
    Given the list is [1, 2, 1, 1, 3, 2, 1, 2] of type String and reverse is False
    When I sort the list
    Then I expect the result to be [1, 1, 1, 1, 2, 2, 2, 3]

  Scenario: SortTestNum.py with reverse of the result
    Given the list is [1, 2, 1, 1, 3, 2, 1, 2] of type String and reverse is True
    When I sort the list
    Then I expect the result to be [3, 2, 2, 2, 1, 1, 1, 1]