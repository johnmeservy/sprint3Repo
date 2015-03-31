$(function () {

	$('.add_button').on('click', function() {

		var pid = $(this).attr('data-pid');
		// var qty = ;

		$.loadmodal({
			url: "/homepage/shopping_cart.addrental/" + pid + '/' + qty,
			title: 'Shopping Cart',
			width: '700px',
		});
	});

// Search
	$('.searchbar').on('keyup', function(e) {
		var searchTerm = $('.searchbar').val().toLowerCase();
		$('.item_container').each(function() {
			var product = $(this).find('#product').html().toLowerCase(),
				match = false;
			
			// Does the product match the search term?
			if(product.indexOf(searchTerm) != -1) {
				match = true;
			}
			if(match) {
				$(this).show();
			} else {
				$(this).hide();
			}
		});
	});
});
	