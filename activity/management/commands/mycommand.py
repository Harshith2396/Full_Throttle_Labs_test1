from django.core.management import BaseCommand
import activity.createdates as dates
from faker import Faker
import random
import activity.createdates as dates
from django.utils.crypto import get_random_string
from activity.models import Myuser,Activity_period
timezones=['Americas/Los_Angelos',"Asia/Kolkata",'Asia/Hongkong',]
class Command(BaseCommand):
    help='creates records of desired number'
    def add_arguments(self, parser):
        return parser.add_argument('total',type=int)
    def handle(self, *args, **kwargs):
        fakers=Faker()
        total=kwargs['total']
        for _ in range(total):
            user_id=get_random_string(9)
            name=fakers.name()
            password=fakers.password()
            email=fakers.email()
            tz=random.choice(timezones)
            try:
                Myuser.object.create_user(email,password,user_id,tz)
                for i in range(3):
                    start,end=dates.return_dates()
                    print(start)
                    Activity_period.objects.create(start_time=start,end_time=end,email_id=email)
            except :
                pass
        print("Done with inserting {} records".format(total))