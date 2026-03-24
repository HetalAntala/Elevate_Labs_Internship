import time

def monitor_files(file_paths, callback):
    files = []

    # Open all files
    for path in file_paths:
        f = open(path, "r")
        
        # 🔥 READ EXISTING LOGS FIRST
        for line in f:
            callback(line)

        files.append(f)

    print("\n[+] Monitoring logs in real-time...\n")

    while True:
        for f in files:
            line = f.readline()
            if line:
                callback(line)

        time.sleep(1)