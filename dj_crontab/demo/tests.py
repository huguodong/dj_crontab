from django.test import TestCase
from demo.models import User
import datetime
# Create your tests here.
def test():
    user=User()
    user.time=datetime.datetime.now()
    user.save()
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
