def writer(data: dict)->None:
    """
    Write the data to a file.
    """
    with open('/home/alokrkmv/Documents/walmart_backend_assignment/dataset/output.txt', 'w') as f:
        for key, value in data.items():
            if value == "Invalid Reservation" or value == "House full":
                f.write(f"{key} {value}\n")
            else:
                val = ", ".join(value)
                f.write(f'{key} {val}\n')