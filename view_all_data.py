import utils

indent = 3
data = utils.retrieve_data("resume_data.txt")
for section in data:
    print("\n{}".format(section))
    for entry in data[section]:
        if entry != "Format":
            print(" " * indent + entry)
