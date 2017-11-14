$(document).ready(function()
{
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
                height: $(window).height()*0.915,
                selectable: true,
                selectHelper: true,

                //Click on Existing Event
                eventClick: function(calEvent, jsEvent, view)
                {
                    ClearPopupFormValues()
                    $('#eventModal').modal('open');
                    $('#event-form').attr('action', 'javascript:updateScheduleForm()');
                    $("#eventTitle").val(calEvent.title);
                    $('#deleteEvent').removeClass("disabled")
                    $("#eventStartDate").val(calEvent.start.format('YYYY-MM-DD'))
                    $("#eventStartTime").val(calEvent.start.format('HH:mm:ss'))
                    $('#eventEndDate').val(calEvent.end.format('YYYY-MM-DD'))
                    $('#eventEndTime').val(calEvent.end.format('HH:mm:ss'))
                    $('#sched-groups').val(calEvent.group)
                    $('select').material_select()
                    //var startTime = $.fullCalendar.moment(calEvent.start);
                    //alert('Event: ' + calEvent.title);
                    //alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
                    //alert('View: ' + view.name);

                    // change the border color just for fun
                    //$(this).css('border-color', 'red');

                },

                //Create New Event
                select: function (start, end)
                {
                    ClearPopupFormValues()
                    $('#event-form').attr('action', 'javascript:submitScheduleForm()');

                    $('#eventModal').modal('open');
                    $("#eventTitle").val('');
                    $('#deleteEvent').addClass("disabled")
                    $("#eventStartDate").val(start.format('YYYY-MM-DD'))
                    $("#eventStartTime").val(start.format('HH:mm:ss'))
                    $('#eventEndDate').val(end.format('YYYY-MM-DD'))
                    $('#eventEndTime').val(end.format('HH:mm:ss'))


                    //var title = prompt("Enter event title")
				    // var eventData;
				    // if (title)
                    // {
                    //
                    // //event data produced here should be stored in database
					//     eventData = {
					// 	    title: title,
					// 	    start: start,
					// 	    end: end
					//         };
                    //
					// $('#calendar').fullCalendar('renderEvent', eventData, true); // stick? = true
				    // }
                    //
				    // $('#calendar').fullCalendar('unselect');
                },

                //Move an Event Around
                eventDrop: function (event, delta, revertFunc, jsEvent, ui, view)
                {
                    if (confirm("Confirm move?")) {
                        //UpdateEvent(event.id, event.start);
                    }
                    else {
                        revertFunc();
                    }
                },

                //Resive an event
                eventResize: function (event, delta, revertFunc, jsEvent, ui, view)
                {
                    if (confirm("Confirm change event length?"))
                    {
                        //UpdateEvent(event.id, event.start, event.end);
                    }
                    else {
                        revertFunc();
                    }
                },

                //events: '/GetCampEvents', -> end point to supply calendar with events
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

        if(calendar)
        {
          $(window).resize(function() {
            var calHeight = $(window).height()*0.915;
            $('#calendar').fullCalendar('option', 'height', calHeight);
          });
        };

        $('select').material_select();
});

//Update event and update the back-end when an event is moved
function updateScheduleForm()
{

    console.log("Updating")
    // var dataRow = {
    //     'ID': EventID,
    //     'NewEventStart': EventStart,
    //     'NewEventEnd': EventEnd
    // }
    // $.ajax({
    //     type: 'POST',
    //     url: "/UpdateEvent",
    //     dataType: "json",
    //     contentType: "application/json",
    //     data: JSON.stringify(dataRow)
    // });
}

//Clear the Values of the Pop Up Form
function ClearPopupFormValues()
{
    $('#eventTitle').val("")
    $("#eventStartDate").val("")
    $("#eventStartTime").val("")
    $('#eventEndDate').val("")
    $('#eventEndTime').val("")
    $('#sched-groups').val("")
    $('select').material_select()
}


//Add New events to Calendar by clicking the Save button
function submitScheduleForm()
{

    console.log("running")
    $('#eventModal').modal('close')

    var dataRow = {
        'title':$('#eventTitle').val(),
        'eventStartDate': $('#eventStartDate').val(),
        'eventStartTime': $('#eventStartTime').val(),
        'eventEndDate': $('#eventEndDate').val(),
        'eventEndTime': $('#eventEndTime').val(),
        'group': $('#sched-groups').val()
    }


    var ISOStartDate = dataRow['eventStartDate'] + 'T' + dataRow['eventStartTime']
    var ISOEndDate = dataRow['eventEndDate'] + 'T' + dataRow['eventEndTime']

    eventData = {
        title: dataRow['title'],
        start: ISOStartDate,
        end: ISOEndDate,
        group: $('#sched-groups').val()
    };

    console.log(eventData)

    $.ajax({
        url: "/saveEvent",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(eventData),
        dataType: "json",
    })

    .done( function (response) {

        if (response)
        {
            color = response['color']
            eventData['color'] = color
            $('#calendar').fullCalendar('renderEvent', eventData, true);
        }

     })

     .fail ( function() {
        Materialize.toast('Error: Check Your Internet Connection', 4000)
     })

     .always (function() {

        $('#calendar').fullCalendar('unselect');
     })

}
