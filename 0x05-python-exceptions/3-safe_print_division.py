#!/usr/bin/python3
def safe_print_division(a, b):
    try:
       div_ result = a / b
    except ZeroDivisionError:
        div_result = None
    finally:
        print("Inside div_result: {}".format(div_result))
    return div_result
