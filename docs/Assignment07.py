# ------------------------------------------------- #
# Title: Explore Pickling & Error Handling
# Description: A simple example of storing data in
#               a binary file and using exceptions
# ChangeLog: (Who, When, What)
# RRoot,<1.1.2030>,Created Starter Script
# CWei,2020.05.21,added pickle dump/load to Processing
# CWei, 2020.05.22,pseudocode
# CWei,2020.05.28,added except to check for .dat file
# CWei,2020.05.29,removed Try/Except from Add Customer
# CWei,2020.05.30,reused Mod06 IO func()
# CWei,2020.05.30,fixed display DB in Try/Except
# CWei,2020.05.31,relocated Try/Except to add func
#                 revise psuedocode and flow chart
#                 revise document, clean UI environment
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []
strChoice = ""      # from Mod6, get menu choice
strStatus = ""      # from Mod6, status of func
strCustomer = ""    # assign Customer
intID = ""         # assign ID


# Processing -------------------------------------- #

class Processes:
    """ Process functions """
    @staticmethod
    def add_new_data(nID, nCN, list_of_data):
        """Add new data to list

        :param nID:
        :param nCN:
        :param list_of_data:
        :return: (list)
        """
        row = {"ID": nID, "Customer": nCN}
        list_of_data.append(row)
        return list_of_data

    @staticmethod
    def save_data_to_file(file_name, list_of_data):
        # Added code 2020.05.21
        """ convert list as binary data

        :param file_name:
        :param list_of_data:
        :return:
        """
        objFile = open(file_name, "wb")
        pickle.dump(list_of_data, objFile)
        objFile.close()

    @staticmethod
    def read_data_from_file(file_name):
        # Added code 2020.05.21
        """ revert binary file to list

        :param file_name:
        :return: list of data
        """
        in_file = open(file_name, "rb")
        list_of_data = pickle.load(in_file)
        in_file.close()
        return list_of_data

# I/O --------------------------------------------- #
class IO:
    """ UI functions """
    @staticmethod
    def show_Menu():    # display Menu, from Mod6
        """" Display Menu options

        :return: (nothing)
        """
        print("""
            *************************************
            Please Choose an Option from Menu:
            1 - Add a Customer
            2 - Save List to database
            3 - View List
            4 - Exit
            *************************************
        """)
        print()

    @staticmethod
    def inp_fr_Menu():  # assign value for Menu option, from Mod6
        """ assign menu choice
        :return: (string)
        """
        choice = str(input("What would you like to do? [1-4]: "))
        print()
        return choice

    @staticmethod
    def inp_to_Cont(opt_msg=""):    # break/continue, from Mod6
        """ pause before continuing

        :return:
        """
        print(opt_msg)
        input("press the [Enter] key to continue")

    @staticmethod
    def new_Customer(list_of_data):     # add new customer
        """ New Entry w/ try/except

        :param list_of_rows:
        :return: (string)
        """
        nFLnm = str(input("Enter Customer First & Last name: "))
        nID = str(input("Enter 3 digit number for their ID [ex 123]: "))

        return nID, nFLnm

    @staticmethod
    def view_CustomerList(list_of_rows):    # view customer from list
        """ Displays list of Customers from ram

        :param list_of_rows:
        :return: (list) of Customers
        """
        print("""
        *************************************
        ID  | Customer Name
        -------------------------------------
        """)
        for i in list_of_rows:
           print("\t   " + i["ID"] + " | " + i["Customer"])
        # print(lstCustomer)
        print("""
        *************************************
        """)
        print()

    @staticmethod
    def dbl_Check(message):     # 'yes_no' module, from Mod06
        """ Confirm changes to session or data

        :param message:
        :return: (string)
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def close_SessWindow():
        """ Close prompt or interpreter
        :return: (nothing)
        """
        input("\n\tPress the [Enter] key to close the command prompt.")

# Presentation ------------------------------------ #
while True:
    IO.show_Menu()
    strChoice = IO.inp_fr_Menu()

    # Step 1:
    #   Get ID and NAME From user, then store it in a list object
    if strChoice == "1":
        (intID, strCustomer) = IO.new_Customer(lstCustomer)
        try:
            lstCustomer = Processes.read_data_from_file(strFileName)
        except IOError:     # except Error: if file not found, continue with ram data
            print("\n\tRemember to save your session.")
            print()
        else:
            print("\n\tCustomer added to database")
            print()
        print("\tYou have enter customer id for : " + strCustomer)
        Processes.add_new_data(intID, strCustomer, lstCustomer)

    # Step 2:
    #   Store list obj into a binary file
    if strChoice == "2":
        Processes.save_data_to_file(strFileName, lstCustomer)

    # Step 3:
    #   View List saved to dat file
    #   *********** try/except ***********
    #   try: reading from 'AppData.dat'
    if strChoice == "3":
        IO.view_CustomerList(lstCustomer)
        IO.inp_to_Cont(strStatus)

    # Step 4:
    #   Exit App
    if strChoice == "4":
        strChoice = IO.dbl_Check("Do you wish to save your Session? [y/n]: ")
        if strChoice.lower() == "y":
            Processes.save_data_to_file(strFileName, lstCustomer)
            print("\n\tSession saved.")
            break
        else:
            print("\tSession not saved.\n")
            break
IO.close_SessWindow()

