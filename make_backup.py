from utils import save, retrieve_data

data = retrieve_data("resume_data.txt")
save(data, "backup.txt")
