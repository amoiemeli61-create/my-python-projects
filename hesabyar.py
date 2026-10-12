# ===تنظیمات اولیه===
import datetime
import json

orders = []
purchase_list = []
save_total = []
order_sum = 0
total = 0
customers = []
products = []

business_name = input("Enter your business name: ")
print("Welcome to", business_name)

while True:
    product_name = input("Enter product name: ")
    product_price = int(input("Enter product price: "))
    save = [product_name, product_price]
    products.append(save)
    # وقتی کاربر N میزنه از برنامه خارج شه
    another = input("Do you have another product (y/n): ")
    if another[0] == "n" or another[0] == "N":
        break

for i in products:
    print(i)

while True:
    print(
        "^_^Hesabyar^_^"
        "\n"
        "1.Manage products"
        "\n"
        "2.Manage Customers"
        "\n"
        "3.Register order"
        "\n"
        "4.Report Profit/Loss"
        "\n"
        "5.Save to File"
        "\n"
        "6.Exit"
    )
    choice = int(input("Enter your choice? "))

    # ===مدیریت محصولات===
    if choice == 1:
        while True:
            print(
                "===Manage products==="
                "\n"
                "1.Add products"
                "\n"
                "2.View products"
                "\n"
                "3.Delete product"
                "\n"
                "4.Edit product"
                "\n"
                "5. Back to main menu"
            )
            manage_choice = int(input("Your choice:"))

            if manage_choice == 1:
                new_product_name = input("Enter new product: ")
                new_product_price = int(input("Enter new price: "))
                save2 = [new_product_name, new_product_price]
                products.append(save2)

            elif manage_choice == 2:
                for i in products:
                    print(i)

            elif manage_choice == 3:
                delete_mode = input("Delete by name or price? (n/p): ")
                found = False
                if delete_mode == "n":
                    name = input("Enter product name? ")
                    for i in products:
                        if name == i[0]:
                            found = True
                            products.remove(i)
                            break
                elif delete_mode == "p":
                    price = int(input("Enter price product? "))
                    for i in products:
                        if price == i[1]:
                            found = True
                            products.remove(i)
                            break
                if found == True:
                    print("Found!")
                else:
                    print("not Found!")

            elif manage_choice == 4:
                edit_mood = input("Edit by name or price:(n/p)? ")
                if edit_mood == "n":
                    edit = input("Which product do you want to edit? ")
                    for i in products:
                        if edit == i[0]:
                            edit_new = input("Enter new product name: ")
                            i[0] = edit_new
                            break
                if edit_mood == "p":
                    edit2 = int(input("Enter product price to edit: "))
                    for i in products:
                        if edit2 == i[1]:
                            edit_new2 = int(input("Enter new product price? "))
                            i[1] = edit_new2
                            break

            elif manage_choice == 5:
                break

    # ===مدیریت مشتریان===
    if choice == 2:
        while True:
            print(
                "===Manage Customers==="
                "\n"
                "1.Add Customer"
                "\n"
                "2.view Debts"
                "\n"
                "3.Settle Debt"
                "\n"
                "4.Back to Main Menu"
            )
            selection = int(input("Enter your selection? "))

            if selection == 1:
                while True:
                    customer_Name = input("Enter customer name: ")
                    customer_Phone_Number = input("Enter customer phone number: ")
                    customer_debt = int(input("Enter customer debt: "))
                    customer_date = datetime.datetime.now()
                    Settlement_Date = None
                    save_customer = [
                        customer_Name,
                        customer_Phone_Number,
                        customer_debt,
                        customer_date,
                        Settlement_Date,
                    ]
                    customers.append(save_customer)
                    exit_customers = input(
                        "Do you want to add another customer? (y/n): "
                    )
                    if exit_customers == "n":
                        break

            if selection == 2:
                for i in customers:
                    n = i[0], i[2]
                    print(n)

            if selection == 3:
                found = False
                Settle = input("Enter debtor name: ")
                for i in customers:
                    if Settle == i[0]:
                        found = True
                        print(i[0], "debt was", i[2])
                        i[2] = 0
                        settlement_Date = datetime.datetime.now()
                        i[4] = settlement_Date
                        print("Settlement Date: ", i[4])
                        break
                if found == True:
                    print("Debt settled✅")
                else:
                    print("Customer not found!")

            if selection == 4:
                break

    # ===ثبت سفارش===
    if choice == 3:
        customer = ""
        print(
            "1.Select Customer"
            "\n"
            "2.Select Product and Quantity"
            "\n"
            "3.Calculate Total Order Amount"
            "\n"
            "4.Select Payment Type (Cash/Credit)"
            "\n"
            "5.Exit"
        )
        while True:
            order_choice = int(input("Enter your choice: "))

            if order_choice == 1:
                customer = input("Enter Customer Name: ")
                yes = False
                for i in customers:
                    if i[0] == customer:
                        yes = True
                if yes == True:
                    print("Yes")
                else:
                    print("No")

            if order_choice == 2:
                while True:
                    Product = input("Enter product name from the list: ")
                    exit3 = "y"
                    for i in products:
                        if i[0] == Product:
                            quantity = int(input("How many units do you want?"))
                            exit3 = input("Do you want to add another product? (y/n):")
                            chosen_products = (Product, quantity)
                            purchase_list.append(chosen_products)
                    if exit3 == "n":
                        break

            if order_choice == 3:
                order_sum = 0
                for i in products:
                    for j in purchase_list:
                        if i[0] == j[0]:
                            total = i[1] * j[1]
                            order_sum += total
                    print(order_sum)
                order_date = datetime.datetime.now()
                order_info = [order_date, order_sum]
                orders.append(order_info)

            if order_choice == 4:
                cash_credit = int(input("Enter payment type (1:Cash/2:Credit): "))
                if cash_credit == 1:
                    print("Debt paid successfully!")
                if cash_credit == 2:
                    for i in customers:
                        if i[0] == customer:
                            i[2] += order_sum
                            break

            if order_choice == 5:
                break

    # ===گزارش سود و زیان===
    if choice == 4:
        while True:
            print(
                "=== Report ==="
                "\n"
                "1. Daily Report"
                "\n"
                "2. Monthly Report"
                "\n"
                "3. Yearly Report"
                "\n"
                "4. Total Sales"
                "\n"
                "5. Back to Main Menu"
            )
            report = int(input("Enter your choice: "))

            if report == 1:
                daily_total = 0
                today_date = datetime.datetime.now().date()
                for i in orders:
                    if today_date == i[0].date():
                        daily_total += i[1]
                print(daily_total)

            if report == 2:
                monthly_total = 0
                month_date = datetime.datetime.now().month
                for i in orders:
                    if month_date == i[0].month:
                        monthly_total += i[1]
                print(monthly_total)

            if report == 3:
                year_total = 0
                year_date = datetime.datetime.now().year
                for i in orders:
                    if year_date == i[0].year:
                        year_total += i[1]
                print(year_total)

            if report == 4:
                all_orders_total = 0
                for i in orders:
                    all_orders_total += i[1]
                print(all_orders_total)

            if report == 5:
                break

    # ===ذخیره در فایل===
    if choice == 5:
        save_file = [products, customers, orders]
        with open("hesabyar.json", "w") as file:
            json.dump(save_file, file, default=str)

    # ===خروج===
    if choice == 6:
        break
