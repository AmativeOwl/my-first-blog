# importing info from other files
from django.conf import settings
from django.db import models
from django.utils import timezone

# defines model (object): class - defines an object
# models.Model --> Post is a Django model so saved in database
class Post(models.Model):
    # link to the database/another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # defines text with a limit of 200 characters for title
    title = models.CharField(max_length=200)
    # enables for a long text without a limit for textbox 
    text = models.TextField()
    # defines date and time
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # defining the method "publish"; referencing published_date
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # defining the method "__str__"; referencing title 
    def __str__(self):
        return self.title 