$(function () {
	$('#show_login_dialog').on('click', function() {
		$.loadmodal({
			url: '/homepage/login.loginform/',
			title: 'Login',
			id: 'login_dialog',
		});
	});

	$('button[id^="product_"]').on('click', function() {
		var pid = $(this).attr('data-pid');
	    var id = 'quantity_' + pid
	    var qty = $("#" + id).val();

	    $.loadmodal({
	      url: '/homepage/shoppingcart.add/' + pid + '/' + qty,
	      title: 'Shopping Cart',
	      id: 'view_shopping_cart',
	      width: '800px',
	      closeButton: true,
	    });
	});

	$('#shopping_cart').on('click', function() {
    $.loadmodal({
      url: '/homepage/shoppingcart/',
      title: 'Shopping Cart',
      id: 'button_view_shopping_cart',
      width: '800px',
    });
  });
});
