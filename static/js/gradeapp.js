$(document).ready(function(){
    $('#rating_form').submit(function(event){
      event.preventDefault()
      event.stopImmediatePropagation();
      form = $("#rating_form")
  
      $.ajax({
        'url':'/ajax/rateproject/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(data){
          alert(data['success'])
        },
      })// END of Ajax method
      $('#rating_form').hide()
      
    }) // End of submit event    
  
  })