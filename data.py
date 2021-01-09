import utils


def add(section):
    """Takes the categories that need to be filled and asks for input on each.
    Ends by adding the resulting dictionary to the save_location (a list)"""
    try:
        categories = section["Format"]
        new_entry = utils.iterated_ask(categories)
        identifier = categories[0]
        section[new_entry[identifier]] = new_entry
    except TypeError:
        print("Here's what's in this section:")
        [print(entry) for entry in section]
        if len(section) == 0:
            print("Whelp... there's nothing in here")
        q = "What would you like to add? "
        new_entry = input(q)
        section.append(new_entry)


def edit(section):
    try:
        entry = utils.entry_select(section, "Edit")
        q1 = "What subsection should be changed? "
        subsec = utils.option_regulator(section[entry], q1)
        # asks what subsection in the entry needs editing

        q2 = 'What should "{}" be changed to? '.format(subsec)
        new_subsec = input(q2)
        # asks for the new contents of the subsection

        diff_subsec = new_subsec != section[entry][subsec]
        # is the new content the same as the previous content

        section[entry][subsec] = new_subsec
        # sets the subsection to the new content

        if subsec == section["Format"][0] and diff_subsec:
            # checks if the subsection is the first one in the format and if new content is the same as previous

            new_entry = {}
            for category in section["Format"]:
                new_entry[category] = section[entry][category]
            identifier = section["Format"][0]
            section[new_entry[identifier]] = new_entry
            del section[entry]
            entry = new_entry[identifier]
        [print("{}: {}".format(category, section[entry][category])) for category in section[entry]]
    except AttributeError:
        q1 = "Which entry would you like to edit? "
        entry = utils.option_regulator(section, q1)
        section.remove(entry)
        q2 = 'What should "{}" be changed to? '.format(entry)
        new_entry = input(q2)
        section.append(new_entry)
        print("This is what the section now looks like: ")
        [print(entry) for entry in section]


def remove(section):
    """From the inputted section prompts user to select an entry to remove and double checks user choice"""
    q = "Are you sure you want to delete this entry? "
    try:
        entry = utils.entry_select(section, "Remove")
        print("This is the entry:")
        for subsec in section[entry]:
            print("{}: {}".format(subsec, section[entry][subsec]))
        if utils.option_regulator(utils.y_n, q) == "Yes":
            del section[entry]
            print("It has been done...")
        else:
            print("Wise choice not to forget your own history")
    except AttributeError:
        q_vlist = "What would you like to remove? "
        if len(section) != 0:
            del_entry = utils.option_regulator(section, q_vlist)
            if utils.option_regulator(utils.y_n, q) == "Yes":
                section.remove(del_entry)
                print("It has been done...")
            else:
                print("Wise choice not to forget your own history")
        else:
            print("Whelp...there's nothing to remove")


def view(section):
    try:
        entry = utils.entry_select(section, "Remove")
        print("This is the entry:")
        for subsec in section[entry]:
            print("{}: {}".format(subsec, section[entry][subsec]))
    except AttributeError:
        print("Here's all the entries in {}:".format(section))
        [print(entry) for entry in section]


# archive
