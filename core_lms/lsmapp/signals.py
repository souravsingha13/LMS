from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Book


@receiver(post_save, sender=Book)
def book_created_confirmation(sender, instance, created, **kwargs):
    
    if created:
        subject = 'New Book Added: {}'.format(instance.title)
        message = 'A new book titled "{}" has been added to the library.'.format(instance.title)
        recipient_list = ['souravsingha1304021@gmail.com']
        send_mail(subject, message, None, recipient_list)