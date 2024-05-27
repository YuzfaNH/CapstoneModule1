# PROJECT CAPSTONE MODULE ! - DATA KARYAWAN


# data_dict
employee_list = [{'Employee ID': 769001,'Name' : 'John','DOB' : '12/12/1970','Job Title' : 'Pilot','Phone Number' : '0812111111','Status' : 'Active'}, 
{'Employee ID': 769002,'Name' : 'Ben','DOB' : '18/2/1979','Job Title' : 'Co-Pilot','Phone Number' : '0812111111','Status' : 'Active'},
{'Employee ID': 769003,'Name' : 'Anton','DOB' : '11/2/1981','Job Title' : 'Co-Pilot','Phone Number' : '0812111111','Status' : 'Active'},
{'Employee ID': 769004,'Name' : 'Pascal','DOB' : '10/9/1981','Job Title' : 'Cargo Mgr','Phone Number' : '0812111111','Status' : 'Active'},
{'Employee ID': 769005,'Name' : 'Nadia','DOB' : '13/11/1991','Job Title' : 'Flight Attendant','Phone Number' : '0812111111','Status' : 'Active'},
{'Employee ID': 769006,'Name' : 'Brenda','DOB' : '21/3/1987','Job Title' : 'Flight Attendant','Phone Number' : '0812111111','Status' : 'Active'},
{'Employee ID': 769007,'Name' : 'Dedy','DOB' : '18/8/1972','Job Title' : 'Maintenance','Phone Number' : '0812111111','Status' : 'Active'},
{'Employee ID': 769008,'Name' : 'Frans','DOB' : '11/6/1980','Job Title' : 'Passenger Traffic','Phone Number' : '0812111111','Status' : 'Active'},]
    
# Function Delete Employees
def delete():
    print('\n-----Terminate Employee Data Record-----\n')
    print(' 1. Delete Employee data')    
    print(' 0. Return to Menu')
    submenu_choice = int(input('Pick menu (1~0): '))
    if submenu_choice == 0:
        return menu()
    elif submenu_choice == 1:
        del_id = int(input('Please input Employee ID Number you wish to delete: '))
        for i in range(len(employee_list)):
            # ID Exist untuk menentukan dalam looping, jika ID yang dicari ada/tidak
            id_exist = False
            if del_id == employee_list[i]['Employee ID']:
                id_exist = True
                print('\nEmployee Data Found!\n')
                print (employee_list[i])
                delconf = input('Do you want to delete this data (Yes/No)? ').lower()
                if delconf == 'yes':
                    del employee_list[i]
                    print('Data Deleted!\n')
                    print('-------------------------------------Employee Lists----------------------------------------------------\n')
                    print('Employee ID\t     | Name  \t    | DOB\t\t    | Job Title\t    | Phone Number\t    | Status\t     |')
                    for i in range(len(employee_list)) :
                        print('{}\t\t| {}\t\t     | {}\t      | {}   \t      | {}\t       | {}\t\t     |\n'.format(employee_list[i]['Employee ID'],employee_list[i]['Name'],employee_list[i]['DOB'],employee_list[i]['Job Title'],employee_list[i]['Phone Number'],employee_list[i]['Status']))
                    input('Press Enter to Return')
                    return delete()
                elif delconf == 'no':
                    print('Data Deletion Cancelled')
                    return delete()
        if not id_exist:
            print('No data found!')
            return delete()           


    

# Update Data Function
def update():
    data_change = {}
    print('\n-----Update Employee Data Record-----\n')
    print(' 1. Change Employee data')
    print(' 0. Return to Menu')
    submenu_choice = int(input('Pick menu (1~0): '))
    if submenu_choice == 0:
        return menu()
    elif submenu_choice == 1:
        id = int(input('Employee ID: '))
        for i in range(len(employee_list)):
            id_exist = False
            if id == employee_list[i]['Employee ID']:
                id_exist = True
                print('\nEmployee Data Found!\n')
                print (employee_list[i])
                updconf = input('Is the data correct? ').lower()
                if updconf == 'yes':
                    print('\nInput the data you wish to change\n(Leave it blank if you dont wish to change)')
                    nname = input('\n1. Change Name ')
                    ndob = input('2. Change Date of Birth ')
                    ntitle = input('3. Change Title/Position ')
                    ncontact = input('4. Change Contact ')
                    nstatus = input('5. Change Status ')
                    
                    data_change['Name'] = nname
                    data_change['DOB'] = ndob
                    data_change['Job Title'] = ntitle
                    data_change['Phone Number'] = ncontact
                    data_change['Status'] = nstatus

                    datafix = {key:val for key,val in data_change.items() if val != ''}
                    print('Following data will be change')
                    print(datafix)
                    updconf2 = input('Confirm Data Update(Yes/No): ')
                    if updconf2 == 'yes':
                        employee_list[i].update(datafix)
                        print('Data Sucessfully Updated!\n')
                        print('\n-------------------------------------Employee Lists----------------------------------------------------\n')
                        print('Employee ID\t    | Name  \t     | DOB\t\t     | Job Title\t    | Phone Number\t|     Status\t     |')
                        for i in range(len(employee_list)) :
                            print('{}\t\t    | {}\t\t   | {}\t    | {}   \t| {}\t   | {}\t\t    |'.format(employee_list[i]['Employee ID'],employee_list[i]['Name'],employee_list[i]['DOB'],employee_list[i]['Job Title'],employee_list[i]['Phone Number'],employee_list[i]['Status']))
                        input('Press Enter to Return')
                        return menu()
                    elif updconf2 == 'no':
                        print('Update cancelled')
                        return update()
                    else:
                        print('Invalid! Returning to menu')
                        return menu()
                elif updconf == 'no':
                    return(update)
                else:
                    print('Invalid! Returning to menu')
                    return menu()            
        if not id_exist:
            print('No data')
            return update()
                    

# ADD FUNCTION
def add():
    print('\n------New Employee Portal----------------\n')
    print(' 1. Add New Employee')
    print(' 0. Return to Menu')
    new_employee = {}
    submenu_choice = int(input('Pick menu (1~0): '))
    if submenu_choice == 0:
        return menu()
    elif submenu_choice == 1:
        add_id = int(input('Input New Employee ID: '))
        id_exist = False
        for n in range(len(employee_list)):
            if add_id == employee_list[n]['Employee ID']:
                id_exist = True
                print('ID already exist!')
                input('Press Enter to Return')
                return add()
            
        if not id_exist:
            print('Employee ID not found!\n')
            new_name = input('Name: ')
            new_dob = input('DOB: ')
            new_job_title = input('Job Title: ')
            new_phone_number = input('Phone Number: ')
            new_employee['Name'] = new_name
            new_employee['DOB'] = new_dob
            new_employee['Job Title'] = new_job_title
            new_employee['Phone Number'] = new_phone_number
            new_employee['Status'] = 'Active'

            print(new_employee)
            conf = input('\nIs the data correct? \n').lower()
            if conf == 'yes':
                print('\nData registered sucessfully!\n')
                employee_list.append({'Employee ID' : add_id, 'Name' : new_name, 'DOB' : new_dob, 'Job Title' : new_job_title, 'Phone Number' : new_phone_number, 'Status' : 'Active'})
                print('\n-------------------------------------Employee Lists----------------------------------------------------\n')
                print('Employee ID\t| Name  \t| DOB\t\t| Job Title\t| Phone Number\t| Status\t|')
                for i in range(len(employee_list)) :
                    print('{}\t\t| {}\t\t| {}\t| {}   \t| {}\t| {}\t\t|'.format(employee_list[i]['Employee ID'],employee_list[i]['Name'],employee_list[i]['DOB'],employee_list[i]['Job Title'],employee_list[i]['Phone Number'],employee_list[i]['Status']))
                    
            else:
                return add()
    input('Press Enter to Return')
    return add()


# SEARCH FUNCTION/SHOW
def search():
    print('\n-----Search Employee Data Record-----\n')
    print(' 1. Search Employee')
    print(' 0. Return to Menu')
    submenu_choice = int(input('Pick menu (1~0): '))
    if submenu_choice == 0:
        return menu()
    elif submenu_choice == 1:
        id = int(input('Employee ID: '))
        search_id = ([data for data in employee_list if data['Employee ID'] == id])
        if search_id == []:
            print ('\nEmployee ID Does not Exist!\n')
            print('-------------------------------------Employee Lists----------------------------------------------------\n')
            print('Employee ID\t     | Name  \t         | DOB\t\t      | Job Title\t     | Phone Number\t    | Status\t    |')
            for i in range(len(employee_list)) :
                print('{}\t\t     | {}\t\t     | {}\t     | {}   \t     |  {}\t       |      {}\t\t       |'.format(employee_list[i]['Employee ID'],employee_list[i]['Name'],employee_list[i]['DOB'],employee_list[i]['Job Title'],employee_list[i]['Phone Number'],employee_list[i]['Status']))
        else:
            print('\nEmployee Data Found!\n')
            print (search_id)
            

        
        return search_cont()

                      
def search_cont():
     print('\n\n-----Search Employee Data Record-----\n')
     id_cont = input('Would you like to search another data(Yes/No)? ').lower()
     if id_cont == 'yes':
         return search()
     else:
         return menu()

     

# Opening MENU
def menu():
    print('\n-----List karyawan PT. X Airlines--------')
    print('')
    print('1. Search Employee data')
    print('2. Add Employee data')
    print('3. Change Employee data')
    print('4. Delete Employee data')
    print('5. Done/Exit')
    
    menu_choice = int(input('Choose action: '))
    if menu_choice == 1:
        search()
    elif menu_choice == 2:
        add()
    elif menu_choice == 3:
        update()
    elif menu_choice == 4:
        delete()
    elif menu_choice == 5:
        exitconf = input('Are you sure (Yes/No)? ').lower()
        if exitconf == 'yes':
            exit()
        elif exitconf == 'no':
            return menu()
        else:
            print('Error!')
            return menu()


menu()





