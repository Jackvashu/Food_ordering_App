import json
class Food_ordering_app:
    
    def __init__(self):     # Constructor
        self.menu_list = {1:{"name": "Tandoori Chicken", "price": 240, "quantity_type": "pieces", "quantity": 4, "discount": 40, "stock": 25 },
        2:{"name": "Vegan Burger", "price": 320, "quantity_type": "pieces", "quantity": 1, "discount": 40, "stock": 25 }, 
        3:{"name": "Truffle Cake", "price": 900, "quantity_type": "kg", "quantity": 1.0, "discount": 50, "stock": 25 }}
        self.food_id = len(self.menu_list)+1
        self.personal_details = {}
        
    # Admin Functionalities
    
    def add_food_item(self):  # adding food Item 
        self.item_name = input("Enter Food Item Name: ")
        self.quantity = int(input("Quantity please : "))
        self.quantity_type = input("Is This Quantity In Kgs or Pieces?")
        self.item_price = int(input("Enter the price in INR: "))
        self.discount = int(input("Enter the discount in INR: "))
        self.stock = int(input("Enter the stock available: "))
        self.item = {"name": self.item_name, "price": self.item_price, "quatity_type": self.quantity_type, "quantity": self.quantity, "discount": self.discount, "stock": self.stock }
        self.food_id = len(self.menu_list)+1
        self.menu_list[len(self.menu_list)+1] = self.item
        print("Item has been added successfully!")
        print(self.menu_list)
        
    def remove_item(self):
        id = int(input("Enter the food_id of the item you want to delete: "))
        del self.menu_list[id]
        print("Item deleted successfully!")
        print("Remaing Items are: \n",self.menu_list)
        
    def edit_item(self):
        id = int(input("Enter the food_id of the item you want to update: "))
        for i in self.menu_list[id]:
            self.menu_list[id][i] = input("Enter the {} you want to update".format(i))
        print("Food details updated successfully \n ",self.menu_list)
        
    def get_item(self):
        id = int(input("Enter to food_id of item you want to check"))
        print(self.menu_list[id])
        3
    def show_menu(self):
        print(" \n\n  ****  Food List  ****  ")
        print("\n")
        for i in self.menu_list:
            print("")
            print("food_id",i)
            print("=========")
            for j in self.menu_list[i]:
                print(j, " -- ", self.menu_list[i][j])
                
        
                
    # User functionalities           
                
            
    def register(self):
        try:
            self.full_name = input("Enter you Full Name: ")
            self.phone_no  = int(input("Enter you phone number: "))
            self.email = input("Enter you email address: ")
            self.address = input("Enter your address: ")
            self.username = input("Enter your username: ")
            self.password = input("Enter your password: ")
            self.personal_details = {"full name":self.full_name, "phone number": self.phone_no, "email": self.email, "address": self.address, "username": self.username, "password": self.password}
            f = open('personal_details.json')
            previous_data = json.load(f)
            f.close()
            previous_data[self.username]=self.personal_details
            with open("personal_details.json", "w") as outfile:
                json.dump(previous_data, outfile)
            print("\n  ****  Congratulations!! ****  ")
            print("\n You have successfully registered your account ")

        except:
            print("Invalid Input!")
            
            
    def login(self):
        while True:
            u_name = input("Enter your username: ")
            password = input("Enter your password: ")
            f = open("personal_details.json")
            data = json.load(f)
            u_data = data.get(u_name)    
            if data.get(u_name) and password == u_data.get("password"):
                print("You are successfully logged in!")
                self.personal_details = data.get(u_name)
                self.password = self.personal_details.get("password")
                self.username = self.personal_details.get("username")
                self.full_name = self.personal_details.get("full_name")
                self.phone_no = self.personal_details.get("phone_no")
                self.email = self.personal_details.get("email")
                self.address = self.personal_details.get("address")
                break
            else:
                print("Incorrect details, please try again")
            f.close()    
            
    def place_order(self):
        print("Here's the Menu: ")
        
        self.show_menu() 
        u_input =""
        while True: 
            u_input =  input("Enter the food_ids of the items you want to order separated by ',' in an array(example: [1,2,3]): ")
            if ('[' not in u_input) or (']' not in u_input):
                print("Enter valid data!")
            else:
                u_input=u_input.strip('"[]')
                break
        list_of_food_ids = u_input.split(',')
        
        print("Your order is \n") 
        
        for i in list_of_food_ids:
            item = self.menu_list.get(int(i))
            print("{} ({} INR for {} {})".format(item.get("name"),item.get("price"),item.get("quantity"),item.get("quantity_type") ))
        
        confirm_order = input("Do you want to confirm your order? (Enter 'Y' or 'N')") 
        
        if confirm_order == 'Y':
            list_of_order = []
            for i in list_of_food_ids:
                list_of_order.append(self.menu_list.get(int(i))) 
            f = open('order_history.json')
            previous_data = json.load(f)
            f.close()
            if previous_data.get(self.username):
                previous_data[self.username].append(list_of_order)
            else:
                previous_data[self.username] = []
                previous_data[self.username].append(list_of_order)
            
            with open("order_history.json", "w") as outfile:
                json.dump(previous_data, outfile)
            print("Thank you, you order has been confirmed Successfully!") 
        
        else: 
            print("Order cancelled!")
            
    def order_history(self):       
        f = open('order_history.json')
        data = json.load(f)
        f.close()
        if data.get(self.username):
            print("Your history of orders is \n")
            for i in data[self.username]:
                print(i)
        else:
            print("There is no history for your account!")
        

    def edit_personal_details(self):
        for i in self.personal_details:
            self.personal_details[i] = input("Enter the {} you want to update".format(i))
        f = open('personal_details.json')
        previous_data = json.load(f)
        f.close()
        previous_data[self.username]=self.personal_details
        with open("personal_details.json", "w") as outfile:
            json.dump(previous_data, outfile)
        print("Personal details updated successfully \n ",self.personal_details) 
        
    def show_personal_details(self):
        print("Your personal details are: ")
        for i in self.personal_details:
            print("{} : {}".format(i,self.personal_details.get(i)))
 


      
    def home_page(self):
        print("---------------  Welcome to the food ordering app!  ---------------")
        while True:
            print("\n **** Please enter your role.  ****")
            role = int(input("1. Admin \n2. user \n3. Exit \n"))
            if role == 1:
                while True:
                    print("\n **** Enter your preference:  ****")
                    admin_input = int(input(" \n1. Add new food item \n2. Edit a food item \n3. Remove a food item \n4. Show all food items \n5. Check a food item using food_id \n6. Exit \n"))
                    if admin_input == 1:
                        self.add_food_item()
                    elif admin_input == 2:
                        self.edit_item()
                    elif admin_input == 3:
                        self.remove_item()
                    elif admin_input == 4:
                        self.show_menu()   
                    elif admin_input == 5:
                        self.get_item()    
                    elif admin_input == 6:
                        break
            elif role == 2:
                new_user = input("Are you a new user? ('Y' or 'N')")
                if new_user == 'Y':
                    print("Register Your account!")
                    self.register()
                print("")
                print("Please Log in to your account")
                print("")
                self.login()
                while True:
                    user_input = int(input("Select an option below \n1. Place order\n2. Show order history\n3. Edit personal details \n4. check your personal details \n5. logout \n"))
                    if user_input == 1:
                        self.place_order()
                    elif user_input == 2:
                        self.order_history()
                    elif user_input == 3:
                        self.edit_personal_details()
                    elif user_input == 4:
                        self.show_personal_details()
                    elif user_input == 5:
                        print("Logged out successfully!")
                        break
            elif role == 3:
                print("Thank You!")
                break
                            

f = Food_ordering_app()
f.home_page()              


class FoodApp:
    
    def __init__(self) -> None:
        pass

    def Home_Page(self):
        print("")
        print("----------------  Welcome to the Food World  ----------------")
        print("---- Choose The option")
        print("1. Admin")
        print("2. User")
        print("3. exit")
        newInput = int(input("       : "))
        while True:
            if newInput == '1':    # for admin 
                pass
            elif newInput == '2':       # for new User
                print("1.New User \n 2. Exsiting User")
                newUser = input("Enter Choice : ")
                while True:
                    if newUser == '1':
                        fullName = input("Enter Full Name : ")
                        phoneNumber = int(input("Enter Phone number : "))
                        email = input("Enter Email Address : ")
                        userName = input("Enter User Name : ")
                        passWord = input("Enter Password : ")
                        
            elif newInput == '3':
                pass
            else:
                break

item = FoodApp()  # calling the food App class


