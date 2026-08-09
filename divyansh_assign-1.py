
products = [
    {
        "name":"mouse",
        "price":1000,
        "stock":3
    },
    {
        "name":"keyboard",
        "price":2000,
        "stock": 4
    },
    {
        "name":"pendrive",
        "price":1500,
        "stock":5
    }
]
def calculate_total_inventory_value():
    tsum=0
    for item in products:
       total_price= item['price']*item['stock'] 
       tsum = tsum+total_price
    return tsum
total_val = calculate_total_inventory_value()
print(f"Toal Inventory Value:{total_val}")
try:
    with open("inventory_report.txt","w") as file:
        file.write(f"This is total value:{total_val}\n")

    with open("inventory_report.txt","r") as file:
        val = file.read()
        print("File Content->",val)
except Exception as e:
    print(f"Somthing went worng:{e}")
    
