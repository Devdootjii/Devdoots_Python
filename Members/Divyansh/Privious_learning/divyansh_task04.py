#Day 4 Dictionaries & Sets
#Name : Divyansh
#what i learnd : Dictionaries and sets
#where i stuck : opretion at dict

loyalty_db={
    "C101":150,
    "C102":320,
    "C103":80,
    "C104":500
}
Cate_list=['Electronics', 'Fashion', 'Home', 'Books','Books']
unique_cat=set(Cate_list)
loyalty_db["C105"]=200
loyalty_db["C101"]=loyalty_db["C101"]+50


print(f"""CUSTOMER LOYALTY & CATEGORY AUDIT

Total Customers Registered: {len(loyalty_db)}
Unique Store Categories: {unique_cat}
Customer C102 Points: {loyalty_db.get("C102",0)}
Updated Customer C101 Points: {loyalty_db.get('C101',0)}
Total System Loyalty Points: {sum(loyalty_db.values())}
Audit Status: SUCCESSFUL
""")
