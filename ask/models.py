from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	rating = models.IntegerField()
	nickname = models.CharField(max_length=20)
	avatar_url = models.CharField(max_length=60)

class Tag(models.Model):
	word = models.CharField(max_length=60)

class TextSet(models.Model):
	author	= models.ForeignKey(Profile)
	text 	= models.TextField()
	likes 	= models.IntegerField()

	date_added = models.DateTimeField(auto_now_add=True)
	#likes = models.ManyToManyField(Like)

class Like(models.Model):
	author   = models.ForeignKey(Profile)
	positive = models.BooleanField(default=True)
	#like_type = models.BooleanField(default=True)#true - answer, false - question
	text_id = models.ForeignKey(TextSet)



class Question(models.Model):
	text  = models.ForeignKey(TextSet)
	title = models.CharField(max_length=60)
	view_counter =  models.IntegerField()
	#tags = models.ManyToManyField(Tag)

class Answer(models.Model):
	text     = 	models.ForeignKey(TextSet)
	question = 	models.ForeignKey(Question)
	is_right = 	models.BooleanField(default=False)
	






