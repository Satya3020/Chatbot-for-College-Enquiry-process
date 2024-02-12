import csv
from twilio.rest import Client

# Twilio account information
account_sid = 'ACd407488eec7b1e5e1fe654a82a0a5670'
auth_token = '806fcdcdc3f96764ae1ba3b422a10b94'
client = Client(account_sid, auth_token)

# Open the CSV file and read course preferences and phone numbers
with open('course_suggestions.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        phone_number = row['Mobile No.']
        course1 = row['Course Preference 1']
        course2 = row['Course Preference 2']
        name = row['Name']
        # Generate the message
        message = f"\n\nHi {name}! Glad to know your interest in {course1} and {course2}. Please note that admission to LICET is based solely on your academic performance, and we do not encourage any form of donation or influence in the admission process.\n Dont worry, If your score does not meet the cutoff for your desired course, you can apply through Management Quota as well. \nWe look forward to welcoming you to our campus and helping you grow both academically and personally. Please feel free to connect with us on LICET's social media pages to stay updated on the latest news and events.\n\nInstagram: https://www.instagram.com/loyolaicam_official/?hl=en\nLinkedIn: https://www.linkedin.com/school/loyola-icam-college-of-engineering-and-technology/?originalSubdomain=in\n\nBest regards,\nLICET"

        # Replace the placeholders with actual course preferences
        message = message.format(course1=course1, course2=course2,name=name)


        # Send SMS using Twilio
        message = client.messages.create(
            body=message,
            from_='+16203902038',
            to=phone_number
        )

        print(f'Message sent to {phone_number}')
