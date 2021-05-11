# MEDISAFE
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Dishant%20Tayade-red)
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Hardik%20Sharma-red)
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Khushi%20Pathak-red)
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Swathi%20Kasoju-red)
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Raghav%20Garg-red)

##GROUP 19 - WAD PROJECT

## Description
Medisafe enables patients book confirmed appointments and maintain their health records with the prescriptions. All your medical records are securely kept in your health account. Just login to Medisafe service, and all records will be in one place. Medisafe provides to keep your medical history digitally. You can see what prescriptions are given. You can make an appointment with your doctor. You can see appointment list as well.

## Modules
### Account
- Account module maintains the records of the users.
- All the primary pages has its backend in this module.
- The user model of the project is in this module.
- forms.py of this module contains the forms for registration of user
- models.py of this module contains the user model.
- urls.py of this module contains the basic urls for login, logout, register, account, etc.
- views.py of this module contains the webresponses of login, logout, register, account, etc


### Appointment
- Appointment module has the models Appointment, Prescriptions, Payments in it.
- It has the backend part for maintaining the records of appointments, prescriptions, payments.
- forms.py of this module contains the forms for appointments, presciptions, payments.
- models.py of this module contains the Appointment, Prescriptions, Payments models.
- urls.py of this module contains the links for appointments, history, presciption.
- views.py of this module contains the functions for webresponses of Appointment, Prescriptions, Payments.

### User Profile
- User Profile module has the User profile models where we can see the profiles for Doctors and Patients
- It maintains the profile records of the users.
- forms.py of this module contains the forms for User profile update and doctor profile.
- models.py of this module contains the user profile models.
- urls.py of this module contains profile related links.
- views.py of this module contains backend for creating account for a patient, updating user profile and the pages accessed by admin.

## Procedure to run the project
- Install Python(3.8.5) (Dont Forget to add it to the path variables)
- Create a virtual environment if you need.
- Download the project and extract or clone it to your pc.
- Now move to the project directory.
- Run the following command.
```
pip install -r requirements.txt
```
- After you have all the requirements, run the following commands.
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
- Now enter following URL in your browser.
```
http://127.0.0.1:8000/
```
- In the above url, you can see the application run.

## Screenshots of website
### Homepage
![homepage1](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/homepage1.png?raw=true)
![homepage2](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/homepage2.png?raw=true)

### Signup Page
![signup](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/signupform.png?raw=true)
### Login Page
![loginpage](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/loginform.png?raw=true)
### Patient's Profile Page
![patientprofile](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/patientaccount.png?raw=true)
### Update profile
![updatepatientprofile](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/patientupdateaccount.png?raw=true)
### Patient Appointments
![patientappointment](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/patientappointment.png?raw=true)
### Patient's History (Prescriptions)
![patientprescriptions](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/patientpriscription.png?raw=true)
### Patients Payment history
![patientpayment](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/paymenthistory.png?raw=true)
### Doctor's Account
![doctoraccount](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/doctoraccount.png?raw=true)
### Doctors Appointments
![doctorappointment](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/doctorappointments.png?raw=true)
### Doctor making new Appointment
![doctornewappointment](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/createappointment.png?raw=true)
### Doctor making new prescriptions
![doctornewprescriptions](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/createpresciption.png?raw=true)
### Blog Page
![blogpage](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/blogpagebyadmin.png?raw=true)
### Women Health Page
![womenhealth1](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/womenhealthage1.png?raw=true)
![womenhealth2](https://github.com/dishanttayade/FourthSemProject/blob/master/screenshots/womenhealthage2.png?raw=true)

## Admin page
- You can create a superuser using the following command.
```
python manage.py createsuperuser
```
- Enter the username, email, password.
- Login with the username and password on following link.
```
http://127.0.0.1:8000/admin
```
- Now you can see the admin page and all the backend of the project

