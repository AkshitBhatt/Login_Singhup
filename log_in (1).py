# def sin_in():
#     print('Welcome! to Sin_in_page....')
#     import json
#     data_file={}
#     name=str(input('enter your name '))
#     last_name=str(input('enter your Last_name '))
#     mail=str(input('enter your Mail '))
#     passrd=str(input('enter your Password '))
#     dict={}
#     list=[]
#     dict["Name"]=name
#     dict["Last_name"]=last_name
#     dict["Mail"]=mail
#     dict["Password"]=passrd
#     data_file[name]=dict
#     list.append(data_file)
#     a=open("sinin_data.json","a")
#     b=json.dump(list,a,indent=2)
#     print('Thank!,for sin_in....., your data saved successfully.')
#     a.close()
# sin_in()

def log_in():
    print('Welcome! to Sinin_page....')
    import json
    usern=str(input('enter your user name '))
    passw=str(input('enter your password '))
    a=open("sinin_data.json","r")
    b=a.read()
    j=json.loads(b)
    for i in j:
        for k,v in i.items():
            for k in v:
                print(k['Name'])
log_in()
        # print(j[i]['Password'])
#         if usern==j[i]['Name']:
#             if passw==j[i]['Password']:
#                 print('login_succesful')
#             else:
#                 print("Invalid password....\n Plz write valid password")
#         else:
#             print('Invalid user_name....\n Plz write Valid user name')
#     a.close()
# log_in()

# def forgetp():
#     import json
#     userid=str(input('enter your user Id '))
#     passw=str(input('enter your new password '))
#     a=open("sinin_data.json","r")
#     b=a.read()
#     j=json.loads(b)
#     data_file={}
#     dict={}

#     dict["Password"]=passw
#     a.close()

# a=int(input('enter what do you want\n *if you wants to sin_in pres(1)\n *or presh (2)'))
# if a==1:
#     sin_in()
# elif a==2:
#     log_in()
# else:
#     forgetp()


