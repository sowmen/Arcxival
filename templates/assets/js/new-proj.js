$(function(){
    //CHANGE SELECTED VALUE OF CURRENT USER FROM DJANGO
    $('#member-select').trigger('changed.bs.select');
});
$('form').on('keyup keypress', function(e) {
  var keyCode = e.keyCode || e.which;
  if (keyCode === 13) { 
    e.preventDefault();
    return false;
  }
});
$('#member-select').on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    $("#member-table > tbody").html("");
    var data = $(this).val();
    for(var i=0; i<data.length; i++){
        var str = data[i], flag = 0; 
        var name = [], reg = [];
        for(var j=0; j<str.length; j++){
            if(str.charAt(j) == ':'){
                flag = 1;
                continue;
            }
            if(flag == 0)
                name.push(str.charAt(j));
            else
                reg.push(str.charAt(j));
        }
        
        var markup = "<tr><td>" + name.join('') + "</td><td>" + reg.join('') + "</td></tr>";
            $("table tbody").append(markup);
        
    }   
});
