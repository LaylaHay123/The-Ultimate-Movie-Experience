from app import app
# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# message = Mail(
#     from_email= userdata['email'],
#     to_emails='atticusrothschild@gmail.com',
#     subject='Comments',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     print(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e)
