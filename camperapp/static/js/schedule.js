var setup = function(group) {
	group.onclick = function() {
		console.log(group.id);
	}
}

$(document).ready(function() {     
  $('.modal').modal();
  $('.trigger-modal').modal();

  var groups = $("#groups")[0];
  for (var i=0; i<groups.childElementCount; i++) {
  	if (groups.children[i].className == "group") {
  		var group = groups.children[i]
			setup(group);
		}
	}
});

