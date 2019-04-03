# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:55:42 2019

@author: harsh
"""
import sys
import os

def main():
    args = sys.argv[1:]
    if len(args)>3 or len(args) <3:
        print("Error: Takes only three arguments")
    else:
        try:
            order_products_file = args[0]
        except:
            print("order_products.csv not found")
        try:
            products_file = args[1]
        except:
            print("products.csv not found") 
        output_file = args[2] 
        if(os.path.isfile(output_file)):
            os.remove(output_file)
        print("Reading and processing {}".format(order_products_file))
        order_products_list=orderProducts(order_products_file)
        if(order_products_list):
            print("Reading and processing {}".format(products_file))
            products_list=Products(products_file)
            if(products_list):
                try:
                    print("Data processing in progress")
                    merged_df=mergeDataFrames(order_products_list,products_list) 
                    print("Preparing output file")
                    Report(merged_df,output_file)
                    print("File saved to {}".format(output_file))
                except:
                    print("Failed to generate output file")
            else:
                print("Failed to process products data")
        else:
            print("Failed to process order_products data")
        
    
def orderProducts(order_products_file):    
    order_products=[]
    try:
        with open(order_products_file,'r',encoding = "utf-8") as  f:    
            read_data=f.readlines()
            for i in range(1,len(read_data)):           
                try:
                    order_id=int(read_data[i].split(',')[0])
                except:
                    order_id=order_id
                try:
                    product_id=int(read_data[i].split(',')[1])
                except:
                    product_id='NA'
                try:
                    add_to_cart_order=int(read_data[i].split(',')[2])
                except:
                    add_to_cart_order='NA' 
                try:
                    reordered=int(read_data[i].split(',')[3])
                except:
                    reordered='NA'            
                order_products.append({"order_id":order_id,"product_id":product_id,
                                   "add_to_cart_order":add_to_cart_order,
                                   "reordered":reordered})        
            f.close()
    except :
        print("Failed to open Order_products file")
    return order_products


def Products(products_file):
    products=[]
    try:
        with open(products_file,'r',encoding = "utf-8") as  f1:    
            read_data=f1.readlines()
            for i in range(1,len(read_data)):
                try:
                    product_id=int(read_data[i].split(',')[0])
                except:
                    product_id='NA'
                try:
                    product_names=read_data[i].split(',')[1]
                except:
                    product_names='NA'
                try:
                    aisle_ids=int(read_data[i].split(',')[2])              
                except:
                    aisle_ids='NA' 
                try:
                    department_id=int(read_data[i].split(',')[3])
                except:
                    department_id='NA'
                products.append({"product_id":product_id,"Product_name":product_names,"aisle_ids":aisle_ids,"department_id":department_id})
        f1.close()
    except:
        print("Failed to open products file")
    return products


def mergeDataFrames(order_products_list,products_list):
    order_products_details=[]
    for i in range(0,len(order_products_list)):  
        for j in range(0,len(products_list)):
            if(order_products_list[i]['product_id']==products_list[j]['product_id']):
                order_products_list[i].update(products_list[j])
                order_products_details.append(order_products_list[i])            
    return sorted(order_products_details,key=lambda merged_df:merged_df['department_id'] )  


def Report(merged_df,output_file):
    number_of_orders={}
    number_of_first_orders={}
    percentage={}
    count_orders=0
    count=1
    for i in range(0,len(merged_df)):
        if(merged_df[i]['department_id'] not in number_of_orders):
            number_of_orders.update({merged_df[i]['department_id']:count})               
        else:
            number_of_orders.update({merged_df[i]['department_id']:count+1})
        if(merged_df[i]['department_id'] not in number_of_first_orders):
            number_of_first_orders.update({merged_df[i]['department_id']:count_orders})
        if(merged_df[i]['reordered']==0):
            number_of_first_orders.update({merged_df[i]['department_id']:count_orders+1})
    for key,value in number_of_orders.items():
        for key1,value1 in number_of_first_orders.items():
            if(key==key1):
                percentage.update({key:round((value1/value),2)})
    with open(output_file,'a') as f2:
        f2.write(str("department_id,number_of_orders,number_of_first_orders,percentage")+"\n")
        for key,value in number_of_orders.items():
            f2.write(str(key)+","+str(value)+","+str(number_of_first_orders[key])+","+str(percentage[key])+"\n")

    
if __name__ == "__main__":
    main()
    
