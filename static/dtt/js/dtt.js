
var dtt_template_text = '<div class="popover dttpopover" role="tooltip"> \
<div class="arrow"></div> \
<div class="popover-content"></div>\
<div class="popover-remove"><label><input type="checkbox"/>Don\'t show me this again </label></div> \
<a href="#" class="dttclose"><span class="glyphicon glyphicon-remove" aria-hidden="true"></span></a> \
</div>';


function make_tooltip_text(element,popup_id,text,placement){
    placement = placement || 'auto';
    element.popover({
        html:true,
        content:text,
        placement:placement,
        template:dtt_template_text,
    }).popover('show');

    var id = element.attr('aria-describedby');
    console.log(id);
    $('#' + id).find('input[type=checkbox]').bind('change',function(e){
        $(this).closest('.popover').popover('destroy');
        console.log(popup_id);
        $.ajax({
            url:'/dtt/hide_popup',
            data:{p:popup_id}
        }).done(function(data){});
    });

}

$(function(){
    $('.dtt').each(function(){
        var us = $(this);
        var position =us.attr('data-position');
        var popup_id = us.attr('data-pid');
        var text = us.attr('data-content');
        make_tooltip_text(us,popup_id,text,position);
    });

    $(document).on('click','.dttclose',function(e){
        e.preventDefault();
        $(this).closest('.popover').popover('destroy');
    });

});
