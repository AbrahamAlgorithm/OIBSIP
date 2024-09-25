import yagmail
import smtplib

def send_email(content):
    confirmation = input("Do you want to send this email? (y/n): ")
    if confirmation.lower() == 'y':
        receiver = 'abrahamalgorithm1@gmail.com'
        message = content
        try:
            # Replace 'your_app_password' with the actual App Password
            sender = yagmail.SMTP('abrahamfolorunso6@gmail.com', 'pbey ilzd xwjr iszu')
            sender.send(to=receiver, subject="Automated mail from Voxia", contents=message)
            print("Email sent successfully!")
        except smtplib.SMTPAuthenticationError:
            print("Authentication failed. Please check your email and App Password.")
            print("Make sure you're using an App Password, not your regular Gmail password.")
            print("You can create an App Password at: https://myaccount.google.com/apppasswords")
        except Exception as e:
            print(f"An error occurred while sending the email: {e}")
    else:
        print("Email cancelled.")
    print("Exiting...")