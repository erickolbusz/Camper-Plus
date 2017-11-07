//<i class="material-icons">create</i><button class="group1">Group 1</button><br>
var groupDisplay = $("#groups");
var groups = [];

var	addNewGroup = function(name, color, members) {
	groups.push({
		name: name,
		color: color,
		members: members
	});
}

var editGroup = function(name, newColor, newMembers) {
}