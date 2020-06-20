# Full_throttle_labs_test1
This dajngo api was created as an assignment
it is hosted at 'http://bryan23.pythonanywhere.com/members/' using python anywhere the link is valid only till '20 spetember 2020'
it has cutsom command to pouplate the database with dummy data


'python manage.py mycommand 10'

the above command(mycommand) when run will insert 10 dummy records into the database

when a user visits the site 'http://bryan23.pythonanywhere.com/members/' data in the form of json will be served

a sample data is

{"ok": true, "members": [{"id": "Hg5clnEzu", "real_name": "Frank Jackson MD", "tz": "Asia/Kolkata", "activity_periods": [{"start_time": "April 19 2020 11:43 AM", "end_time": "May 03 2020 05:17 AM"}, {"start_time": "April 19 2020 11:43 AM", "end_time": "May 03 2020 05:17 AM"}, {"start_time": "April 19 2020 11:43 AM", "end_time": "May 03 2020 05:17 AM"}]},

                        {"id": "nrY9613fq", "real_name": "Alejandra Smith", "tz": "Asia/Kolkata", "activity_periods": [{"start_time": "April 19 2020 11:43 AM", "end_time": "May 03 2020 05:17 AM"}, {"start_time": "April 19 2020 11:43 AM", "end_time": "May 03 2020 05:17 AM"}, {"start_time": "April 19 2020 11:43 AM", "end_time": "May 03 2020 05:17 AM"}]}
                        ]
 }
