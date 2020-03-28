$(function()
{
	$(document).on('click','.list-down-btn',function(event)
  {
  	event.preventDefault();
    var target = $(this).attr('data-toggle');
    $(target).slideToggle();
    var clicked = event.target;
    $(clicked).toggleClass("fa-chevron-down  fa-chevron-up");
  });
});



