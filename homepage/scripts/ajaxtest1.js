$(function () {

  $('#loginform').ajaxForm(function(data) {
    $('#loginform_container').html(data);
  });

});