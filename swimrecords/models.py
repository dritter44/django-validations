from django.db import models
from django.core.exceptions import ValidationError # import ValidationError from Django

#validates presence of first_name
def validate_fname_not_null(first_name):
    if first_name == None:
        raise ValidationError("This field cannot be blank.")

#validates presence of last_name
def validate_lname_not_null(last_name):
    if last_name == None:
        raise ValidationError("This field cannot be blank.")

#validates presence of team_name
def validate_team_name(team_name):
    if team_name == None:
        raise ValidationError("This field cannot be blank.")

#validates presence of relay
def validate_relay_presence(relay):
    if relay == None:
        raise ValidationError('"None" value must be either True or False.')


class SwimRecord(models.Model):
    first_name = models.CharField(max_length=255,validators=[validate_fname_not_null])
    last_name = models.CharField(max_length=255,validators=[validate_lname_not_null])
    team_name = models.CharField(max_length=255,validators=[validate_team_name])
    relay = models.BooleanField( validators=[validate_relay_presence])
    # stroke = models.CharField()
    # distance = models.IntegerField()
    # record_date = models.DateTimeField()
    # record_broken_date = models.DateTimeField()
