import json

d = {}


d["Work Experience"] = {"Format": ["Company",
                                   "Position",
                                   "Start Date",
                                   "Stop Date",
                                   "Description 1/5",
                                   "Description 2/5",
                                   "Description 3/5",
                                   "Description 4/5",
                                   "Description 5/5"]}

d["Projects"] = {"Format": ["Title",
                            "Start Date",
                            "Finish Date",
                            "Description 1/5",
                            "Description 2/5",
                            "Description 3/5",
                            "Description 4/5",
                            "Description 5/5"]}

d["Volunteer Experience"] = {"Format": ["Organization",
                                        "Position",
                                        "Start Date",
                                        "Stop Date",
                                        "Description 1/5",
                                        "Description 2/5",
                                        "Description 3/5",
                                        "Description 4/5",
                                        "Description 5/5"]}

d["Education"] = {"Format": ["Degree/Diploma",
                             "Institution",
                             "Start Date",
                             "Stop Date",
                             "GPA"]}

d["Mechanical Design"] = []

d["Programming"] = []

d["Prototyping"] = []

d["Related Courses"] = []

d["Certificates"] = {"Format": ["Title",
                                "Institution"]}

d["Awards"] = {"Format": ["Title",
                          "Organization"]}

d["Languages"] = []

d["Interests"] = []


with open("resume_data.txt", "w") as final:
    final.write(json.dumps(d, indent=4))
