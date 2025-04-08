def log_message(massage, filename="logfile.txt"):
    with open(filename, "a") as file:
        file.write(massage + "\n")