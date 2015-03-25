$(function () {

  $('#id_username').on('change', function(){
    //console.log('change');
    //ajax is a hidden tab in the background

    //get the username from the input box
    var username = $('#id_username').val();
    //var username = $(this).val();
    //console.log(username);

    //make the ajax call
    //$.ajax({
      //url:'/homepage/ajaxtest.check_username' + username,

    //})://ajax


    //make the ajax call using a dictionary, also gets rid of the / from messing up the params.
    $.ajax({
      url:'/homepage/ajaxtest.check_username',

      data: {
        u: username,
      },//data

      //this is to hide it from the user in the console
      type:"POST",

      //this is to receive the answer from the server (1 or 0 from .py)
      success: function(resp){
        if (resp == '1'){
          $(id_username_message).text('This username is available!');
        }else{
          $(id_username_message).text('This username is unavailable!');
        }
      }

    })://ajax


  });//change

  //console.log($('#id_username'))
  //alert('hey');
  //console.log('world');

}); //ready