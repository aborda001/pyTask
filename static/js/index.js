document.addEventListener('DOMContentLoaded', function() {

	function ajaxli(search) {
		$.ajax({
			url: "/tasksearch",
			method: "POST",
			data: {
				search: search
			},
			success: function(data) {
				$('#tasksTable').html(data)
				$("#tasksTable").append(data.htmlresponse);
			}
		});
	}

	$('#taskSearcher').keyup( () => {
		//llama a la funcion para realizar la consulta
		let search = $('#taskSearcher').val();
		console.log(search);
		ajaxli(search);
	});

	ajaxli("");
});