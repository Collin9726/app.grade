$(document).ready(function(){
    $('#rating_form').submit(function(event){
      event.preventDefault()
      event.stopImmediatePropagation();
      form = $("#rating_form")
      $('#rating_form').fadeOut()
  
      $.ajax({
        'url':'/ajax/rateproject/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(data){
        //   alert(data['success']);
          if(data.success){ 
            setTimeout(function(){
                 location.reload(); 
            }, 1000); 
         }
        },
      })// END of Ajax method     
      
    }) // End of submit event    
  
  })