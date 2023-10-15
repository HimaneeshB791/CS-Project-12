import pickle

admin_data={'Samosa':50, 'Vada Pav':20, 'Pizza':200, 'Idli Sambar':250, 'Frankie':150, 'Burger':100,
            'French Fries':50, 'French Toast':300, 'Tea': 15, 'Coffee':20, 'Smoothie':50, 'Iced Soda':80}

preset_orders=[{'Customer_Name':'Max Euceda', 'Mobile_Number':9786746384, 'Order_ID':12, 'Samosa':2,
               'Pizza':1, 'Smoothie':1, 'Grand Total':350},
               {'Customer_Name':'Ronnie Coleman', 'Mobile_Number':6748593827,'Order_ID':14,
                'Vada Pav':2, 'Frankie':2, 'Tea':1, 'Grand Total':355}]

with open('Adminfile.dat','wb') as f:
    pickle.dump(admin_data,f)
print('Admin File Has Been Created Successfully')

with open('Counterfile.dat','wb') as fa:
    pickle.dump(preset_orders,fa)
print('Counter File Has Been Created Successfully')



        
        
        
    

