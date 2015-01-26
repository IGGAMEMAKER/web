from django.core.management.base import BaseCommand

from optparse import make_option

from ask.models import Profile, Question, Answer, Like, TextSet, Tag
from django.contrib.auth.models import User

from faker.frandom import random
from faker.lorem import sentence, sentences
from mixer.fakers import get_username, get_email

from pprint import pformat

class Command(BaseCommand):
	option_list = BaseCommand.option_list + (
		make_option('--users',
		    	action='store',
		    	dest='users',
		   	default=0,
		),
		make_option('--questions',
		    	action='store',
		    	dest='questions',
		   	default=0,
	    	),
		make_option('--upd',
		    	action='store',
		    	dest='questions',
		   	default=0,
	    	),
		make_option('--answers',
		    	action='store',
		    	dest='answers',
		   	default=0,
	    	),
	)
	#def handle(self, *args, **kwargs):
	def handle(self, *args, **options):
		#print('hello')
        	#print "USERS {} , Q :{}, A : {}".format(options['users'], options['questions'], options['answers'])
		names = {}
		while(len(names.keys())<int(options['users'])):
			names[get_username(length=30)]=1

		#print pformat(names)
		for name in names.keys():
			u = User.objects.create(username=name, email=get_email())
			p = Profile.objects.create(user_id=u.id, rating = random.randint(0,20))


		for i in range(0,int(options['questions'])):
			tset= TextSet.objects.create(author_id=random.randint(1, 100), text = sentences(3), likes = random.randint(1, 100))
			q = Question.objects.create(title = (sentence())[0:59],text=tset)

		#for i in range(0,int(options['upd'])):
			#Question.objects.filter(id>0).update(likes = random.randint(1, 100) )

		#title = (sentence())[0:10],
		count = Question.objects.count()
		print 'Count:' + str(count)
		for j in range(0,int(options['answers'])):
			q = Question.objects.get(id= random.randint(1,int(count) ))
			tset = TextSet.objects.create(author_id=random.randint(1, 100), text = sentences(3), likes = random.randint(1, 100))
			a = Answer.objects.create(question=q, text= tset, view_counter = random.randint(1,100) )
		


