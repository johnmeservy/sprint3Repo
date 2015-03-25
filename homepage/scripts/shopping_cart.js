$(function () {

	$('.add_button').on('click', function() {

		var pid = $(this).attr('data-pid');
		// var qty = ;

		$.loadmodal({
			url: "/homepage/shopping_cart.add/" + pid + '/' + qty,
			title: 'Shopping Cart',
			width: '700px',
		});
	});

});
	