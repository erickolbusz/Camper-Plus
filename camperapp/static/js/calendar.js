$(document).ready(function() {
	$('#calendar').fullCalendar({
        header: {
					left: 'prev,next today',
					center: 'title',
					right: 'month,agendaWeek,agendaDay,listMonth'
				},
                themeSystem: 'jquery-ui',
                defaultView: 'agendaWeek',
                nowIndicator: true,
				navLinks: true, // can click day/week names to navigate views
				editable: true,
				eventLimit: true, // allow "more" link when too many events

                selectable: true,
                selectHelper: true,

                //Click on Existing Event

                eventClick: function(calEvent, jsEvent, view)
                {
                    window.console.log(calEvent)
                    $('#eventModal').modal('open');
                    $("#eventTitle").val(calEvent.title);
                    $('#deleteEvent').removeClass("disabled")
                    $("#eventStartDate").val(calEvent.start.format('YYYY-MM-DD'))
                    $("#eventStartTime").val(calEvent.start.format('HH:mm:ss'))
                    $('#eventEndDate').val(calEvent.end.format('YYYY-MM-DD'))
                    $('#eventEndTime').val(calEvent.end.format('HH:mm:ss'))
                    //var startTime = $.fullCalendar.moment(calEvent.start);
                    //alert('Event: ' + calEvent.title);
                    //alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
                    //alert('View: ' + view.name);

                    // change the border color just for fun
                    //$(this).css('border-color', 'red');

                },
                //Create New Event
                select: function(start, end)
                {
                    $('#eventModal').modal('open');
                    $("#eventTitle").val('');
                    $('#deleteEvent').addClass("disabled")
                    $("#eventStartDate").val(start.format('YYYY-MM-DD'))
                    $("#eventStartTime").val(start.format('HH:mm:ss'))
                    $('#eventEndDate').val(end.format('YYYY-MM-DD'))
                    $('#eventEndTime').val(end.format('HH:mm:ss'))


                    //var title = prompt("Enter event title")
				    var eventData;
				    if (title)
                    {

                    //event data produced here should be stored in database
					    eventData = {
						    title: title,
						    start: start,
						    end: end
					        };

					$('#calendar').fullCalendar('renderEvent', eventData, true); // stick? = true
				    }

				    $('#calendar').fullCalendar('unselect');
                },

				events: [
					{
						title: 'All Day Event',
						start: '2017-11-09'
					},
					{
						title: 'Long Event',
						start: '2017-10-07',
						end: '2017-11-07',
                        color: 'green'
					},
					{
						id: 999,
						title: 'Repeating Event',
						start: '2017-10-09T16:00:00',
                        color: 'orange'
					},
					{
						id: 999,
						title: 'Repeating Event',
						start: '2017-10-16T16:00:00'
					},
					{
						title: 'Conference',
						start: '2017-10-11',
						end: '2017-10-13'
					},
					{
						title: 'Meeting',
						start: '2017-10-12T10:30:00',
						end: '2017-10-12T12:30:00',
                        color: 'green'
					},
					{
						title: 'Lunch',
						start: '2017-11-6T12:00:00'
					},
					{
						title: 'Meeting',
						start: '2017-11-07T14:30:00'
					},
					{
						title: 'Happy Hour',
						start: '2017-11-10T17:30:00',
                        color: 'green'
					},
					{
						title: 'Dinner',
						start: '2017-11-09T20:00:00'
					},
					{
						title: 'Birthday Party',
						start: '2017-11-07T07:00:00',
                        color: 'brown'
					}
				]
		});

    $('select').material_select();
	});
