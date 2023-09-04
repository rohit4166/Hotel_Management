import datetime
class hotel:
    def home1(self):
        import mysql.connector as con
        
        
        ad=con.connect(host='localhost',user='root',password='root')
        self.cur=ad.cursor()
        try:
            self.cur.execute('create database db28')
            print(' Your Database Is Created Successfully...')
            print()
            print()
            self.ad=con.connect(host='localhost',user='root',password='root',database='db28')
            self.cur=self.ad.cursor()
            h1.home()
        except Exception:
            self.ad=con.connect(host='localhost',user='root',password='root',database='db28')
            self.cur=self.ad.cursor()
            print(' Your Database Is In Ready Position Successfully...')
            print()
            print()
       
            h1.home()
        
    def home(self):
        y=datetime.datetime.now()
        self.z=str(y.strftime("%x"))
        try:
            a= "create table table1(Name varchar(100),Id varchar(20),Phno varchar(25),Address varchar(100),Date varchar(20))"
            self.cur.execute(a)
            self.ad.commit()
        except Exception:
            pass
         
        input('Press Any key To Cont...')
        print()
        print('*****❤❤❤❤❤*****❤❤❤❤❤*****❤❤❤❤❤*****❤❤❤❤❤******************************WELCOME IN YASH HOTEL***********************************❤❤❤❤❤*****❤❤❤❤❤*****❤❤❤❤❤*****❤❤❤❤❤*****')
        print('')
        print('                                                                       ✔ 1. Custmor Entry')
        print('                                                                       ✔ 2. Order your Food')
        print('                                                                       ✔ 3. Room_INFO')
        print('                                                                       ✔ 4. Booking Room')
        print('                                                                       ✔ 5. View Custmor_Old Record(By Adhar_Id)')
        print('                                                                       ✔ 6. View Custmor_Old Record (By Date)')
        print('                                                                       ✔ 7. Count Custmour Visiting Time')
        print('                                                                       ✔ 8. Update Custmour Record')
        print('                                                                       ✔ 9. Delete Custmour Record')
        print('                                                                       ✔ 0. Exit')
        print()
        print()
        print('$$$$$$$$$$$$$$$$$$$^^^^^^^^^^^^^^^^^$$$$$$$$$$$$$$$$$$^^^^^^^^^^^^^^^^^$$$$$$$$$$$$$$$$$$$^^^^^^^^^^^^^$$$$$$$$$$$$$$$$$$$^^^^^^^^^^^^^^$$$$$$$$$$$$$$$$$$$^^^^^^^^^^')
        try:
            ch=int(input('Enter your Choice='))
            if (ch==1):
                h1.C_Entry()
            elif (ch==2):
                h1.f_order()
            elif (ch==3):
                h1.Room_INFO()
            elif (ch==4):
                h1.B_Room()
            elif (ch==5):
                h1.O_record()
            elif( ch==6):
                h1.Date_record()
            elif(ch==7):
                h1.Count()
                
            elif(ch==8):
                h1.Update()
                
          
            elif (ch==9):
                h1.Delete()
            elif(ch==0):
                print()
                print()
               
                print('You Are Exited Now Successfully.') 
                print('Thank You....')
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')
                print()
                print()
                quit() 
            else:
                raise ValueError
            
        except ValueError:
            print('Your choice is invalid.Please try again....')
            h1.home()
       
       
       
 #Function No :2

    def C_Entry1(self):
        h1.getid()
        n=0
        x='select * from table1'
        self.cur.execute(x)
        result=self.cur.fetchall()
        for i in result:
            if(self.id1==i[1]):
                print()
                print('   *Name*                     *Id*                 *Ph.no*                 *Address*  ')
                print()
                print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t\t', i[3])
                n=n+1       
                break
                
        if(n>0):
            print()
            print('Record Is Already Present For Id',self.id1,'In database !!!')
            
        else:
         
            h1.getName()
    
            try:
                self.phno=input('Enter Your 10 Digit Mobile No=')
             
                if (len(self.phno)!=10):
                    raise ValueError
            except ValueError:
                h1.getmob()
    
            h1.getAddr() 
      
            print()
            print()
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
            print('Do You Want to Save This Custmor Record?')
            print('press 1 for YES')
            print('press 2 for NO')
            try:
                self.ch=int(input('Enter Your Choice='))
                if(self.ch==1):
                    h1.save1()
                    h1.save()
                elif (self.ch==2):
                    print('You Are Selected For NO')
                    h1.home()
                else:
                    raise ValueError
            except ValueError:
                h1.choice()
        h1.home()
    
    def getAddr(self):
            
            print('🚕🚕🚕🚕🚕🚕🚓🚓🚓🚓🚓🚓🚓🚓🚓🚕🚓🚓🚓🚓🚓🚓🚓🚓🚓🚕🚕🚕🚕🚕🚕🚕🚕🚕🚕🚕🚕🚕🚕  Districts  🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓🚓')
            print()
            print('                                                             Press   1 For Ahmednagar       Maharastra')
            print('                                                             Press   2 For Akola            Maharastra')
            print('                                                             Press   3 For Amravati         Maharastra')
            print('                                                             Press   4 For Aurangabad       Maharastra')
            print('                                                             Press   5 For Beed             Maharastra')
            print('                                                             Press   6 For Bhandara         Maharastra')
            print('                                                             Press   7 For Buldhana         Maharastra')
            print('                                                             Press   8 For Chandrapur       Maharastra')
            print('                                                             Press   9 For Dhule            Maharastra')
            print('                                                             Press  10 For Gadchiroli       Maharastra')
            print('                                                             Press  11 For Gondia           Maharastra')
            print('                                                             Press  12 For Hingoli          Maharastra')
        
            print('                                                             Press  13 For Jalgaon          Maharastra')
            print('                                                             Press  14 For Jalna            Maharastra')
            print('                                                             Press  15 For Kolhapur         Maharastra')
            print('                                                             Press  16 For Latur            Maharastra')
            print('                                                             Press  17 For Mumbai City      Maharastra')
            print('                                                             Press  18 For Mumbai Suburban  Maharastra')
            print('                                                             Press  19 For Nagpur           Maharastra')
            print('                                                             Press  20 For Nanded           Maharastra')
            print('                                                             Press  21 For Nandurbar        Maharastra')
            print('                                                             Press  22 For Nashik           Maharastra')
            print('                                                             Press  23 For Osmanabad        Maharastra')
            print('                                                             Press  24 For Palghar          Maharastra')
            print('                                                             Press  25 For Parbhani         Maharastra')
            print('                                                             Press  26 For Pune             Maharastra')
            print('                                                             Press  27 For Raigad           Maharastra')
            print('                                                             Press  28 For Ratnagiri        Maharastra')
            print('                                                             Press  29 For Sangli           Maharastra')
            print('                                                             Press  30 For Satara           Maharastra')
            print('                                                             Press  31 For Sindhudurg       Maharastra')
            print('                                                             Press  32 For Solapur          Maharastra')
            print('                                                             Press  33 For Thane            Maharastra')
            print('                                                             Press  34 For Wardha           Maharastra')
            print('                                                             Press  35 For Washim           Maharastra')
            print('                                                             Press  36 For Yavatmal         Maharastra')
            print('                                                             Press  37 For Other                 State')
            
            try:
                print()
                ch=int(input('Enter Your Valid Choice='))
                if ch==1:
                    self.addr='Ahmednagar       Maharastra'
                elif ch==2:
                    self.addr=' Akola            Maharastra'
                elif ch==3:
                    self.addr='Amravati         Maharastra'
                elif ch==4:
                    self.addr='Aurangabad       Maharastra'
                elif ch==5:
                    self.addr='Beed             Maharastra'
                elif ch==6:
                    self.addr='Bhandara         Maharastra'
                elif ch==7:
                    self.addr='Buldhana         Maharastra'
                elif ch==8:
                    self.addr='Chandrapur       Maharastra'
                elif ch==9:
                    self.addr='Dhule            Maharastra'
                elif ch==10:
                    self.addr='Gadchiroli       Maharastra'
                elif ch==11:
                    self.addr='Gondia           Maharastra'
                elif ch==12:
                    self.addr='Hingoli          Maharastra'
                elif ch==13:
                    self.addr='Jalgaon          Maharastra'
                elif ch==14:
                    self.addr='Jalna            Maharastra'
                elif ch==15:
                    self.addr='Kolhapur         Maharastra'
                elif ch==16:
                    self.addr='Latur            Maharastra'
                elif ch==17:
                    self.addr='Mumbai City      Maharastra'
                elif ch==18:
                    self.addr='Mumbai Suburban  Maharastra'
                elif ch==19:
                    self.addr='Nagpur           Maharastra'
                elif ch==20:
                    self.addr='Nanded           Maharastra'
                elif ch==21:
                    self.addr='Nandurbar        Maharastra'
                elif ch==22:
                    self.addr='Nashik           Maharastra'
                elif ch==23:
                    self.addr='Osmanabad        Maharastra'
                elif ch==24:
                    self.addr='Palghar          Maharastra'
                elif ch==25:
                    self.addr='Parbhani         Maharastra'
                elif ch==26:
                    self.addr='Pune             Maharastra'
                elif ch==27:
                    self.addr='Raigad           Maharastra'
                elif ch==28:
                    self.addr='Ratnagiri        Maharastra'
                elif ch==29:
                    self.addr='Sangli           Maharastra'
                elif ch==30:
                    self.addr='Satara           Maharastra'
                elif ch==31:
                    self.addr='Sindhudurg       Maharastra'
                elif ch==32:
                    self.addr='Solapur          Maharastra'
                elif ch==33:
                    self.addr='Thane            Maharastra'
                elif ch==34:
                    self.addr='Wardha           Maharastra'
                elif ch==35:
                    self.addr='Washim           Maharastra'
           
                elif ch==36:
                    self.addr='  Yavatmal         Maharastra'
                elif ch==37:
                    self.addr='  Other                 State'
                else:
                    raise ValueError
           
            except ValueError:
                print()
                print('Your Choice Is Invalid...Please Try Again.')
                h1.getAddr()
 
  
  
  # function No 3
    def getid(self):
        print()
        print('Please Enter Your Correct 12 Digit Aadhar Id')
        try:
            self.id1=input('Enter Your Aadhar Id=')
            
            try:
                if(len(self.id1)!=12):
                    raise TypeError
            except TypeError:
                h1.getid()
        except ValueError:
            h1.getid()
    
    
    def C_Entryz(self):
        print()
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Welcome For Custmor Entry!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print()
        h1.getName()
         
    
        try:
            self.phno=input('Enter Your 10 Digit Mobile No=')
             
            if (len(self.phno)!=10):
                raise ValueError
        except ValueError:
            h1.getmob()
    
        h1.getAddr()
      
        print()
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        print('Do You Want to Save This Custmor Record?')
        print('Only press 1 for Saving Record')
        #print('press 2 for NO')
        try:
            self.ch=int(input('Enter Your Choice='))
            if(self.ch==1):
                h1.save1()
                h1.save()
            
            else:
                raise ValueError
        except ValueError:
                h1.choice0()
        
    
    
    
 #function No 4
    def getmob(self):
        print('Please Enter Youe Correct 10 Digit mobile No=')
        
        self.phno=input('Enter Your Mobile No=')
        try:
            if (len(self.phno)!=10):
                raise ValueError
        except ValueError:
            h1.getmob()
           
    

    def choice0(self):
        print()
        print('Sorry.......')
        print('Your  Entered Choice is Invalid.')
        print('Please Enter Correct Choice')
        print()
        print('Do You Want to Save This Custmor Record in Database?')
        print('Compulsory press 1 for YES ')
        #print('Press 2 for NO')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        print()
        try:
            self.ch=int(input('Enter Your Choice='))
            if( self.ch==1):
                h1.save1()
                h1.save()
             
            else:
                raise ValueError
        except ValueError:
            h1.choice0()
           
           
   #function No 5
    def choice(self):
        print()
        print('Sorry.......')
        print('Your  Entered Choice is Invalid.')
        print('Please Enter Correct Choice')
        print()
        print('Do You Want to Save This Custmor Record in Database?')
        print('press 1 for YES')
        print('Press 2 for NO')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        print()
        try:
            self.ch=int(input('Enter Your Choice='))
            if( self.ch==1):
                h1.save1()
                h1.save()
            elif(self.ch==2):
                print('You Have Selected for NO')
                h1.home()
            else:
                raise ValueError
        except ValueError:
            h1.choice()
            
  #function No 6
    def save1(self):
        dict1={'Name':None,'id':None,'phno':None,'Address':None,'Date':None}
        dict1['id']=self.id1
        dict1['Name']=self.name
        dict1['phno']=self.phno
        dict1['Address']=self.addr
        dict1['Date']=self.z
        dict2=str(dict1)
        self.x=open('Abc.txt','a')
        if (self.x):
           
            self.x.write(dict2)
            
            self.x.write(',') 
        self.x.close()
        
    
    #function No 7
    def f_order1(self):
        print()
        input('You Are In Process, Press Any Key To Cont...')
        n=0
        x='select * from table1'
        self.cur.execute(x)
        result=self.cur.fetchall()
        for i in result:
            if(self.id1==i[1]):
                n=n+1       
                break
        if n>0:
            self.name=i[0]
            self.id1=i[1]
            self.phno=i[2]
            self.addr=i[3]
            
        
        else:
            h1.getid()
            h1.getmob()
            h1.getName()
            h1.getAddr()
       
            
        
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ') 
        print()
        print()
        print('***************************************************************************Hotel Menu Card****************************************************************************')
        print()
        print('                                                                             *BIRYANIS*')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        
        print('                                                    | Chicken Biryani                                               Rs 210 |')
        print('                                                    | Mutton Biryani                                                Rs 253 |' )
        print('                                                    | Chicken Family Pack                                           Rs 552 |')
        print('                                                    | Special Chicken Biryani                                       Rs 337 |')
        print('                                                    | Special Mutton Biryani                                        Rs 351 |')
        print('                                                    | Supreme Mutton Biryani                                        Rs 810 |')
        print('                                                    | Supreme Chicken Biryani                                       Rs 784 |')
        print('                                                    | Egg Biryani                                                   Rs 154 |')
        print('                                                    | Veg. Biryani                                                  Rs 154 |')
        print('                                                    | Veg. Family Pack                                              Rs 383 |')
        print('                                                    | Veg. Supreme Pack                                             Rs 574 |')
        print()
        print('                                                                              *STARTERS*')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('                                                    | Chilli Chicken                                                Rs 264 |')
        print('                                                    | Chicken 65                                                    Rs 264 |')
        print('                                                    | panner 65                                                     RS 196 |')
        print('                                                    | Veg. Manchurian                                               RS 189 |')
        print()
        print('                                                                               *KEBABS*')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print()
        print('                                                    | Chicken Tikka Kebab                                           Rs 243 | ')
        print('                                                    | Tandoori Chicken Half                                         Rs 243 |')
        print('                                                    | Tandoori Chicken Full                                         Rs 379 |')
        print('                                                    | Chicken Reshmi Kebab                                          Rs 243 |')
        print('                                                    | Chicken Garlic Kebab                                          Rs 243 |')
        print()
        print('                                                                               *CURRIES*')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print()
        print('                                                    | Butter Chicken Boneless                                       Rs 246 |')
        print('                                                    | Nizami Handi                                                  Rs 171 |')
        print()
        print('                                                                             *INDIAN BREADS*')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print()
        print('                                                    | Tandoori Roti                                                 Rs 40 |')
        print('                                                    | Rumali Roti                                                   RS 40 |')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print()
         
         
        
        self.food=input('Enter Your Food Item=')
        if (len(self.food)<=3):
            while(len(self.food)<=3):
                self.food=input('Enter Your Ordered Food Item=')
        self.get_Amnt()
        print()
        print('- - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - -')
        print()
        print('Do You Want to Save This Custmor Record in Your Database?')
        print('press 1 for YES')
        print('press 2 for NO')
        print()
        try:
            self.ch=int(input('Enter Your Choice='))
            if (self.ch==1):
                h1.save4()
                h1.save2()
                
            elif(self.ch==2):
                print('You Have Selected For NO Saving Data')
               
            else:
                raise ValueError
            
            
            
        except ValueError:
            h1.mychoice()
        h1.home()
    
    def get_Amnt(self):
        print()
        try:
        
            self.amnt=int(input('Please Enter Total Amount Of Custmor='))
        except ValueError:
            print('Sorry..')
            print('Please Enter Valid Amount')
            print()
            h1.get_Amnt()
        
    
    #function no 8
    def save2(self):
         
        
        self.dict1={'Name':None,'id':None,'phno':None,'Address':None,'F_item':None,'Pr':None,'Date':None}
        self.dict1['id']=self.id1
        self.dict1['Name']=self.name
        self.dict1['phno']=self.phno
        self.dict1['Address']=self.addr
        self.dict1['F_item']=self.food
        self.dict1['Pr']=self.amnt
        self.dict1['Date']=self.z
        self.x=open('Abc.txt','a')
       
        dict2=str(self.dict1)
        if self.x:
            
            self.x.write(dict2)

            self.x.write(',')             
        self.x.close()
         
         
        
        #function No 8
    def Room_INFO(self):
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print()
        print('                                            *STANDARD NON-AC1*')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - ')
        print('Room aminties include : 1 Double Bed,TV, Telephone')
        print('Double Door cupboard ,1 coffee table with 2 sofa ,Balcony')
        print('an attachment washroom with hot/cold water')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print()
        print('                                             *STANDARD NON-AC2*')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - ')
        print('Room aminties include : 1 Double Bed,TV, Telephone')
        print('Double Door cupboard ,1 coffee table with 2 sofa ,Balcony')
        print('an attachment washroom with hot/cold water+window/split AC')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        
        print('                                              *3-BED NON-AC*')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - ')
        print('Room aminties include : 1 Double Bed+ 1 single BED ,TV, Telephone')
        print('Triple Door cupboard ,1 coffee table with 2 sofa ,Balcony')
        print('an attachment washroom with hot/cold water')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        
        print('                                               *3-BED AC*')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - ')
        print('Room aminties include : 1 Double Bed+1 single BED TV, Telephone')
        print('Triple Door cupboard ,1 coffee table with 2 sofa ')
        print('1 side table ,Balcony with an accent table with 2 chair')
        print('an attachment washroom with hot/cold water')
        print()
        print('/ / / // / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  ')
        h1.home()
  

#function No 9
    def B_Room1(self):
        print()
        n=0
        x='select * from table1'
        self.cur.execute(x)
        result=self.cur.fetchall()
        for i in result:
            if(self.id1==i[1]):
                n=n+1       
                break
        if n>0:
            self.name=i[0]
            self.id1=i[1]
            self.phno=i[2]
            self.addr=i[3]
            
        
        else:
            h1.getid()
            h1.getmob()
            h1.getName()
            h1.getAddr()
        
        print()
        
       
        print('*******************************************************************************WELCOME********************************************************************************')
        
        print('You are in Proceed for Booking your Room...')
        print()
        input('Press Any Key To Cont..')
        print()       
        print('press 1 for STANDARD NON-AC1')
        print('press 2 for STANDARD NON-AC2')
        print('press 3 for 3-BED NON-AC')
        print('press 4 for 3-BED AC')
        print()
        try:
            self.Rch=int(input('Enter Your choice='))
            if (self.Rch==1):
                print('You have Selected for STANDARD NON-AC1')
                print('per Night = 4000/-')
                self.Rch1='STANDARD NON-AC1 Room'
            elif (self.Rch==2):
                print('You Have Selected for STANDARD NON-AC2')
                print('per Night = 4500/-')
                self.Rch1='STANDARD NON-AC2 Room'
            elif (self.Rch==3):
                print('You Have Selected for 3-BED NON-AC ')
                print('per Night = 5000/-')
                self.Rch1='3-BED NON-AC Room'
            elif (self.Rch==4):
                print('You Have Selected for  3-BED AC')
                print('per Night  = 5500/-')
                self.Rch1='3-BED AC Room'    
            else:
                raise ValueError
        except ValueError:
            print()
            print('Sorry..')
            print('Your Choice is Invalid.Please Try Again...')
            h1.B_Room1()
         
        h1.get_Amnt()
        print()
        print('Do You want to Save This Custmour Record?')
        print('press 1 for YES')
        print('press 2 for No')
        try:
            self.ch=int(input('Enter Your Choice='))
            if (self.ch==1):
                h1.save5()
                h1.save3()
                
            elif(self.ch==2):
                print('You Have Selected for NO')
                
               
            else:
                raise ValueError
        except ValueError:
            h1.Mychoice()
            
            
        h1.home()    
#function no 10
    def Mychoice(self):
        print()
        print('Sorry...')
        print('Your Choice is Invalid...')
        print('Please try again.')
        print()
        print('Do You Want To Save This C_Record?')
        print('press 1 for YES')
        print('press 2 for NO')
        try:
            self.ch=int(input('Enter Your Choice='))
            if(self.ch==1):
                h1.save3()
                h1.save5()
            elif(self.ch==2):
                print('You Have Selected for NO...')
                h1.home() 
            else:
                raise ValueError
        except ValueError:
            h1.Mychoice()
            
    #function No 11
    def mychoice(self):
        print()
        print('Sorry....')
        print('Invalid Choice....')
        print('Please try again.')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        print()
        print('Do You Want to Save This Custmor Record?')
        print('press 1 for YES')
        print('press 2 for NO')
        print()
        try:
            x=self.ch=int(input('Please Enter Your Choice='))
            if x==1:
                h1.save2()
                h1.save4()
            elif(x==2):
                print('You Have Selected for NO')
                h1.home()
            else:
                raise ValueError
        
        except ValueError:
            h1.mychoice()
            
    
    def save3(self):
# function no 12
        self.dict1={'Name':None,'id':None,'phno':None,'Address':None,'Room':None,'Pr':None,'Date':None}
        self.dict1['id']=self.id1
        self.dict1['Name']=self.name
        self.dict1['phno']=self.phno
        self.dict1['Address']=self.addr
        self.dict1['Room']=self.Rch1
        self.dict1['Pr']=self.amnt
        self.dict1['Date']=self.z
        self.x=open('Abc.txt','a')
        dict2=str(self.dict1)
        self.x.write(dict2)
       
        self.x.write(',') 
        
        self.x.close()
        
 
# function no 13
    def O_record(self):
        print()
        print('- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - --')
        print('Do You Want to see old Record of Custmor?')
        print('press 1 for YES')
        print('press 2 for NO')
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        try:
            self.ch =int(input('Enter Your Choice='))
            if (self.ch==1):
                h1.O_record1()
            elif(self.ch==2):
                print('You Have Selected for NO')
                h1.home()
            
            else:
                raise ValueError
        except ValueError:
            print('Sorry....')
            print('Your Choice is Invalid...')
            print('Try again Later.')
            h1.O_record()
       
    # function no 14            
    
    def O_record1(self):
        self.tot=0
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print()
        print('Please Do Select Valid Option..')
        print()
        print('press 1 for See All Custmor Record')
        print('press 2 for see Specific Custmor Record')
        print()
        self.l=0
        try:
            self.ch=int(input('Enter Your Choice='))
            
        except ValueError:
                print('Your Choice is Invalid.Please Try Again...')
                h1.O_record1()
    
        if((self.ch==1)or(self.ch==2)):
            pass
        else:
            print('Sorry...')
            print('Your Choice Is Invalid..Please Try Again Later.')
            h1.O_record1()
    
    
        if(self.ch==1):
            print()
           
           
            print('   *Name*                     *Id*          *Ph.no*                   *Address*              *B_Room Type*                  *O_Food*')
               
            print()
            
            x='select * from table5'
            try:
            
                self.cur.execute(x)
            except:
                pass
            
            try:
            
                result=self.cur.fetchall()
                self.l= self.l+self.cur.rowcount
                
            except:
                pass
                
             
            try:
            # print('   *Name*                     *Id*                 *Ph.no*                 *Address*                              *B_Room Type*                         *O_Food*')
                for i in result:
                    if(len(i[0])<=13 ):
                    
                    
                        print(i[0], '\t\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t\t\t\t',i[4],)
                        self.tot=self.tot+i[5]
                    
                     
                    
                    else:
                    
                    
                        print(i[0], '\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t\t\t\t',i[4],)
                        self.tot=self.tot+i[5]
                    
                    
                       
            except Exception:
                pass
            
            
            
            x='select * from table6'
            
            try:
            
                self.cur.execute(x)
            except:
                pass
            try:
            
                result=self.cur.fetchall()
                self.l= self.l+self.cur.rowcount
                
            except:
                pass
            try:
            
            #print('   *Name*                     *Id*                 *Ph.no*                 *Address*                              *B_Room Type*                         *O_Food*')
                for i in result:
                    if(len(i[0])<=13):
                    
                        print(i[0], '\t\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t',i[4])
                        self.tot=self.tot+i[5]
                        
                    else:
                        print(i[0], '\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t',i[4],)
                        self.tot=self.tot+i[5]
                  
                        
            except Exception:
                pass
              
            if(self.l>0):
                pass
            
            else:
                print()
                print()
                print('If Nothing Shows Any Record...Then There Is No Record Available In Database')
                print()
            print()
            print(self.l,'rows are affected')
            print('Total Amount Of All Custmor=',self.tot)
            
        else:
   
                    
                self.id2=input('Please Enter Correct 12 Digit Adhar Id to see Record Itself=')
                if(len(self.id2)!=12):
                    h1.Id()
                else:
                    
                    pass
                print()
                print('   *Name*                     *Id*          *Ph.no*               *Address*                 *B_Room Type*            *O_Food*')
                print()
                 
                try:
                
                    x='select * from table5'
                    self.cur.execute(x)
                    result=self.cur.fetchall()
                     
                    for i in result:
                         
                        
                
                        if(i[1]==self.id2):
                            
                            if(len(i[0])<=13):
                    
                                print(i[0], '\t\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t\t\t\t',i[4])
                                self.tot=self.tot+i[5]
                                self.l= self.l+  1
                            else:
                                print(i[0], '\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t\t\t\t',i[4],)
                                self.tot=self.tot+i[5]
                                self.l= self.l+  1
                            
                   
                        else:
                            pass         
                except Exception:
                    pass
                    
                try:
                
                    x='select * from table6'
                    self.cur.execute(x)
                    result=self.cur.fetchall()
                    
                    for i in result:
                
                        if(i[1]==self.id2):
                            if(len(i[0])<=13):
                    
                                print(i[0], '\t\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t',i[4])
                                self.tot=self.tot+i[5]
                                self.l= self.l+  1
                            else:
                                print(i[0], '\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t',i[4],)
                                self.tot=self.tot+i[5]
                                self.l= self.l+  1
                            
                   
                        else:
                            pass
                            
                except Exception:
                    pass
                
                if(self.l>0):
                    print()    
                    print(self.l,'rows are affected')
                    print('Total Amount Of',self.id2,'=',self.tot) 
                    
                else:
                    print()        
                    print('Nothing have Any Record For',self.id2,'...So There Is No Record Available In Database')
                    print()
        h1.home()         
    # function No 15
     

    def O_record2(self):
        try:
            self.x=open('Abc.txt','r')
            if (self.x):
                self.data=self.x.read()
                print(self.data)
                self.x.close()
                 
        except:
            print('File Does Not Contain Data.It Is Empty......')
             
            
    # Function No 16
    def O_record3(self):
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        h1.getid()
        
        try:
            self.x=open('Abc.txt','r')
            if self.x:
                a=self.data=self.x.read()
                print(a[0])
                for i in a[0]:
                    if(self.id1==i['id']):
                        print(i)
        except:
            print()
            print('The Record Is Not Present in File Of Your Adhar Id')
            
    
    def C_Entry(self):
        try:
            a= "create table table1(Name varchar(30),Id varchar(20),Phno varchar(25),Address varchar(100),Date varchar(20))"
            self.cur.execute(a)
            h1.C_Entry1()
        except Exception:
        
            h1.C_Entry1()
            
    def save(self):
        a="insert into table1 values(%s,%s,%s,%s,%s)"
        b=(self.name,self.id1,self.phno,self.addr,self.z)
        self.cur.execute(a,b)
        self.ad.commit() 
       
        print('Your Data is Saved Successfully...')
       
         
    
    def f_order(self):
        
       
        
        
        print()
        h1.getid()
        print('Is This Custmor Of Id ',self.id1,'Was Visit TO Your Hotel before This?')
        print('Press 1 If YES') 
        print('Press 2 If NO')
        print()
        try:
        
            ch=int(input('Enter Your Choice='))
        except ValueError:
            print()
            print('Sorry...')
            print('Your choice Is Invalid..Please Try Again.')
            h1.f_order()
        if(ch==1):
            n=0
            x='select * from table1'
            self.cur.execute(x)
            result=self.cur.fetchall()
            for i in result:
                if(self.id1==i[1]):
                    print()
                    print('   *Name*                     *Id*                 *Ph.no*                 *Address*  ')
                    print()
                    print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t', i[3])
                    n=n+1       
                    break
                
            if(n>0):
                pass
            else:
                print()
                print('Sorry...')
                print('Details Is Not Present For',self.id1,'In Database')
                print('Do Custmor_Entry Now.')
                h1.C_Entryz()
                x='select * from table1'
                self.cur.execute(x)
                result=self.cur.fetchall()
                for i in result:
                    if(self.id1==i[1]):
                        print()
                        print('   *Name*                     *Id*                 *Ph.no*                 *Address*  ')
                        print()
                        print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t\t', i[3])
                                
                        break
                
                
            
        
        elif(ch==2):
            n=0
            x='select * from table1'
            self.cur.execute(x)
            result=self.cur.fetchall()
            for i in result:
                if(self.id1==i[1]):
                    print()
                    print('Details For ',self.id1,' Are Available In Database')
                    print()
                    print('   *Name*                     *Id*                 *Ph.no*                 *Address*  ')
                    print()
                    print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t', i[3])
                    n=n+1       
                    break
                
            if(n>0):
                pass
            else:
        
        
        
        
        
                print()
                print('Details For ',self.id1,'Is Not present In Database.Do Custmor_Entry Now.')
                print('And After That Order Food For ',self.id1 )
                h1.C_Entryz()
                x='select * from table1'
                self.cur.execute(x)
                result=self.cur.fetchall()
                for i in result:
                    if(self.id1==i[1]):
                        print()
                        print('   *Name*                     *Id*                 *Ph.no*                 *Address*  ')
                        print()
                        print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t\t', i[3])
                            
                        break
             
        else:
            print()
            print('Sorry...')
            print('Your choice Is Invalid..Please Try Again.')
            h1.f_order()
        
        try:
            a= "create table table5(Name varchar(50),Id varchar(20),Phno varchar(25),Address varchar(50),O_Food varchar (100),Pr int(100),Date varchar(20))"
            self.cur.execute(a)
            h1.f_order1()
        except Exception:
            h1.f_order1()
            
            
            
        
        
    def save4(self):
        a="insert into table5 values(%s,%s,%s,%s,%s,%s,%s)"
        b=(self.name,self.id1,self.phno,self.addr,self.food,self.amnt,self.z)
        self.cur.execute(a,b)
        self.ad.commit() 
        print('Your Data Is Saved Successfully..')
        
        
    def  B_Room(self):
        print()
        h1.getid()
        print('Is This Custmor Of Id',self.id1,' Was Visit Your Hotel Before This?')
        print('Press 1 If YES')
        print('Press 2 If NO')
        print()
        
        try:
            ch=int(input('Enter Your Choice='))
        except ValueError:
            print()
            print('Sorry...')
            print('Your Choice Is Invalid..Please Try Again Later.')
            h1.B_Room()
        if(ch==1):
            n=0
            x='select * from table1'
            self.cur.execute(x)
            result=self.cur.fetchall()
            for i in result:
                if(self.id1==i[1]):
                    print()
                    print('   *Name*                     *Id*                 *Ph.no*                 *Address*  ')
                    print()
                    print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t\t', i[3])
                    n=n+1       
                    break
                
            if(n>0):
                pass
            else:
                print()
                print('Sorry...')
                print('Details Is Not Present For',self.id1,'In Database')
                print('Please Do Custmor_Entry For ',self.id1,' Now.')
                h1.C_Entryz()
                x='select * from table1'
                self.cur.execute(x)
                result=self.cur.fetchall()
                for i in result:
                    if(self.id1==i[1]):
                        print()
                        print('   *Name*                     *Id*                 *Ph.no*                 *Address*  ')
                        print()
                        print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t\t', i[3])
                                
                        break
                
         
        

        
        elif(ch==2):
            n=0
            x='select * from table1'
            self.cur.execute(x)
            result=self.cur.fetchall()
            for i in result:
                if(self.id1==i[1]):
                    print()
                    print('Details For',self.id1,'Is Present In Database')
                    print()
                    print('   *Name*                     *Id*                 *Ph.no*                 *Address*  ')
                    print()
                    print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t\t', i[3])
                    n=n+1       
                    break
                
            if(n>0):
                pass
            else:
                print('Details For Id',self.id1,'Is Not Present In Database')
         
                print()
                print('Do Custmor_Entry For Id',self.id1,' Now.')
                print('And After That Book Room For This Custmor.')
                h1.C_Entryz()
                x='select * from table1'
                self.cur.execute(x)
                result=self.cur.fetchall()
                for i in result:
                    if(self.id1==i[1]):
                        print()
                        print('   *Name*                     *Id*                 *Ph.no*                 *Address*  ')
                        print()
                        print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t\t', i[3])
                            
                        break
                 
        
        else:
            print()
            print('Sorry...')
            print('Your Choice Is Invalid..Please Try Again Later.')
            h1.B_Room()
        
        try:
            a= "create table table6(Name varchar(50),Id varchar(20),Phno varchar(25),Address varchar(50),B_Room_Type varchar (100),Pr int(100),Date varchar(20))"
            self.cur.execute(a)
            h1.B_Room1()
        except Exception:
            h1.B_Room1()
            
            
    def save5(self):
        a="insert into table6 values(%s,%s,%s,%s,%s,%s,%s)"
        b=(self.name,self.id1,self.phno,self.addr,self.Rch1,self.amnt,self.z)
        self.cur.execute(a,b)
        self.ad.commit() 
        print('Your Data Is Saved Successfully..')
                
    def Id(self):
        try:
            print('Sorry...')
            print('Your Adhar Id Is Not Valid ...Please Try Again Later.')
            self.id2=input('Enter Your Adhar Id to See Record Itself=')
            while(len(self.id2)!=12):
                h1.Id()
        except ValueError:
            h1.Id()
    
    def Count(self):
        print()
        print('Please Enter 12 Digit Adhar Id, You Want to See Record Itself')
        print()
        try:
        
            self.id3=input('Enter Adhar Id=')
        except:
            print()
            print('Sorry...')
            print('Your Entered Adhar Id Is Wrong..Please Renter Adhar Id')
            print()
            h1.Count()
        A=0
         
        try:
                
            x='select * from table5'
            self.cur.execute(x)
            result=self.cur.fetchall()
            for i in result:
                
                if(i[1]==self.id3):
                    #print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t\t', i[3],'\t\t\t\t',i[4])
                    A+=1
                else:
                    pass
        except Exception:
            pass
       
        try:
                
            x='select * from table6'
            self.cur.execute(x)
            result=self.cur.fetchall()
            for i in result:
                
                if(i[1]==self.id3):
                    #print(i[0], '\t\t'              ,      i[1] , '\t\t'     ,             i[2],'\t\t', i[3],'\t\t\t\t',i[4])
                    A+=1
                else:
                    pass
        except Exception:
            pass
        print('Total No. of ',self.id3,'Is =',A,'In Database')
        h1.home()
    def getName(self):
        print()
        n=0
        m=0
        x=self.name=input('Enter Your Name=')
        for i in x:
            if (i==" "):
        
                n=n+1
        
        if(n!=1):
        
        
            print('Enter Your Surname First(Use only 1 Space)...')
            m=m+1
        else:
            pass
        
        p=0
        
        if(len(x)>20):
            print('Name Should be in 20 Charactors Only..')
            
            m=m+1
        else:
            pass
        
        p=0
        if (m!=0):
            h1.getName()
        else:
            pass
    def Update(self):
        self.l=0
        print()
        h1.getid()
        h1.Update_choice()
            
        if (self.ch==1):
            try:
                h1.getName()
                x='update table1 set Name=%s where Id=%s'
                y=(self.name,self.id1)
                self.cur.execute(x,y)
                self.l=self.l+self.cur.rowcount
                self.ad.commit()
                 
            except Exception:
                pass
            
            try:
                
               
                x='update table5 set Name=%s where Id=%s'
                y=(self.name,self.id1)
                self.cur.execute(x,y)
                self.l=self.l+self.cur.rowcount
                
                self.ad.commit()
                 
            except Exception:
                pass
            
            try:
                x='update table6 set Name=%s where Id=%s'
                y=(self.name,self.id1)
                self.cur.execute(x,y)
                self.l=self.l+self.cur.rowcount
                
                self.ad.commit()
                 
            except Exception:
                pass
            
        elif(self.ch==2):
            
            h1.getmob()
            try:
                
                x='update table1 set Phno=%s where Id=%s'
                y=(self.phno,self.id1)
                self.cur.execute(x,y)
                self.l=self.l+self.cur.rowcount
                
                self.ad.commit()
                
            except Exception:
                pass
            
            try: 
                x='update table5 set Phno=%s where Id=%s'
                y=(self.phno,self.id1)
                self.cur.execute(x,y)
                self.l=self.l+self.cur.rowcount
                
                self.ad.commit()
                
            except Exception:
                pass
            
            try: 
                x='update table6 set Phno=%s where Id=%s'
                y=(self.phno,self.id1)
                self.cur.execute(x,y)
                self.l=self.l+self.cur.rowcount
                
                self.ad.commit()
                
            except Exception:
                pass
        
        elif(self.ch==3):
                print()
                print('Enter Address You Want To Set To ',self.id1)
                print()
                h1.getAddr()
                
                
                try:
                    x='update table1 set Address=%s where Id=%s'
                    y=(self.addr,self.id1)                 
                    self.cur.execute(x,y)
                    self.l=self.l+self.cur.rowcount
                
                    self.ad.commit()
                     
                except Exception:
                    pass
                
                try:
                    x='update table5 set Address=%s where Id=%s'
                    y=(self.addr,self.id1)                 
                    self.cur.execute(x,y)
                    self.l=self.l+self.cur.rowcount
                
                    self.ad.commit()
                     
                except Exception:
                    pass
                
                try:
                    x='update table6 set Address=%s where Id=%s'
                    y=(self.addr,self.id1)                 
                    self.cur.execute(x,y)
                    self.l=self.l+self.cur.rowcount
                
                    self.ad.commit()
                     
                except Exception:
                    pass
        if(self.l>0):
        
            print('Database Is Updated Successfully...')
            print()
            print(self.l,'rows are affected')
            print()
        else:
            print()
            print(self.l,'rows are affected')
            print()
        h1.home()
    
    def Update_choice(self):
        print()
        print('Press 1 for Update Name of',self.id1)
        print('Press 2 for Update Phno of',self.id1)
        print('Press 3 for Update Address of',self.id1)
        print()
        
        
        try:
        
            self.ch=int(input('Enter Valid Choice='))
            if (self.ch==1):
                pass
            elif(self.ch==2):
                pass
            elif(self.ch==3):
                pass
            else:
                raise ValueError
        except ValueError:
            print('Sorry...')
            print('Your Choice Is Invalid...Please Try Again.')
            print()
            h1.Update_choice()
    
    def Delete(self):
        
        h1.Delete_choice()
            
        if(self.ch==1):
            self.affr=0
            print()
            h1.getid()
            
            try:
            
                x="delete from table1 where Id =%s"
                y=(self.id1,)
                self.cur.execute(x,y)
                  
                self.ad.commit()
            except:
                pass
                
            try:
            
                x="delete from table5 where Id =%s"
                y=(self.id1,)
                self.cur.execute(x,y)
                self.affr=self.affr+self.cur.rowcount
                
                self.ad.commit()
            except:
                pass
    
            try:
            
                x='delete from table6 where Id =%s'
                y=(self.id1,)
                self.cur.execute(x,y)
                self.affr=self.affr+self.cur.rowcount
                self.ad.commit()
            except:
                pass
            if(self.affr>0):
            
                print('Data Is Successfully Deleted From Your Database  For ',self.id1)
                print()
                print(self.affr,'rows are affected')    
                print()
            else:
            
                print(self.affr,'rows are affected')    
        
        else:
            print()
            print('You Have Selected NO For <<  Deleting  >> Data')
            print()
        h1.home()
    
    def  Delete_choice(self):
        print()
        print('Do You Want To Delete The Custmour Record?')
        print('Press 1 For YES')
        print('Press 2 For NO')
        print()
        
        try:
            self.ch=int(input('Enter Valid Choice='))
        
    
            if (self.ch==1):
                pass
            elif(self.ch==2):
                pass
                
                 
            else:
                raise ValueError
                
        except  ValueError:
            print()
            print('Sorry...')
            print('Your Choice Is Invalid..Please Try Again Later.')
            h1.Delete_choice()      
        
    def Date_record(self):
        self.l=0
        self.tot=0
        print()
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('Please Enter Valid Date, You Want To Show Record Of Itself')
        print('Please Enter Date in Format of(MM/DD/YY) Like: 05/05/21')
        print()
        
        self.Date=input('Enter Date=')
        print()
        
        a=len(str(self.Date)) 
         
        if(a!=8):
        
            print()
            print('Sorry...')
            print('Your Date Is Invalid..Please Try Again Later.')
            h1.Date_record()
            
        else:
                
                print('This Following Is All Custmor Record Of Date=',self.Date)
                print()
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                
                print('   *Name*                     *Id*        *Ph.no*                *Address*                *B_Room Type*                   *O_Food*')
                print()
                 
                try:
                
                    x='select * from table5'
                    self.cur.execute(x)
                    result=self.cur.fetchall()
                     
                    for i in result:
                
                        if(i[6]==self.Date):
                            if(len(i[0])<=13):
                    
                                print(i[0], '\t\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t\t\t\t',i[4])
                                self.tot=self.tot+i[5]
                                self.l= self.l+  1
                            else:
                                print(i[0], '\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t\t\t\t',i[4],)
                                self.tot=self.tot+i[5]
                                self.l= self.l+  1
                            
                            
                            
                        else:
                            pass         
                except Exception:
                    pass
                    
                try:
                
                    x='select * from table6'
                    self.cur.execute(x)
                    result=self.cur.fetchall()
                    
                    for i in result:
                
                        if(i[6]==self.Date):
                            if(len(i[0])<=13):
                    
                                print(i[0], '\t\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t',i[4])
                                self.tot=self.tot+i[5]
                                self.l= self.l+  1
                            else:
                                print(i[0], '\t'              ,      i[1] , '\t'     ,             i[2],'\t', i[3],'\t',i[4],)
                                self.tot=self.tot+i[5]
                                self.l= self.l+  1
                        
                            
                        else:
                            pass
                except Exception:
                    pass
                
                print()
                print()
                print(self.l,'rows are affected')
                print('Tatal Amount Of Date ',self.Date,'=',self.tot)
                    
                
        h1.home()   

    
        
h1=hotel()
h1.home1()           

