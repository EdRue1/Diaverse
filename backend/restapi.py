#loading flask libraries
import flask

from flask import jsonify
from flask import request

import sql
from sql import create_connection
from sql import execute_read_query
from sql import execute_update_query

import creds
import time


#create application with configuration
app = flask.Flask(__name__)
app.config["DEBUG"]=True #to show errors in browser

#create an endpoint to run default home page request
@app.route('/', methods=['GET'])
def home():
    return "<h1> Welcome </h1>"

#get all applicants
@app.route('/data', methods=['GET'])
def fetch_data():
    mycreds = creds.creds()
    myconn = create_connection(mycreds.myhostname, mycreds.uname, mycreds.passwd, mycreds.dbname)
    mysqltst = "SELECT * FROM Applicants"
    result = execute_read_query(myconn, mysqltst)
    return jsonify(result)

#add an applicant
@app.route('/add', methods=['POST'])
def api_add_applicant():
    request_data = request.get_json()
    #variables for the applicant table
    App_F_Name = request_data['AFirstName']
    App_L_Name = request_data['ALastName']
    App_Date_Of_Birth = request_data['DOB']
    App_Address = request_data['Address']
    App_City = request_data['ACity']
    App_State = request_data['AState']
    App_Zip_Code = request_data['ZipCode']
    App_Email = request_data['Email']
    App_Phone = request_data['APhone']
    App_Four_SSN = request_data['SSN']
    App_US_Citizen = request_data['USCitizen']
    App_Elig_Work = request_data['EligWork']
    App_Cert_True = request_data['CertifyTrue']
    App_Authorize = request_data['Authorize']
    App_No_False = request_data['NoFalseInfo']
    App_Digital_Sign = request_data['DigitalSign']

    
    #connection to DB
    mycreds = creds.creds()
    myconn = create_connection(mycreds.myhostname, mycreds.uname, mycreds.passwd, mycreds.dbname)
    #insert into applicants
    sql = "INSERT INTO Applicants (AFirstName, ALastName, DOB, Address, ACity, AState, ZipCode, Email, APhone, SSN, USCitizen, EligWork, CertifyTrue, Authorize, NoFalseInfo, DigitalSign, created_at) " \
    "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', CURRENT_TIMESTAMP)" % (App_F_Name, App_L_Name, App_Date_Of_Birth, App_Address, 
                                                                                                                              App_City, App_State, App_Zip_Code, App_Email, App_Phone,
                                                                                                                              App_Four_SSN, App_US_Citizen, App_Elig_Work, App_Cert_True,
                                                                                                                              App_Authorize, App_No_False, App_Digital_Sign)
    Applicant_ID = execute_update_query(myconn, sql)

    #time.sleep(3)

    #grabbing the new ID
    #mycursor = myconn.cursor()
    #Applicant_ID = mycursor.lastrowid

    print(f"New applicant ID: {Applicant_ID}")

    #variables for the education table
    Edu_AppID = Applicant_ID
    Edu_School_Name = request_data['SchoolName']
    Edu_City = request_data['ECity']
    Edu_State = request_data['EState']
    Edu_Degree = request_data['Degree']
    Edu_Major = request_data['Major']
    Edu_Start_Year = request_data['EStartYear']
    Edu_End_Year = request_data['EEndYear']
    Edu_Other_Certs = request_data['OtherCerts']


    #insert into education
    sql = "INSERT INTO Education (AppID, SchoolName, ECity, EState, Degree, Major, EStartYear, EEndYear, OtherCerts) " \
    "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (Edu_AppID, Edu_School_Name, Edu_City, Edu_State, Edu_Degree, Edu_Major, Edu_Start_Year, 
                                                                       Edu_End_Year, Edu_Other_Certs)
    execute_update_query(myconn, sql)


    #variables for the prevemp table
    Pre_AppID = Applicant_ID
    Pre_Company_Name = request_data['PCompanyName']
    Pre_City = request_data['PCity']
    Pre_State = request_data['PState']
    Pre_Position = request_data['Position']
    Pre_Duties = request_data['Duties']
    Pre_Start_Year = request_data['PStartYear']
    Pre_End_Year = request_data['PEndYear']
    Pre_Supervisor = request_data['Supervisor']
    Pre_Rea_Leav = request_data['ReaForLeav']
    Pre_May_Contact = request_data['MayContact']


    #insert into prevemp
    sql = "INSERT INTO PrevEmp (AppID, PCompanyName, PCity, PState, Position, Duties, PStartYear, PEndYear, Supervisor, ReaForLeav, MayContact) " \
    "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (Pre_AppID, Pre_Company_Name, Pre_City, Pre_State, Pre_Position, Pre_Duties, Pre_Start_Year, 
                                                                                   Pre_End_Year, Pre_Supervisor, Pre_Rea_Leav, Pre_May_Contact)
    execute_update_query(myconn, sql)


    #variables for the refs table
    Ref_AppID = Applicant_ID
    Ref_First_Name = request_data['RFirstName']
    Ref_Last_Name = request_data['RLastName']
    Ref_Title = request_data['Title']
    Ref_Company_Name = request_data['RCompanyName']
    Ref_Phone = request_data['RPhone']


    #insert into refs
    sql = "INSERT INTO Refs (AppID, RFirstName, RLastName, Title, RCompanyName, RPhone) " \
    "VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (Ref_AppID, Ref_First_Name, Ref_Last_Name, Ref_Title, Ref_Company_Name, Ref_Phone)
    execute_update_query(myconn, sql)


    return 'Add user request successful!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
