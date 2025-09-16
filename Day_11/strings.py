def check_nic(nic_number):
    if len(nic_number) != 11:
        return False

    if nic_number[:9].isdigit() and nic_number[-1].upper() == "V":
        return True


nic = "2003188000v"

if check_nic(nic):
    print("NIC Format is Correct")
else:
    print("NIC Format is Incorrect")