#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    div = 0
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            div_list.append(div)
        except ZeroDivisionError:
            div = 0
            div_list.append(div)
            print("division by 0")
            continue
        except TypeError:
            div = 0
            div_list.append(div)
            print("wrong type")
            continue
        except IndexError:
            div = 0
            div_list.append(div)
            print("out of range")
            continue
        except ValueError:
            div = 0
            div_list.append(div)
            continue
        finally:
            continue
    return div_list
