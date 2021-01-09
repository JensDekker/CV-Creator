import utils
import data

cv_data = utils.retrieve_data("resume_data.txt")
sections = [section for section in cv_data]

working = True
while working:
    q1 = "Which section would you like to access? "
    r1 = utils.option_regulator(sections, q1)
    current_section = True
    while current_section:
        q2 = "What would you like to do in {}? ".format(r1)
        interactions = ["Create", "Edit", "Remove", "View", "Archive"]
        r2 = utils.option_regulator(interactions, q2)

        q3 = "Would you like to {} more entries? ".format(r2.lower())
        while r2 == "Create":
            data.add(cv_data[r1])
            r3 = utils.option_regulator(utils.y_n, q3)
            if r3 == "No":
                break
        while r2 == "Edit":
            data.edit(cv_data[r1])
            r3 = utils.option_regulator(utils.y_n, q3)
            if r3 == "No":
                break
        while r2 == "Remove":
            data.remove(cv_data[r1])
            r3 = utils.option_regulator(utils.y_n, q3)
            if r3 == "No":
                break
        while r2 == "View":
            data.view(cv_data[r1])
            r3 = utils.option_regulator(utils.y_n, q3)
            if r3 == "No":
                break
        while r2 == "Archive":
            print("Under construction")
            break
        q4 = "Would you like to continue working in {}? ".format(r1)
        r4 = utils.option_regulator(utils.y_n, q4)
        if r4 == "No":
            break
    q5 = "Would you like to continue using the program? "
    r5 = utils.option_regulator(utils.y_n, q5)
    if r5 == "No":
        break

utils.save(cv_data, "resume_data.txt")
print("Thank you for using the program!")
