from lab_python_fp.sort import num_sort
from lab_python_fp.sort import sort
from behave import *


@given("the list is [{list}] of type {type} and reverse is {reverse}")
def have_info(context, list, type, reverse):

    if type == "string" or type == "String":
        context.type = str
        context.list = [i for i in list.split(', ')]
    elif type == "integer" or type == "Integer":
        context.type = int
        context.list = [int(i) for i in list.split(', ')]
    context.reverse = False if reverse == "False" or reverse == "false" else True


@when("I sort the list")
def find_unique(context):
    context.result = num_sort(context.list, rev=context.reverse) if context.type == int else sort(context.list, rev=context.reverse)


@then("I expect the result to be [{list}]")
def expect_result(context, list):
    result = []
    if context.type == str:
        result = [i for i in list.split(', ')]
    elif context.type == int:
        result = [int(i) for i in list.split(', ')]
    assert context.result == result
