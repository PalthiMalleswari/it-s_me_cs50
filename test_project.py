
import pytest
from project import send_Email,sender_details,validate_mail

def test_send_email():

    with pytest.raises(AttributeError):
        send_Email('Malli','Hi')

    with pytest.raises(AttributeError):
        send_Email('Malli@gmail','Heloo')

def test_sender_details():
    #assert sender_details('Johnson@gmail.com','XXXX')=='Sent Successfully'
    assert sender_details('HarryPotter.mail.com','yyy')==0

def test_validate_mail():
    assert validate_mail('malli@gmail.com')==True
    assert validate_mail('DavidJmelon@hardvard.edu')==True
    assert validate_mail('Radha123gmail.com')==False
