#!/usr/bin/python3
def safe_print_division(a, b):
    div_result = None
    try:
        div_result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        print("Inside div_result: {}".format(div_result))
    return div_result
