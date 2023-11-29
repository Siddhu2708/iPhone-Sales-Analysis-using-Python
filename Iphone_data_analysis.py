
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

iphone = pd.read_csv("iphone_data.csv")
# top 10 rating iphone list
highest_rated = iphone.sort_values(by=["Star Rating"], ascending=False)
highest_rated = highest_rated.head(10)
print(highest_rated.describe())
print(iphone.isnull())

def product_rating():
    apple = highest_rated["Product Name"]
    count = highest_rated["Number of Ratings"]
    figure = px.bar(highest_rated, x=apple, y=count, color="Star Rating", title="Number of Ratings of Highest Rated Iphone")
    figure.show()

def product_review():
    apple = highest_rated["Product Name"]
    count = highest_rated["Number of Reviews"]
    figure = px.bar(highest_rated, x=apple, y=count, color="Star Rating", title="Number of Reviews of Highest Rated Iphone")
    figure.show()

def product_sale():
    apple = highest_rated["Product Name"]
    count = highest_rated["Sale Price"]
    figure = px.bar(highest_rated, x=apple, y=count, color="Product Name", title="Sale Price of Highest Rated Iphone")
    figure.show()

def sale_review():
    figure = px.bar(data_frame=iphone, x="Sale Price", y="Number of Reviews", color="Product Name", title="Relationship between Sale Price and Number of Reviews of Iphone")
    figure.show()

def sale_rating():
    apple = highest_rated["Product Name"]
    figure = px.bar(data_frame=iphone, x="Sale Price", y="Number of Ratings", color="Product Name", title="Relationship between Sale Price and Number of Ratings of Iphone" )
    figure.show()

while True:
    print("\n\t\t\t\t\t ---------------------------- IPhone Data Analysis------------------------------")
    print("\t\t\t\t\t| 1.Display the Top 10 Iphone Rated Phone\t\t\t\t\t\t\t\t\t\t|")
    print("\t\t\t\t\t| 2.Display the Number of Ratings of Highest Rated Iphone\t\t\t\t\t\t|")
    print("\t\t\t\t\t| 3.Display the Number of Reviews of Highest Rated Iphone\t\t\t\t\t\t|")
    print("\t\t\t\t\t| 4.Display the Sale Price of Highest Rated Iphone\t\t\t\t\t\t\t\t|")
    print("\t\t\t\t\t| 5.Display the Relationship between Sale Price and Number of Reviews of Iphone\t|")
    print("\t\t\t\t\t| 6.Display the Relationship between Sale Price and Number of Ratings of Iphone\t|")
    print("\t\t\t\t\t| 7.Exit \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t\t\t\t\t -------------------------------------------------------------------------------")
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        print(highest_rated)
    elif choice == 2:
        product_rating()
    elif choice == 3:
        product_review()
    elif choice == 4:
        product_sale()
    elif choice == 5:
        sale_review()
    elif choice == 6:
        sale_rating()
    elif choice == 7:
        break
    else:
        print("Enter Correct the operation!")



