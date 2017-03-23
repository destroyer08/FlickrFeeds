
$('body').on('click','.likes', function(){
	var img_id;
	img_id = $(this).attr('img_id');
	$('#'+img_id).html("<b>Liked</b>");
	$(this).hide();

});