with open("names.csv", "r") as name_file:
    csv_data = name_file.read().splitlines()


    for line in csv_data:
        splitted_names = line.split(",")
        print((splitted_names[0]) + " is " + (splitted_names[1]) + " years old and " + (splitted_names[2]))



