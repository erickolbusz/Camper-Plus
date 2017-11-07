//<i class="material-icons">create</i><button class="group1">Group 1</button><br>
var groupDisplay = $("#groups")[0];
var groups = [];

var	addNewGroup = function(name, color, members) {
	groups.push({
		name: name,
		color: color,
		members: members
	});
	updateDisplay();
}

var updateDisplay = function() {
	var s = "";
	for (var i=0; i<groups.length; i++) {
		var group = groups[i];
		s += "<a class=\"modal-trigger\" href=\"#editGroup\"><i class=\"material-icons\">create</i></a><button class=\"group1\" id=\"group"+group.name+"1\">"+group.name+"</button><br>";
	}
	groupDisplay.innerHTML = s;
}

var editGroup = function(name, newColor, newMembers) {
	for (var i=0; i<groups.length; i++) {
		var group = groups[i];
		if (group.name == name) {
			group.color = newColor;
			group.members = newMembers;
		}
	}
	updateDisplay();
}

$(document).ready(function() {     
  $('.modal').modal();
  $('.trigger-modal').modal();
});