# heart_rate_sentinel_server

This code works by sending 'requests.get' or 'requests.post' to 
the server. The user can post patient information (patient_id, 
attending_email, user_age) to the server that stores the data 
into a Mongo database. The user can then post heart rate data
to the server along with the user_id, to add heart rate data 
to an existing patient.  

The user can then make get requests to determine the following:
list of all heart rates, average heart rate over all values, 
average heart rate since a given time, and the status of the 
patient to determine if they are tachycardic. In order to get 
this information the user must input the user_id, in order for 
the server to access the information on that user. 

When determining if the patient is tachycardic, if the result
comes back 'true' (they are tachycardic) an email is sent to 
the patient, using the email associated with their data. 

In order to determine the average since a given time, the user
must make a request post with the user_id, and specified time 
using te UTC time stamp. 

