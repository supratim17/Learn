from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    def diff(self):
        ago = (timezone.now() - (self.pub_date)).seconds/60
        if(ago<0):
            ago = 0-ago
            return "-"+str(ago)+" minutes later"
    	return str(ago)+" minutes ago"
    
    diff.short_description = 'Last Modified'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text

