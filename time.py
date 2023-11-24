from datetime import datetime
sign_in = {}
username = input(f'input username: ')
checki = datetime.now()
checkin = checki.strftime("%A, %B %d, %Y %I:%M %p")
sign_in = {checkin:username}