'''
 templatetags/dtt.py - tempalte tag library for DissmissableToolTip
 @author jammers
 @date 2015-05-12
'''

import logging
logger = logging.getLogger(__name__)
from django import template
register = template.Library()
from django_dismissable_tooltips.models import DissmissableToolTip,HasSeen


@register.simple_tag(takes_context=True)
def dtt(context,template_id,position='auto'):

    #Get tooltip, check no badness in position
    tooltip,created = DissmissableToolTip.objects.get_or_create(unique_id=template_id,defaults={'text':'Template not set:%s'% template_id})
    assert position in ['top','left','bottom','right','auto']

    #check to see if this user has decided to cose the popup, if they have, just forget about it all
    hide = False
    if('user' in context):
        hide = HasSeen.objects.filter(user=context['user'],dtt=tooltip).exists()

    if(hide):
        return ''
    else:
        return "<div class='dtt' data-content='%s' data-position='%s' data-pid='%s' ></div>" % (tooltip.text,position,template_id)
