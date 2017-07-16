import csv
import os

class Product:

    def create_product_list(self):
    	csvfile=open('products.csv', 'w')
    	fieldnames = ['Product', 'Price']
    	product_list=[]
    	product_list.append({'Product': 'Vegetables', 'Price': '150'})
    	product_list.append({'Product': 'Fruits', 'Price': '350'})
    	product_list.append({'Product': 'Chocolates', 'Price': '200'})
    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    	writer.writeheader()
    	for r in product_list:
    		writer.writerow(r)
    	csvfile.close()

    def add_product(self,name,price):
    	product_list=[]
    	product_list.append({'Product' : name, 'Price' : price})
    	csvfile = open('products.csv','rw')
    	reader = csv.DictReader(csvfile)
    	for row in reader:
    		product_list.append(row)
    	csvfile.close()
    	csvfile = open('products.csv','w')
    	fieldnames = ['Product', 'Price']
    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    	writer.writeheader()
    	for r in product_list:
    		writer.writerow(r)
    	csvfile.close()

    def delete_product(self,name):
    	product_list=[]
        csvfile = open('products.csv','rw')
        reader = csv.DictReader(csvfile)
    	for row in reader:
    		if row['Product'] != name:
    			product_list.append(row)
    	csvfile.close()
    	csvfile = open('products.csv','w')
    	fieldnames = ['Product', 'Price']
    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    	writer.writeheader()
    	for r in product_list:
    		writer.writerow(r)
    	csvfile.close()

    def search_product(self,name):
        csvfile =open('products.csv')
        reader = csv.DictReader(csvfile)
    	for row in reader:
    		if row['Product'] == name:
    			return True
    		else:
    			continue
    	csvfile.close()
    	return False

    def update_product(self,name,price):
    	product_list=[]
        csvfile= open('products.csv','rw')
        reader = csv.DictReader(csvfile)
    	for row in reader:
    		if row['Product'] == name:
   				row['Price']=price
   				print(row)
   		product_list.append(row)
   		csvfile = open('products.csv','w')
   		fieldnames = ['Product', 'Price']
   		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   		writer.writeheader()
   		for r in product_list:
   			writer.writerow(r)
   		csvfile.close()

    def display_product(self):
        csvfile = open('products.csv')
        reader = csv.DictReader(csvfile)
        for row in reader:
        	print(row)
    	csvfile.close()

    def generate_bill(self):
    	bill_list=dict()
    	csvfile = open('products.csv','r')
    	reader = csv.DictReader(csvfile)
    	k=1
    	total_amount=0
    	while k==1:
    		p=input("Enter the product name:\n")
    		ans=self.search_product(p)
    		if ans==True:
    			q=input("Enter the quantity:\n")
    			a=self.find_price(p)
    			print(a)
    			ip=int(a)*q
    			bill_list[p]=ip
    			total_amount=total_amount+ip
    			k=input("Do you want to purchase more? (Yes : 1, No : 0 ) \n")
    		else:
    			print("Product Not available")
    			k=input("Do you want to purchase more? (Yes : 1, No : 0 ) \n")
    		print("Summary")
    		print("Product\tPrice\n")
    		for i in bill_list:
    			print(i+"\t"+str(bill_list[i])+"\n")
    		print("Total Amount = "+str(total_amount)+"\n")
    		csvfile.close()

    def find_price(self,name):
   		csvfile = open('products.csv','r')
   		reader = csv.DictReader(csvfile)
   		for row in reader:
   			if row['Product'] == name:
   				return row['Price']
   			else:
   				continue
   		csvfile.close()
   		return False


x=Product()
x.create_product_list()
while(1):
	print("Welcome to Superstore")
	print("Menu\n1.Add Product\n2.Delete Product\n3.Update Product\n4.Search Product\n5.Find Price\n6.Display Product\n7.Generate Bill\n8.Exit")
	c=input("Enter your choice\n")
	if c==1:
		p=input("Enter product name\n")
		str(p)
		a=input("Enter product price\n")
		str(a)
		x.add_product(p,a)
		continue
	elif c==2:
		p=input("Enter product name\n")
		x.delete_product(p)
		continue
	elif c==3:
		p=input("Enter product name\n")
		a=input("Enter product price\n")
		x.update_product(p,a)
		continue
	elif c==4:
		p=input("Enter product name\n")
		a=x.search_product(p)
		if a==True:
			print("Product Availabale\n")
		else:
			print("Product Unavailable\n")
		continue
	elif c==5:
		p=input("Enter product name\n")
		a=x.search_product(p)
		if a:
			x.find_price(p)
		else:
			print("Product Unavailable\n")
		continue
	elif c==6:
		x.display_product()
		continue
	elif c==7:
		x.generate_bill()
		continue
	elif c==8:
		print("Thank you for visiting Superstore\n")
		exit(0)