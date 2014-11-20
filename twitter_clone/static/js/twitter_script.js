$(document).ready(function(){

  var $button = $('.tweet-button');
  var $textbox = $('.tweet-box');


  $('.tweet-form').on('submit',function(e){
      event.preventDefault()

      if ($textbox.val() === ""){
        return;
      }

      var text = $textbox.val();
      var id = $button.attr('data-id');
      $textbox.val("");
      $.ajax({
        url: '/twitter/' + id + '/tweets/',
        type: 'POST',
        data: {tweet: text},
        success: function(resp){
          data = jQuery.parseJSON(resp);
          var $listItem = $("<li class='list-group-item'></li>");
          $listItem.append('<h3>' + data.author + ' - ' + data.text + '</h3>');
          $listItem.append('<br>');
          $listItem.append(data.time);
          $('.tweet-list').prepend($listItem)
        }
      });
  });

});
