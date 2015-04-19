from django.db import models

# Create your models here.
class User(models.Model):
	firstname = models.CharField(max_length=200, default=None)
	lastname = models.CharField(max_length=200, default=None, null=True)
	hclass = models.CharField(max_length=200) # this is the hacker, hustler, hipster field
	skills = models.CharField(max_length=200)
	githublink = models.CharField(max_length=200, null=True)
	linkedinlink = models.CharField(max_length=200, null=True)
	dribblelink = models.CharField(max_length=200, default=None)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.firstname
