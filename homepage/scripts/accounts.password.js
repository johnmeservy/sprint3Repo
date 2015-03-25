$(function () {
  $('#notification_alert').hide()

  $('#submit_button').on('click', function() {
    $("#notification_alert").text('Your new password was saved!');
    $("#notification_alert").fadeIn("slow");
    $("#notification_alert").delay(5000).fadeOut(2000);
  });//click

  $('#id_cpassword').on('change', function() {
    console.log('change for current password')
    //get the username from the input box
    var cpassword = $('#id_cpassword').val();

    $.ajax({
      url:'/homepage/accounts.check_currentpassword',

      data: {
        a: cpassword,
      },//data

      type:"POST",

      //this is to receive the answer from the server (1 or 0 from .py)
      success: function(resp){
        if (resp == '1'){
          $('#message_center').attr('class','message_success');
          $('#message_center').text("Current password is correct!");
        }else{
          $('#message_center').attr('class','message_error');
          $('#message_center').text('Current password is incorrect.  Please re-enter current password.');
        }
      },
    });//ajax
  });//change

    $('#id_password2').on('change', function() {
    console.log('change for current password')
    //get the username from the input box
    var password1 = $('#id_password1').val();
    var password2 = $('#id_password2').val();

    $.ajax({
      url:'/homepage/accounts.check_newpasswords',

      data: {
        a: password1,
        b: password2,
      },//data

      type:"POST",

      //this is to receive the answer from the server (1 or 0 from .py)
      success: function(resp){
        if (resp == '1'){
          $('#message_center1').attr('class','message_success');
          $('#message_center1').text("Passwords Match!  Click 'submit' to save password.");
        }else{
          $('#message_center1').attr('class','message_error');
          $('#message_center1').text("Your new passwords don't match.  Please re-enter new passwords.");
        }
      },
    });//ajax
  });//change
}); //ready