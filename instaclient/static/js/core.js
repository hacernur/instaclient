$(document).ready(function(){
	var nextMaxId = ''
	var hashtag = ''
	
	var url = window.location.href;
	var id = url.split('#')[1];

	if(id){
		hashtag = id;
		$('.search-box input').val('#'+id);
		search(null, null, 'id');
	}
	
	$('.prev-hashtags ul').on('click', 'a', function(e){
		$('.search-box input').val($(this).text());
		search($(this), 'prev');
	});
	$('.search-box button').on('click', function(){search($(this), 'input')});
	$('.search-box input').keypress(function(e){if(e.keyCode == 13) search($('.search-box button'), 'input')});
	$('.results button').click(function(){search($(this), null, true)});
	
	(load_hashtag = function(){
		$.ajax({
			url: 'http://localhost:3000/prev-hashtags/',
			success: function(response) {
				$('.prev-hashtags ul li').remove();
				$.each(response, function(i, hashtag){
					$('.prev-hashtags ul').append('<li><a href="#'+hashtag.name+'" clickable="available" hashtag='+hashtag.name+'> #'+hashtag.name+'</a></li>');
				})
			}
		});
	})();

	function c (l) {
		console.log(l);
	}

	function search (t, type, url) {
		if(type === 'input')
			hashtag = $('.search-box input').val();
		else if(type === 'prev')
			hashtag = t.attr('hashtag');
		
		if(url || t.attr('clickable') === 'available' && hashtag){
			$.ajax({
		        url: (function(){
		        	if (url && url !== 'id') { return 'http://localhost:3000/hashtag/' + hashtag + "?id="+ nextMaxId }
		        	else { return 'http://localhost:3000/hashtag/'+ hashtag }
		        })(),
		        beforeSend: function() {
		        	$('.error').hide();
		        	if(url !== 'id') t.attr('clickable', 'not-available');
		        	$('.results img').each(function(i){
		            	$(this).attr('src', 'static/images/loading.gif');
		            });
		        },
		        success: function (response) {
		        	nextMaxId = response.pagination.next_max_id;
		        	if(response.data.length > 0){
		        		$('.results img').each(function(i){
			            	$(this).attr('src', response.data[i].images.thumbnail.url);
			            });
		        	}else{
		        		$('.results img').attr('src', '');
		        	}

		            if(url !== 'id') t.attr('clickable', 'available');
		            load_hashtag();
		        },
		        error: function (xhr, status) {
		        	$('.error').show();
		         	if(url !== 'id') t.attr('clickable', 'available');
		         	$('.results img').attr('src', '');
		        }
		    });
		}
	}
});

