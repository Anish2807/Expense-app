from models import *


class MainApp():
    catList = []
    def startApp(self):
        while True:
            choice = self.printOptions()
            if choice == 1:
                self.addCategory()
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            elif choice == 7:
                pass
            elif choice == 8:
                break
        

    def printOptions(self):
        print("1. Add Category")
        print("2. Category Listing")
        print("3. Expense Entry")
        print("4. Report: Cat-wise")
        print("5. Report: Month-Year")
        print("6. Report: Amount")
        print("7. Report: MonthRange")
        print("8. Exit")
        ch = int(input("Enter your choice: "))
        return ch

    def addCategory(self):
        cid = int(input("Enter Category ID:"))
        cname = input("Enter Category Name: ")

        c = Category()
        c.setCatId(cid)
        c.setCatName(cname)

        MainApp.catList.append(c)
        print("Category Added!")
            


        


obj = MainApp()
obj.startApp()
