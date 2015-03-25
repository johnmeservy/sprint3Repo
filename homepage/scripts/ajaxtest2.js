$(function () {
	$('#login_dialog').on('click', function() {
		$.loadmodal({
			url: '/homepage/login.loginform/',
		});
	});
});