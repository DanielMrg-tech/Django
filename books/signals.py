from django.db.models.signals import post_save
from django.dispatch import receiver
from books.models import Book
from books.utilis import send_whatsapp_message


@receiver(post_save, sender=Book)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        # print("Message for admin: Book created in DB!!,    with data: {}".format(instance))
        send_whatsapp_message("+40755857226", "New BOOk created! {}".format(instance))
print("Initialized books signal successfully!!")
