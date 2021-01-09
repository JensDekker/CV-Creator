import json


y_n = ["Yes", "No"]


def retrieve_data(fname):
    """opens json formatted file and returns workable data (lists and dictionaries)"""
    with open(fname, "r") as file:
        json_str = file.read()
    return json.loads(json_str)


def option_regulator(option_lst, prompt, single_return=True):
    """takes an sequence and asks the user to select one of the choices presented
    returns the chosen option from the iterable
    if the iterable is a dictionary, it will print the key-value pair"""
    print("")
    opt_num = 1
    opt_dict = {}
    for option in option_lst:
        try:
            print("{} -> {}: {}".format(opt_num, option, option_lst[option]))
        except TypeError:
            print("{} -> {}".format(opt_num, option))
        opt_dict[opt_num] = option
        opt_num += 1
    while single_return:
        try:
            user_inp = int(input(prompt))
            return opt_dict[user_inp]
        except KeyError:
            print("Whoops! That number's out of range.")
        except ValueError:
            print("Whoops! That wasn't a valid input.")
    print("Please enter your selection in the order you would like separated by forward slashes")
    print("Note that you are not required to use all the options presented")
    while not single_return:
        try:
            user_inp = input(prompt).split("/")
            return [opt_dict[int(num)] for num in user_inp]
        except KeyError:
            print("Whoops! That number's out of range.")
        except ValueError:
            print("Whoops! That wasn't a valid input.")


def iterated_ask(q_list):
    """asks the user for an input for each element in a sequence
    returns dictionary of the iterables as key and inputs as values"""
    print("Please fill out the following sections as you like.")
    output = {}
    for q in q_list:
        output[q] = input(q + " ")
    return output


def entry_select(section, task):
    """Takes section and asks the user to pick an entry in accordance with what task needs to be completed"""
    q = "Which entry would you like to {}? ".format(task.lower())
    entries = list(section.keys())
    entries.remove("Format")
    entry = option_regulator(entries, q)
    return entry


def save(data, filename):
    with open(filename, "w") as file:
        file.write(json.dumps(data, indent=4))
