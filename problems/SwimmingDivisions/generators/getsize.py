nfiles = 12

"""
This file gets input data from all 12 inputs and outputs what the total size of the input is.
We need to calculate this, as the data is largely randomized
"""


for i in range(nfiles):  # Loop through file names 00.in to 14.in
    # Format the file name as "00.in", "01.in", ..., "14.in"
    filename = f"{i:02}.in"
    
    try:
        with open(filename, 'r') as file:  # Open the file for reading
            n = int(file.readline())
            for j in range(n):
                file.readline()

            n_comp_names = 0
            n_req_names = 0

            while True:
                line = file.readline()
                if line.find("END") != -1:
                    break

                linesplit = line.split()

                if line.find("COMPETITION") != -1:
                    n_comp_names += int(linesplit[1])
                    for j in range(int(linesplit[1])):
                        file.readline()
                elif line.find("REQUEST") != -1:
                    n_req_names += 1
                else:
                    print("Invalid line:", line)
                    break
        print("File:", filename)
        print("Number of competition names:", n_comp_names)
        print("Number of request names:", n_req_names)
        print("Number of total names:", n_comp_names + n_req_names, "10^", len(str(n_comp_names + n_req_names)))
        print()
    except FileNotFoundError:
        print(f"File {filename} not found.")