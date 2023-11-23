import tkinter as tk
from tkinter import StringVar, Label, Frame, Scrollbar, ttk, RIDGE
from tkinter import W
import random
import time
import datetime
import tkinter.messagebox

class Hospital(tk.Tk):
    def __init__(self, title, size, **configure):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}+0+0')
        self.configure(**configure)

        self.cmbNameTablets = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NumberTablets = StringVar()
        self.Lot = StringVar()
        self.IssuedDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.PossibleSideEffects = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachines = StringVar()
        self.HowtoUseMedication = StringVar()
        self.PatientID = StringVar()
        self.PatientNHSNo = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()
        self.Prescription = StringVar()

        #===============================================Funtion=========================================   

        def iExit():
            result = tkinter.messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
            if result:
                # Use self.destroy() instead of root.destroy()
                self.destroy()


        def iPrescription():  
            self.txtPrescription.insert(tk.END, 'Name of Tablets: \t\t\t\t' + self.cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(tk.END, 'Reference No: \t\t\t\t' + self.Ref.get() + "\n")
            self.txtPrescription.insert(tk.END, 'Number of Tablets: \t\t\t\t' + self.NumberTablets.get() + "\n")
            self.txtPrescription.insert(tk.END, 'Lot: \t\t\t\t' + self.Lot.get() + "\n")
            self.txtPrescription.insert(tk.END, 'Issued Date: \t\t\t\t' + self.IssuedDate.get() + "\n")
            self.txtPrescription.insert(tk.END, 'Exp. Date: \t\t\t\t' + self.ExpDate.get() + "\n")
            self.txtPrescription.insert(tk.END, 'Daily Dose: \t\t\t\t' + self.DailyDose.get() + "\n")
            self.txtPrescription.insert(tk.END, 'Possible Side Effects: \t\t\t\t' + self.PossibleSideEffects.get() + "\n")
            self.txtPrescription.insert(tk.END, 'Further Information: \t\t\t\t' + self.FurtherInformation.get() + "\n")
            return

        
        def iSave():
            self.txtFrameDetail.insert(tk.END, self.cmbNameTablets.get() + "\t\t" + self.Ref.get() + "\t" + self.Dose.get() + "\t\t"
                + self.Lot.get() + "\t" + self.IssuedDate.get() + "\t" + self.ExpDate.get() + "\t" + self.DailyDose.get() + "\t" +
                self.StorageAdvice.get() + "\t" + self.PatientNHSNo.get() + "\t" + self.PatientName.get() + "\t" + self.DateofBirth.get() + 
                "\t" + self.PatientAddress.get() + "\n")
            
            #Needed in order for our save data to display on dataframe
            # Set state to normal to allow editing
            self.txtFrameDetail.config(state="normal")
            self.txtFrameDetail.insert(tk.END, self.cmbNameTablets.get() + "\t\t" + self.Ref.get() + "\t" + self.Dose.get() + "\t\t"
                + self.Lot.get() + "\t" + self.IssuedDate.get() + "\t" + self.ExpDate.get() + "\t" + self.DailyDose.get() + "\t" +
                self.StorageAdvice.get() + "\t" + self.PatientNHSNo.get() + "\t" + self.PatientName.get() + "\t" + self.DateofBirth.get() + 
                "\t" + self.PatientAddress.get() + "\n")
            # Set state back to disabled
            self.txtFrameDetail.config(state="disabled")
            return
        
        def iDelete():
            # Get the selected text indices
            sel_start = self.txtFrameDetail.index(tk.SEL_FIRST)
            sel_end = self.txtFrameDetail.index(tk.SEL_LAST)

            # Delete the selected text
            self.txtFrameDetail.delete(sel_start, sel_end)

            return
        
        def iReset():
            self.cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            self.Ref.set("")
            self.Dose.set("")
            self.NumberTablets.set("")
            self.Lot.set("")
            self.IssuedDate.set("")
            self.ExpDate.set("")
            self.DailyDose.set("")
            self.PossibleSideEffects.set("")
            self.FurtherInformation.set("")
            self.StorageAdvice.set("")
            self.DrivingUsingMachines.set("")
            self.HowtoUseMedication.set("")
            self.PatientID.set("")
            self.PatientNHSNo.set("")
            self.PatientName.set("")
            self.DateofBirth.set("")
            self.PatientAddress.set("")
            self.txtPrescription.delete("1.0", tk.END)
            #self.txtFrameDetail.delete("1.0", tk.END)
            return

        #===============================================FRAME=========================================  
        MainFrame = Frame(self)
        MainFrame.grid()
        #Title Box
        TitleFrame = Frame(MainFrame, bd=5, width=1350, padx=260, pady=10, relief=tk.RIDGE)
        TitleFrame.pack(side=tk.TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 40, 'bold'), text="Hospital Management Systems", padx=8)
        self.lblTitle.grid()

        # Section Framing/Record box containing the save data
        FrameDetail = Frame(MainFrame, bd=5, width=1000, height=560, padx=55, relief=tk.RIDGE)
        FrameDetail.pack(side=tk.BOTTOM)
        #Button Box
        ButtonFrame = Frame(MainFrame, bd=5, width=1350, height=50, padx=46, relief=tk.RIDGE)
        ButtonFrame.pack(side=tk.BOTTOM)
        #DataFrame
        DataFrame = Frame(MainFrame, bd=5, width=1350, height=100, padx=20, relief=tk.RIDGE)
        DataFrame.pack(side=tk.BOTTOM)
        #Box containing Patient Info and Prescription
        DataFrameLEFT = tk.LabelFrame(DataFrame, bd=5, width=800, height=300, padx=20, relief=tk.RIDGE, font=('arial', 14, 'bold'), text="Patient Info")
        DataFrameLEFT.pack(side=tk.LEFT)

        DataFrameRIGHT = tk.LabelFrame(DataFrame, bd=5, width=450, height=300, padx=20, relief=tk.RIDGE, font=('arial', 14, 'bold'), text="Prescription")
        DataFrameRIGHT.pack(side=tk.RIGHT)



         #===============================================DATAFRAMELEFT=========================================       

        #Label of Tablet/DataFrameLeft in here puts our framing lblNameTablet in that framing
        self.lblNameTablet= Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Name of Tablets", padx=2, pady=2)
        self.lblNameTablet.grid(row=0, column=0, sticky=W)

        #Note for Field Placement: Row number is what row you want to place label or Field box. Column, is what column you want to place the Label and Field.
        #Column: The grid is being counted by index 0, 1 , 2. Example Label can be index one and to place the box next to it, it would be the next column of 2.

        #Tablet Picklist Field
        self.cboNameTablet= ttk.Combobox(DataFrameLEFT, textvariable=self.cmbNameTablets, state='readonly',font=('arial', 12, 'bold'), width=24)
        self.cboNameTablet['value']=('','Ibuprofen','Co-codamol','Paracetamo','Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)
        
        #Further Info Field
        self.lblFurtherInfo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Further Information:", padx=2, pady=2)
        self.lblFurtherInfo.grid(row=0, column=2, sticky=W)
        self.txtFutherInfo = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.FurtherInformation, width=25)
        self.txtFutherInfo.grid(row=0, column=3, padx=2, pady=2)
        
        #Reference Number Field
        self.lblRef = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Reference No:", padx=2,pady=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.Ref, width=25)
        self.txtRef.grid(row=1, column=1, padx=2, pady=2)
        
        #Storage Advice Field
        self.lblStorage = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Storage Advice#:", padx=2, pady=2)
        self.lblStorage.grid(row=1, column=2, sticky=W)
        self.txtStorage = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.StorageAdvice, width=25)
        self.txtStorage.grid(row=1, column=3, padx=2, pady=2)

        #Dose Field
        self.lblDose = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Dose:", padx=2, pady=2)
        self.lblDose.grid(row=3, column=0, sticky=W)
        self.txtDose = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.Dose, width=25)
        self.txtDose.grid(row=3, column=1, padx=2, pady=2)

        #Number of Tablets Field
        self.lblNumTab = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Number of Tablets:", padx=2, pady=2)
        self.lblNumTab.grid(row=3, column=2, sticky=W)
        self.txtNumTab = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.NumberTablets, width=25)
        self.txtNumTab.grid(row=3, column=3, padx=2, pady=2)

        #Lot Field
        self.lblLot = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Lot:", padx=2, pady=2)
        self.lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.Lot, width=25)
        self.txtLot.grid(row=4, column=1, padx=2, pady=2)

        #Issued Date Field
        self.lblIssuedDate = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Issued Date:", padx=2, pady=2)
        self.lblIssuedDate.grid(row=4, column=2, sticky=W)
        self.txtIssuedDate = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.IssuedDate, width=25)
        self.txtIssuedDate.grid(row=4, column=3, padx=2, pady=2)

        #Expired Date Field
        self.lblExpDate = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Expiration Date:", padx=2, pady=2)
        self.lblExpDate.grid(row=5, column=0, sticky=W)
        self.txtExpDate = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.ExpDate, width=25)
        self.txtExpDate.grid(row=5, column=1, padx=2, pady=2)

        #Daily Dose Field
        self.lblDailyDose = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Daily Dose:", padx=2, pady=2)
        self.lblDailyDose.grid(row=5, column=2, sticky=W)
        self.txtDailyDose = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.DailyDose, width=25)
        self.txtDailyDose.grid(row=5, column=3, padx=2, pady=2)

        #Possible Side Effect Field
        self.lblPossibleSideEffects = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Possible Side Effects:", padx=2, pady=2)
        self.lblPossibleSideEffects.grid(row=6, column=0, sticky=W)
        self.txtPossibleSideEffects = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.PossibleSideEffects, width=25)
        self.txtPossibleSideEffects.grid(row=6, column=1, padx=2, pady=2)

        #Further Information Field
        self.lblFurtherInformation = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Further Information:", padx=2, pady=2)
        self.lblFurtherInformation.grid(row=6, column=2, sticky=W)
        self.txtFurtherInformation = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.FurtherInformation, width=25)
        self.txtFurtherInformation.grid(row=6, column=3, padx=2, pady=2)

        #Storage Advice Field
        self.lblStorageAdvice = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Storage Advice:", padx=2, pady=2)
        self.lblStorageAdvice.grid(row=7, column=0, sticky=W)
        self.txtStorageAdvice = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.StorageAdvice, width=25)
        self.txtStorageAdvice.grid(row=7, column=1, padx=2, pady=2)

        #Driving Using Machines Field
        self.lblDrivingUsingMachines = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Driving Using Machines:", padx=2, pady=2)
        self.lblDrivingUsingMachines.grid(row=7, column=2, sticky=W)
        self.txtDrivingUsingMachines = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.DrivingUsingMachines, width=25)
        self.txtDrivingUsingMachines.grid(row=7, column=3, padx=2, pady=2)

        #How to Use Medication Field
        self.lblHowtoUseMedication = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="How to Use Medication:", padx=2, pady=2)
        self.lblHowtoUseMedication.grid(row=8, column=0, sticky=W)
        self.txtHowtoUseMedication = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.HowtoUseMedication, width=25)
        self.txtHowtoUseMedication.grid(row=8, column=1, padx=2, pady=2)

        #Patient ID Field
        self.lblPatientID = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient ID:", padx=2, pady=2)
        self.lblPatientID.grid(row=8, column=2, sticky=W)
        self.txtPatientID = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.PatientID, width=25)
        self.txtPatientID.grid(row=8, column=3, padx=2, pady=2)

        #Patient NHS No Field
        self.lblPatientNHSNo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient NHS No:", padx=2, pady=2)
        self.lblPatientNHSNo.grid(row=9, column=0, sticky=W)
        self.txtPatientNHSNo = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.PatientNHSNo, width=25)
        self.txtPatientNHSNo.grid(row=9, column=1, padx=2, pady=2)

        #Patient Name Field
        self.lblPatientName = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Name:", padx=2, pady=2)
        self.lblPatientName.grid(row=9, column=2, sticky=W)
        self.txtPatientName = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.PatientName, width=25)
        self.txtPatientName.grid(row=9, column=3, padx=2, pady=2)

        #DOB Field
        self.lblDOB = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date of Birth (DOB):", padx=2, pady=2)
        self.lblDOB.grid(row=10, column=0, sticky=W)
        self.txtDOB = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.DateofBirth, width=25)
        self.txtDOB.grid(row=10, column=1, padx=2, pady=2)

        #Patient Address Field
        self.lblPatientAddress = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Address:", padx=2, pady=2)
        self.lblPatientAddress.grid(row=10, column=2, sticky=W)
        self.txtPatientAddress = ttk.Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=self.PatientAddress, width=25)
        self.txtPatientAddress.grid(row=10, column=3, padx=2, pady=2)

        #===============================================DATAFRAMERIGHT=========================================
        self.txtPrescription=tk.Text(DataFrameRIGHT, font=('arial', 12, 'bold'), width=43, height=12, padx=2, pady=58)
        self.txtPrescription.grid(row=0, column=0)

        #===============================================BUTTONFRAME=========================================
        self.btnPrescription=tk.Button(ButtonFrame, text='Prescription', font=('arial', 12, 'bold'), width=13, bd=4, 
                                       command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)
        
        self.btnSave=tk.Button(ButtonFrame, text='Save', font=('arial', 12, 'bold'), width=13, bd=4,
                                       command=iSave)
        self.btnSave.grid(row=0, column=1)
        
        self.btnDelete=tk.Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'), width=13, bd=4,
                                       command=iDelete)
        self.btnDelete.grid(row=0, column=2)
        
        self.btnReset=tk.Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'), width=13, bd=4,
                                command=iReset)
        self.btnReset.grid(row=0, column=3)
        
        self.btnExit = tk.Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), width=13, bd=4, 
                         command=iExit)
        self.btnExit.grid(row=0, column=4)

        #Search
        self.lblSearch = Label(ButtonFrame, font=('arial', 12, 'bold'), text="Search By", width=13, bd=4)
        self.lblSearch.grid(row=0, column=5,sticky=W)

        search_combo=ttk.Combobox(ButtonFrame, width=12, font=("arial",13,"bold"), state="readonly")
        search_combo.grid(row=0, column=6)
        search_combo["values"]=("Ref", "Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        txtSearch = ttk.Entry(ButtonFrame, takefocus=3, style='TEntry', width=12, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=7)





        #===============================================FRAMEDETAIL COLUMN FIELDS=========================================
        self.lblLabel = Label(FrameDetail,font=('arial', 10, 'bold'), pady=8
        , text="Name of Tablets\tReference No.\t Dosage\t No. of Tablets\t Lot\t Issue Date\t Exp. Date\
        Daily Dose\tStorage Adv.\tNHS Number\t Patient Name\t DOB\t Address"
        ,fg='white')
        self.lblLabel.grid(row=0,column=0)

        # Create a vertical scrollbar
        scrollbar = Scrollbar(FrameDetail)
        scrollbar.grid(row=1, column=1, sticky="ns")

        # The value you enter like tk.Text(FrameDetail), is where you are wanting to place the item
        self.txtFrameDetail = tk.Text(FrameDetail, font=('arial', 12, 'bold'), width=141, height=40, padx=2, pady=4, state="disabled", yscrollcommand=scrollbar.set)
        self.txtFrameDetail.grid(row=1, column=0)

        # Attach the scrollbar to the text widget
        scrollbar.config(command=self.txtFrameDetail.yview)




        #===============================================DATAFRAMERIGHT END=========================================

        # If this runs from python/directly from this file and not imported, run this code
if __name__ == "__main__":
    hospital_app = Hospital('HMS', (1144, 750), background='powder blue')
    hospital_app.mainloop()