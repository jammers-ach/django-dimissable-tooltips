from django.db import models

# Create your models here.


class DissmissableToolTip(models.Model):
    unique_id = models.SlugField(max_length=100,verbose_name='Unique ID',help_text='A string, with no spaces, e.g. help-page-add-user',unique=True,db_index=True)
    text = models.TextField(verbose_name='Tooltip text',help_text='Html text for this tooltip, e.g. &lt;b&gt;User&ltb&gt; date of birth')

    def __unicode__(self):
        return self.unique_id

class HasSeen(models.Model):
    user = models.ForeignKey('auth.User')
    dtt = models.ForeignKey(DissmissableToolTip)
