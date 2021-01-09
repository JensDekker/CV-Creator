from utils import save, retrieve_data

data = retrieve_data("backup.txt")
save(data, "resume_data.txt")
