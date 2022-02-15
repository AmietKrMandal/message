from django.db import models
from twilio.rest import Client

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=200)
    score=models.IntegerField(default=0)

    def __str_(self):
        return self.name

    def save(self,*args,**kwargs):
        if self.score >=70:
            account_sid = 'AC80473f551980446fec5684ecfb68dfd7'
            auth_token = '3ad2007d337deb7d87ebd16efe22e0bb'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"congratulations {self.name},your score is {self.score}",
                     from_='+17752564311',
                     to='+918802694569'
                 )
        else:
            account_sid = 'AC80473f551980446fec5684ecfb68dfd7'
            auth_token = '3ad2007d337deb7d87ebd16efe22e0bb'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"sorry {self.name},your score is {self.score} -->try Again",
                     from_='+17752564311',
                     to='+919634842553'
                 )


            print(message.sid)
            return super().save(*args,**kwargs)