# django-dimissable-tooltips
A neat library for those really helpful "You can do this!!! [x] Ok I've got it" tool tips



## how to use

Create a template via the admin interfce, give it a unique id 

Load the dismissable tool tips into your template:
   {%load dtt %}

then place it next to the area you want

{% dtt help-text top %}


## Using the javascript api

you might need to include these dynamic popups in javascript code.

In that case you can get the text by making a request to the url ::

e.e.

  $.url(BLAHL BLAH)


it will return json like:

  {seen:false, tooltip:’’}

or
   {seen:true, tooltip:’’}

you can then use the helpful

 maketooltip(text);

function to make a tooltip
