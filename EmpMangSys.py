from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import tkinter as tk



# Creating Class
class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')

       

        # VARIABLES
        self.var_dep = StringVar()
        self.var_designation = StringVar()
        self.var_address = StringVar()
        self.var_dob = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_married = StringVar()
        self.var_doj = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()
        self.var_age = StringVar()
        self.var_empid = StringVar()
        self.var_status = StringVar()
        
        
        
        
        
        
        
        

        
         # TITLE 
        lb1_title = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 37, 'bold'),
                          fg='darkblue', bg='white')
        lb1_title.place(x=0, y=0, width=1530, height=50)

        # LOGO IMAGE
        img_logo = Image.open('images/emplogo.png')
        img_logo = img_logo.resize((50, 50), Image.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=270, y=0, width=50, height=50)

        # FRAME
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=1, y=50, width=1360, height=140)

        # FIRST IMAGE
        img1 = Image.open('images/Image1.png')
        img1 = img1.resize((453, 140), Image.LANCZOS)
        self.photo_frame1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo_frame1)
        self.img_1.place(x=1, y=0, width=453, height=140)

        # SECOND IMAGE
        img2 = Image.open('images/image2.png')
        img2 = img2.resize((453, 140), Image.LANCZOS)
        self.photo_frame2 = ImageTk.PhotoImage(img2)

        self.img2 = Label(img_frame, image=self.photo_frame2)
        self.img2.place(x=450, y=0, width=453, height=140)

        # THIRD IMAGE
        img3 = Image.open('images/image3.jpg')
        img3 = img3.resize((455, 140), Image.LANCZOS)
        self.photo_frame3 = ImageTk.PhotoImage(img3)

        self.img3 = Label(img_frame, image=self.photo_frame3)
        self.img3.place(x=900, y=0, width=455, height=140)

        # Main frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=1, y=190, width=1360, height=510)
         # Set the background image for the Main_frame
        bg_image1 = Image.open('images/background4.jpg')
        bg_image1 = bg_image1.resize((1360, 510), Image.LANCZOS)
        self.photo_bg1 = ImageTk.PhotoImage(bg_image1)

        bg_label1 = Label(Main_frame, image=self.photo_bg1)
        bg_label1.place(x=0, y=0, relwidth=1, relheight=1)

        
    

        # upper frame
        self.upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information',
                                      font=('Bahnschrift', 11, 'bold'), fg='navy')
        self.upper_frame.place(x=6, y=2, width=1340, height=255)
        
        # Set the background image for the upper_frame
        bg_image = Image.open('images/background4.jpg')
        bg_image = bg_image.resize((1340, 260), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(bg_image)

        bg_label = Label(self.upper_frame, image=self.photo_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # =============================Labels and Entry fields==================================================
        
        # Department
        lbl_dep = Label(self.upper_frame, text='Department', font=('Rockwell', 11, 'bold'), bg='white')
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(self.upper_frame,textvariable=self.var_dep, font=('Rockwell', 12, 'bold'), width=17, state='readonly')
        combo_dep['value'] = ('Select Department', 'HR', 'Software Engineer', 'Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        # Designation
        lbl_Designation = Label(self.upper_frame, font=('Rockwell', 11, 'bold'), text='Designation:', bg='white')
        lbl_Designation.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        self.txt_Designation = ttk.Entry(self.upper_frame,textvariable=self.var_designation, width=22, font=("Rockwell", 11, "bold"))
        def valid_designation(value):
            # Allow alphabetical characters and spaces
            return all(c.isalpha() or c.isspace() for c in value)

        # Set the validation criteria for the entry field Designation.
        validation = self.upper_frame.register(valid_designation)
        self.txt_Designation.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_Designation.grid(row=1, column=1, sticky=W, padx=2, pady=7)
        
        # Address
        lbl_address = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="Address:", bg='white')
        lbl_address.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        self.txt_address = ttk.Entry(self.upper_frame,textvariable=self.var_address, width=22, font=("Rockwell", 11, "bold"))
        def valid_Address(value):
            # Allow alphabets ,numbers,special charc  and spaces
            return all(char.isalnum() or char.isspace() or char in {',','@','_','-','.'} for char in value)

        # Set the validation criteria for the entry field Email.
        validation = self.upper_frame.register(valid_Address)
        self.txt_address.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_address.grid(row=2, column=1, padx=2, pady=7)
        
        # DOB
        lbl_dob = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="DOB:", bg='white')
        lbl_dob.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        self.txt_dob = ttk.Entry(self.upper_frame,textvariable=self.var_dob, width=22, font=("Rockwell", 11, "bold"))
        def valid_dob(value):
            return all(char.isdigit() or char in {'/', '-'} for char in value)

        # Set the validation criteria for the entry field DOB.
        validation = self.upper_frame.register(valid_dob)
        self.txt_dob.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_dob.grid(row=3, column=1, padx=2, pady=7)
        
        # Id Proof
        com_txt_proof = ttk.Combobox(self.upper_frame, textvariable=self.var_idproofcomb, state="readonly",
                             font=("Rockwell", 12, "bold"), width=18)
        com_txt_proof['value'] = ("Select ID Proof", "PAN CARD", "ADHAR CARD")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4, column=0, sticky=W, padx=2, pady=7)


        self.txt_proof = ttk.Entry(self.upper_frame, textvariable=self.var_idproof, width=22, font=("Rockwell", 11, "bold"))
        

        def validate_ID(value, Select):
         if Select.get() == "PAN CARD":
             if value.isalnum() and len(value) <= 10 or value == "":
                 return True
             else:
                  return False
             
                 
         elif Select.get() == "ADHAR CARD":
             if value.isdigit() and len(value) <= 12 or value == "":
                   return True
             else:
                 return False
             
         else:
             return True
         
           
         
        # Set the validation criteria for the entry field based on the selected ID Proof
        validation = self.upper_frame.register(lambda P, Select=com_txt_proof: validate_ID(P, Select))
        self.txt_proof.config(validate="key", validatecommand=(validation, "%P"))
        self.txt_proof.grid(row=4, column=1, padx=2, pady=7)
         # Message Entry Field
        self.message_entry = ttk.Entry(self.upper_frame, textvariable=tk.StringVar(), state="readonly", width=50,
                                       font=("Rockwell", 10, "bold"))
        self.message_entry.grid(row=5, column=0,columnspan=2 ,padx=2, pady=7,sticky=tk.W)

        # Function to update the message entry field based on the selected ID Proof
        def update_message(*args):
            selected_id_proof = com_txt_proof.get()
            if selected_id_proof == "PAN CARD":
                self.message_entry.config(state="normal")
                self.message_entry.delete(0, tk.END)
                self.message_entry.insert(0, "Enter 10 digit PAN CARD number eg:ABCTY1234D")
                self.message_entry.config(state="readonly")
            elif selected_id_proof == "ADHAR CARD":
                self.message_entry.config(state="normal")
                self.message_entry.delete(0, tk.END)
                self.message_entry.insert(0, "Enter 12 digit ADHAR CARD number")
                self.message_entry.config(state="readonly")
            else:
                self.message_entry.config(state="normal")
                self.message_entry.delete(0, tk.END)
                self.message_entry.config(state="readonly")

        com_txt_proof.bind("<<ComboboxSelected>>", update_message)
        
    


        # Name
        lbl_Name = Label(self.upper_frame, font=('Rockwell', 12, 'bold'), text='Name:', bg='white')
        lbl_Name.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        self.txt_name = ttk.Entry(self.upper_frame,textvariable=self.var_name, width=22, font=('Rockwell', 11, 'bold'))
        def valid_nam(value):
            # Allow alphabetical characters and spaces
            return all(c.isalpha() or c.isspace() for c in value)

        # Set the validation criteria for the entry field Name.
        validation = self.upper_frame.register(valid_nam)
        self.txt_name.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_name.grid(row=0, column=3, sticky=W, padx=2, pady=7)

        
        # Email
        lbl_email = Label(self.upper_frame, font=('Rockwell', 12, 'bold'), text='Email:', bg='white')
        lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        self.txt_email = ttk.Entry(self.upper_frame,textvariable=self.var_email, width=22, font=("Rockwell", 11, "bold"))
        def valid_email_ad(value):
            return all(char.isalnum() or char in {'@','_','-','.'} for char in value)

        # Set the validation criteria for the entry field Email.
        validation = self.upper_frame.register(valid_email_ad)
        self.txt_email.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_email.grid(row=1, column=3, padx=2, pady=7)

        

        # Married
        lbl_married_status = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="Married_status:",
                                   bg='white')
        lbl_married_status.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        com_txt_married = ttk.Combobox(self.upper_frame,textvariable=self.var_married, state="readonly", font=("Rockwell", 12, "bold"), width=18)
        com_txt_married['value'] = ("", "Married", "Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        

        
        # DOJ
        lbl_Doj = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="DOJ:", bg='white')
        lbl_Doj.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        self.txt_Doj = ttk.Entry(self.upper_frame,textvariable=self.var_doj, width=22, font=("Rockwell", 11, "bold"))
        def valid_doj(value):
            return all(char.isdigit() or char in {'/', '-'} for char in value)

        # Set the validation criteria for the entry field DOJ.
        validation = self.upper_frame.register(valid_doj)
        self.txt_Doj.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_Doj.grid(row=3, column=3, padx=2, pady=7)
       


        # Gender
        lbl_gender = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="Gender:", bg='white')
        lbl_gender.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        com_txt_gender = ttk.Combobox(self.upper_frame,textvariable=self.var_gender, state="readonly", font=("Rockwell", 12, "bold"), width=18)
        com_txt_gender['value'] = ("Male", "Female", "Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4, column=3, sticky=W, padx=2, pady=7)
        
       

        # Phone
        lbl_phone = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="Phone No:", bg='white')
        lbl_phone.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        self.txt_phone = ttk.Entry(self.upper_frame,textvariable=self.var_phone, width=22, font=("Rockwell", 11, "bold"))
        def valid_in(value):
            return value.isdigit() and len(value) <= 10 or value == ""

        # Set the validation criteria for the entry field phone.
        validation = self.upper_frame.register(valid_in)
        self.txt_phone.config(validate="key",validatecommand = (validation,"%P"))
        
        self.txt_phone.grid(row=0, column=5, padx=2, pady=7)

        # Country
        lbl_country = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="Country:", bg='white')
        lbl_country.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        self.txt_country = ttk.Entry(self.upper_frame,textvariable=self.var_country, width=22, font=("Rockwell", 11, "bold"))
        def valid_con(value):
            # Allow alphabetical characters and spaces
            return all(c.isalpha() or c.isspace() for c in value)

        # Set the validation criteria for the entry field Country.
        validation = self.upper_frame.register(valid_con)
        self.txt_country.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_country.grid(row=1, column=5, padx=2, pady=7)

        # CTC
        lbl_ctc = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="Salary(CTC):", bg='white')
        lbl_ctc.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        self.txt_ctc = ttk.Entry(self.upper_frame, textvariable=self.var_salary, width=22, font=("Rockwell", 11, "bold"))
        def valid_sal(value):
            return value.isdigit() or value == ""

        # Set the validation criteria for the entry field CTC.
        validation = self.upper_frame.register(valid_sal)
        self.txt_ctc.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_ctc.grid(row=2, column=5, padx=2, pady=7)
        
        # AGE
        lbl_age = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="Age:", bg='white')
        lbl_age.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        self.txt_age = ttk.Entry(self.upper_frame, textvariable=self.var_age, width=22, font=("Rockwell", 11, "bold"))
        def valid_age(value):
            return value.isdigit() and len(value) <= 2 or value ==""

        # Set the validation criteria for the entry field Age.
        validation = self.upper_frame.register(valid_age)
        self.txt_age.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_age.grid(row=3, column=5, sticky=W, padx=2, pady=7)
        
       # Employee_Id
        lbl_empid = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="Employee Id:", bg='white')
        lbl_empid.grid(row=4, column=4, sticky=W, padx=2, pady=1)

        self.txt_empid = ttk.Entry(self.upper_frame,textvariable=self.var_empid, width=22, font=("Rockwell", 11, "bold"))
        def valid_id(value):
            return value.isdigit() and len(value) <= 5 or value == ""
        validation = self.upper_frame.register(valid_id)
        self.txt_empid.config(validate="key", validatecommand=(validation, "%P"))
        self.txt_empid.grid(row=4, column=5, padx=2, pady=6)
        
        # work_STATUS
        lbl_work_status = Label(self.upper_frame, font=("Rockwell", 12, "bold"), text="Status:", bg='white')
        lbl_work_status.grid(row=5, column=2, sticky=W, padx=2, pady=7)

        com_txt_work = ttk.Combobox(self.upper_frame,textvariable=self.var_status, state="readonly", font=("Rockwell", 12, "bold"), width=18)
        com_txt_work['value'] = ("Select Status", "Regular", "Suspended")
        com_txt_work.current(0)
        com_txt_work.grid(row=5, column=3, sticky=W, padx=2, pady=7)

        

        # Button Frame
        button_frame = Frame(self.upper_frame, bd=2, relief=RIDGE)
        button_frame.place(x=1100, y=10, width=170, height=210)
        # Set the background image for the Button_frame
        bg_image4 = Image.open('images/background4.jpg')
        bg_image4 = bg_image4.resize((170, 210), Image.LANCZOS)
        self.photo_bg4 = ImageTk.PhotoImage(bg_image4)
        
        bg_label4 = Label(button_frame, image=self.photo_bg4)
        bg_label4.place(x=0, y=0, relwidth=1, relheight=1)

        btn_add = Button(button_frame, text="Save",command=self.add_data, font=("Forte", 15, "bold"), width=13, bg="peachpuff", fg="black")
        btn_add.grid(row=0, column=0, padx=1, pady=5)

        btn_update = Button(button_frame, text="Update",command=self.update_data, font=("Forte", 15, "bold"), width=13, bg="peachpuff",
                            fg="black")
        btn_update.grid(row=1, column=0, padx=1, pady=5)

        btn_delete = Button(button_frame, text="Delete",command=self.delete_data, font=("Forte", 15, "bold"), width=13, bg="peachpuff",
                            fg="black")
        btn_delete.grid(row=2, column=0, padx=1, pady=5)

        btn_clear = Button(button_frame, text="Clear",command=self.reset_data, font=("Forte", 15, "bold"), width=13, bg="peachpuff", fg="black")
        btn_clear.grid(row=3,column=0,padx=1,pady=5)
        #down frame
        down_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('Bahnschrift',11,'bold'),fg='navy')
        down_frame.place(x=5,y=260,width=1340,height=240)
        # Set the background image for the down_frame
        bg_image2 = Image.open('images/background4.jpg')
        bg_image2 = bg_image1.resize((1340, 240), Image.LANCZOS)
        self.photo_bg2 = ImageTk.PhotoImage(bg_image2)

        bg_label2 = Label(down_frame, image=self.photo_bg2)
        bg_label2.place(x=0, y=0, relwidth=1, relheight=1)
        
        #Search Frame
        Search_frame = LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('Bahnschrift',11,'bold'),fg='navy')
        Search_frame.place(x=2,y=0,width=1330,height=60)
         # Set the background image for the search_frame
        bg_image3 = Image.open('images/background4.jpg')
        bg_image3 = bg_image3.resize((1340, 60), Image.LANCZOS)
        self.photo_bg3 = ImageTk.PhotoImage(bg_image3)
        
        bg_label3 = Label(Search_frame, image=self.photo_bg3)
        bg_label3.place(x=0, y=0, relwidth=1, relheight=1)
        
        #Search By:
        Search_by = Label(Search_frame,text="Search by:",font=("Rockwell",11,"bold"),bg="red",fg="white")
        Search_by.grid(row=0,column=0,sticky=W,padx=5)
        
        # Search ComboBox:
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(Search_frame,textvariable=self.var_com_search,state='readonly',font=('Rockwell',12,'bold'),width=18)
        com_txt_search['value']=("Select Option","Phone","Employee_ID")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)
        
        # Search Entry Feild
        self.var_search=StringVar()
        txt_search=ttk.Entry(Search_frame,textvariable=self.var_search,width=22,font=('Rockwell',11,'bold'))
         # Validation function to restrict input based on ID Proof type
        def validate_proof(value, Select_Option):
         if Select_Option == "Phone":
          return value.isdigit() and len(value) <= 10 or value ==""
         elif Select_Option == "Employee_ID":
          return value.isdigit() and len(value) <= 5 or value == ""
         else:
          return True  

        # Set the validation criteria for the entry field based on the selected ID Proof
        validation = Search_frame.register(lambda P,Select_Option=com_txt_search: validate_proof(P, Select_Option.get()))
        txt_search.config(validate="key", validatecommand=(validation, "%P"))
        txt_search.grid(row=0,column=2,sticky=W,padx=5)
        # Search Button
        btn_search=Button(Search_frame,text='Search',command=self.search_data,font=('Rockwell',11,'bold'),width=14,bg='red',fg='white')
        btn_search.grid(row=0,column=3,padx=5)
        # Show All Button
        btn_show=Button(Search_frame,text='Show All',command=self.fetch_data,font=('Rockwell',11,'bold'),width=14,bg='red',fg='white')
        btn_show.grid(row=0,column=4,padx=5)
        
       # ================EMPLOYEE TABLE=================
        # TABLE FRAME
        Table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        Table_frame.place(x=0, y=60, width=1332, height=140)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(Table_frame, column=('dep', 'degi', 'address', 'dob', 'idproofcomb', 'idproof', 'name', 'email', 'married', 'doj', 'gender', 'phone', 'country', 'salary', 'age','empid','status'),
                                   xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading('dep', text='Department')
        self.employee_table.heading('degi', text='Designation')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('dob', text='DOB')
        self.employee_table.heading('idproofcomb', text='ID Type')
        self.employee_table.heading('idproof', text='ID Number')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('married', text='Married_status')
        self.employee_table.heading('doj', text='DOJ')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('phone', text='Phone')
        self.employee_table.heading('country', text='Country')
        self.employee_table.heading('salary', text='Salary')
        self.employee_table.heading('age', text='Age')
        self.employee_table.heading('empid', text='Employee Id')
        self.employee_table.heading('status', text='work status')
        
        
    
        
        
        
        self.employee_table['show']='headings'
        
        self.employee_table.column("dep",width=100)
        self.employee_table.column("degi",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("idproofcomb",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)
        self.employee_table.column("age",width=100)
        self.employee_table.column("empid",width=100)
        self.employee_table.column("status",width=100)
        
        
        
        
        
        
        
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==========================Function Declaration========================


    def add_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='vin9766',database='proj_emp')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into emp1_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                     (
                                         self.var_dep.get(),
                                         self.var_designation.get(),
                                         self.var_address.get(),
                                         self.var_dob.get(),
                                         self.var_idproofcomb.get(),
                                         self.var_idproof.get(),
                                         self.var_name.get(),
                                         self.var_email.get(),
                                         self.var_married.get(),
                                         self.var_doj.get(),
                                         self.var_gender.get(),
                                         self.var_phone.get(),
                                         self.var_country.get(),
                                         self.var_salary.get(),
                                         self.var_age.get(),
                                         self.var_empid.get(),
                                         self.var_status.get()
                                         
                                    
                                         
                                         
                                         
                                         
                                         
                                     ))
        
                conn.commit()
                self.fetch_data()
                messagebox.showinfo('Success', 'Employee Has Been Added!', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)
        
        

    
     # fetch Data
    def fetch_data(self):
     conn = mysql.connector.connect(host='localhost', username='root', password='vin9766', database='proj_emp')
     my_cursor = conn.cursor()
     my_cursor.execute('select * from emp1_table')
     data = my_cursor.fetchall()
     if len(data) != 0:
        self.employee_table.delete(*self.employee_table.get_children())
        for i in data:
            self.employee_table.insert("", END, values=i)
        conn.commit()
     conn.close()
     
# Get cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']
        
        self.var_dep.set(data[0])
        self.var_designation.set(data[1])
        self.var_address.set(data[2])
        self.var_dob.set(data[3])
        self.var_idproofcomb.set(data[4])
        self.var_idproof.set(data[5])
        self.var_name.set(data[6])
        self.var_email.set(data[7])
        self.var_married.set(data[8])
        self.var_doj.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
        self.var_age.set(data[14])
        self.var_empid.set(data[15])
        self.var_status.set(data[16])
    
    # UPDATE
    def update_data(self):
     if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All fields are required')
     else:
        try:
            update=messagebox.askyesno('update','Are you sure to update this Employee Data?')
            if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='vin9766',database='proj_emp')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update emp1_table set Department=%s,Designation=%s,Address=%s,DOB=%s,ID_Proof=%s,ID_type=%s,Name=%s,Email=%s,Martial_Status=%s,DOJ=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s,Age=%s,Work_Status=%s where Employee_ID=%s',(
                                                                                                                                                                                                                                                           self.var_dep.get(),
                                                                                                                                                                                                                                                           self.var_designation.get(),
                                                                                                                                                                                                                                                           self.var_address.get(),
                                                                                                                                                                                                                                                           self.var_dob.get(),
                                                                                                                                                                                                                                                           self.var_idproofcomb.get(),
                                                                                                                                                                                                                                                           self.var_idproof.get(),
                                                                                                                                                                                                                                                           self.var_name.get(),
                                                                                                                                                                                                                                                           self.var_email.get(),
                                                                                                                                                                                                                                                           self.var_married.get(),
                                                                                                                                                                                                                                                           self.var_doj.get(),
                                                                                                                                                                                                                                                           self.var_gender.get(),
                                                                                                                                                                                                                                                           self.var_phone.get(),
                                                                                                                                                                                                                                                           self.var_country.get(),
                                                                                                                                                                                                                                                           self.var_salary.get(),
                                                                                                                                                                                                                                                           self.var_age.get(),
                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                           self.var_status.get(),
                                                                                                                                                                                                                                                           self.var_empid.get()
                 
                 
                 
                 
                 
                 
                 
                                                                                                                                                                                                                                                           ))
            else:
                if not update:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('success','Employee successfully updated!',parent=self.root)
        except Exception as es:
            messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)
            
            
    #Delete Function
    def delete_data(self):
        if self.var_empid.get()=="":
            messagebox.showerror('Error',"All feilds are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete',"Are you sure you want to delete this employee?",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='vin9766',database='proj_emp')
                    my_cursor=conn.cursor()
                    sql='delete from emp1_table where Employee_ID=%s'
                    value=(self.var_empid.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                    conn.autocommit = True
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee successfully Deleted!',parent=self.root)
            except Exception as es:
             messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)
             
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_designation.set("")
        self.var_address.set("")
        self.var_dob.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_married.set("Select Martial Status")
        self.var_doj.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")
        self.var_age.set("")
        self.var_empid.set("")
        self.var_status.set("")
        self.var_search.set("")
        
    #Search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please choose one option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='vin9766',database='proj_emp')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from emp1_table where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
             messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)
        
                    
        
if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
