import smtplib    
# Calling SMTP    
s = smtplib.SMTP('smtp.gmail.com', 587)    
# TLS for network security    
s.starttls()    
# User email Authentication    
s.login("patel.sajid436@gmail.com", "********")     #pw at *********
# Message to be sent    
message = "hello Tejasssss"    
# Sending the mail    
s.sendmail("patel.sajid436@gmail.com", "tejasdodal@gmail.com", message)
