# from lab_python_fp.sort import sort
# from behave import *
#
#
# @given("the list is [{list}] and reverse is {reverse}")
# def have_info(context, list, reverse):
#     context.list = [i for i in list.split(', ')]
#     context.reverse = False if reverse == "False" or reverse == "false" else True
#
#
# @when("I sort the list")
# def find_unique(context):
#     context.result = sort(context.list, rev=context.reverse)
#
#
# @then("I expect the result to be [{list}]")
# def expect_result(context, list):
#     result = [i for i in list.split(', ')]
#     assert context.result == result
#
