from django.db import models
from django.contrib.auth.models import User

"""class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete= models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)"""

class Quizz (models.Model):
	title = models.CharField(max_length=200)
	time = models.IntegerField(default=0)
	description = models.CharField(max_length=200)

	def __str__(self):
		return  self.title

class Tag(models.Model):
	tag = models.CharField(max_length=200)	
	def __str__(self):
		return  self.tag

class Question(models.Model):
	QUESTION_CHOICES = (
		('TXT', 'Text'),
		('IMG', 'Image'),
		('DOC', 'Document'),
		('VID', 'Vidéo'),
		('SND', 'Son'),
	)

	question_type = models.CharField(max_length=3, choices=QUESTION_CHOICES, default='Text')
	question_text = models.CharField(max_length=200)
	question_fichier = models.ImageField(upload_to='cars', default='Null')
	question_order = models.IntegerField(default=0)
	quizz = models.ForeignKey(Quizz, blank=True, null=True, on_delete= models.CASCADE)
	tag = models.ForeignKey(Tag, blank=True, null=True, on_delete= models.SET_NULL)	

	def __str__(self):
		return  self.question_text	



class Answer(models.Model):
	ANSWER_CHOICES = (
		('TXT', 'Text'),
		('IMG', 'Image'),
		('SND', 'Son'),
		('IPT', 'Input'),
	)

	Answer_type = models.CharField(max_length=3, choices=ANSWER_CHOICES, default='Text')
	Answer_text = models.CharField(max_length=200)
	Answer_fichier = models.ImageField(upload_to='cars', default='Null')
	Answer_value = models.BooleanField(default=False)
	Answer_order = models.IntegerField(default=0)
	question = models.ForeignKey(Question, blank=True, null=True, on_delete= models.CASCADE)

	def __str__(self):
		return  self.answer_text



class User_profil(models.Model):
	GENDER_CHOICES = (
		('MAL', 'Homme'),
		('FEM', 'Femme'),
		('AUT', 'Autre'),
	)

	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	adress = models.CharField(max_length=200)
	gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
	QPV = models.BooleanField(default=False)
	RQTH = models.BooleanField(default=False)
	tiers_temps = models.BooleanField(default = False)
	quizz= models.ManyToManyField(Quizz)

	def __str__(self):
		return  self.user.username