import pickle
import json
import random


def A_adder():
    with open('Adminfile.dat','rb+') as f:
        print('*'*20,'Adding New Item Data','*'*20)
        rec=pickle.load(f)
        ans='y'
        while True:
            Item=input('Enter item name')
            price=int(input('Enter price'))
            rec[Item]=price
            ans=input('Another item?(y/n)')
            if ans=='y':
                continue
            else:
                print('*'*20,'Data added','*'*20)
                print(rec)
                break
                
    with open('Adminfile.dat','wb') as f:
        pickle.dump(rec,f)
        
def A_displayer():
    f=open('Adminfile.dat','rb')
    show=pickle.load(f)
    new=json.dumps(show,indent=6)
    print(new)
    f.close()

def A_editer():
    with open('Adminfile.dat', 'rb+') as f:
        print('*'*20,'Editing Existing Item Data','*'*20)
        rec=pickle.load(f)
        print(rec)
        ans='y'
        while True:
            new=input('Enter item name to edit')
            if new in rec:
                print('Item already in records, enter price to modify')
                pr=int(input('Enter price'))
                rec[new]=pr
            else:
                print('Item not in records')
            ans=input('Another Item? (y/n)')
            if ans=='y':
                continue
            else:
                print('*'*20,'Data modified','*'*20)
                break
    with open('Adminfile.dat','wb') as f:
        pickle.dump(rec,f)

def A_deleter():
    with open('Adminfile.dat', 'rb+') as f:
        print('*'*20,'Deleting Item Data','*'*20)
        rec=pickle.load(f)
        print(rec)
        ans='y'
        while True:
            new=input('Enter item name to delete')
            if new in rec:
                print('Item found in records')
                del rec[new]
            else:
                print('Item not in records')
            ans=input('Another Item? (y/n)')
            if ans=='y':
                continue
            else:
                print('*'*20,'Data deleted','*'*20)
                break
    with open('Adminfile.dat', 'wb') as f:
        pickle.dump(rec,f)

def A_searcher():
    f=open('Adminfile.dat','rb')
    print('*'*20,'Search Existing Records','*'*20)
    rec=pickle.load(f)
    print(rec)
    while True:
        target=input("Enter item name to be search:")
        if target in rec:
            print('Item found')
            print('Item Name:',target,'Price:',rec[target])
        else:
            print('Item not found')
        ans=input('Another Item(y/n)')
        if ans=='y':
            continue
        else:
            break

def C_placeorder():
    f=open("Counterfile.dat","rb")
    fa=open('Adminfile.dat','rb')
    data=pickle.load(f)
    dat=pickle.load(fa)
    rec={}
    print('*'*20,'Placing New Order','*'*20)
    cust_name=input("Enter name of customer:")
    mob_no=int(input("Enter mobile no. :"))
    print('Order Id:', random.randint(10,99))
    copy=int(input('Please re-enter the order ID'))
    rec['Customer_Name']=cust_name
    rec['Mobile_Number']=mob_no
    rec['Order_ID']=copy
    price=0
    while True:
        item=input("Enter item name:")
        if item in dat:
            qty=int(input("Enter quantity:"))
            rec[item]=qty
            price+=qty*dat[item]
        else:
            print('Item not available')
        ch=input("Do you want to order more items (y/n)?:")
        if ch=='y':
            continue
        else:
            break
    rec['Grand Total']=price
    bill=json.dumps(rec, indent=6)
    print(bill)
    data.append(rec)
    with open('Counterfile.dat','wb') as f:
        pickle.dump(data,f)
    print('*'*20,'Order Placed Successfully','*'*20)

def C_showorder():
    print('*'*20,'View Previous Orders','*'*20)
    f=open('Counterfile.dat','rb')
    rec=pickle.load(f)
    new=json.dumps(rec,indent=6)
    print(new)
    f.close()

def C_cancelorder():
    f=open('Counterfile.dat','rb')
    data=pickle.load(f)
    print('*'*20,'Delete Previous Orders','*'*20)
    target=int(input('Enter the order ID to delete'))
    for i in data:
        if i['Order_ID']==target:
            data.remove(i)
            print('Order Deleted')
            break
    else:
        print('*'*20,'Order Not Found','*'*20)
    with open('Counterfile.dat','wb') as f:
        pickle.dump(data,f)



ch='Y'
while ch=='Y':
    print('''1. Admin Login
2. Customer Login''')
    ch=int(input("Enter your choice:"))
    if ch==1:
        pwd=input('Enter password:')
        if pwd =='Admin@123':
             print('You Are Logged In Successfully')
             while True:
                 print('*'*20,'Menu','*'*20)
                 print('''1. Add records
2. Display records
3. Search records
4. Modify records
5. Delete record
6. Exit''')
                 choice=input('Enter choice 1-6:')
                 if choice=='1':
                     A_adder()
                 elif choice=='2':
                     A_displayer()
                 elif choice=='3':
                     A_searcher()
                 elif choice=='4':
                     A_editer()
                 elif choice=='5':
                     A_deleter()
                 elif choice=='6':
                     break
                 else:
                     print('Enter valid choice')
        else:
            print("Enter correct password")
    elif ch==2:
        pwd=input('Enter password:')
        if pwd =='Custom@123':
            print('You Are Logged In Successfully')
            while True:
                print('*'*20,'The Menu','*'*20)
                print('''1. Place Order
2. Show order
3. Cancel order
4. Exit''')
                choice=input("Enter choice 1-4 : ")
                if choice=='1':
                    A_displayer()
                    C_placeorder()
                elif choice=='2':
                    C_showorder()
                elif choice=='3':
                    C_cancelorder()
                elif choice=='4':
                    break
                else:
                    print('Enter valid choice')
        else:
            print("Enter correct password")
             











    
