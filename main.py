print("Welcome to Matt's Fiber Optic Cable Outlet")
company_name = input("Please enter your company name:")
cable_feet = input("Please enter how many feet of fiber optic cable you wish to purchase:")
cable_feet = int(cable_feet)
total_cost = cable_feet * .99 #calculates feet of cable required by the cost of $.99
total_cost = '${:,.2f}'.format(total_cost) #converts total_cost to dollar format
print(f"{company_name}, the total cost for the installation of {cable_feet} feet of cable is: {total_cost}")
input("Press return to exit ") #stops the program from closing immediately after displaying the output and allows the user to manually exit