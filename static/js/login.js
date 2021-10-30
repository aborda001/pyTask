document.addEventListener('DOMContentLoaded', function() {
	const btnRegister = document.getElementById('btnRegister');
	const btnLogin = document.getElementById('btnLogin');
	const btnCrearCuenta = document.getElementById('btnCrearCuenta');

	function ajaxUsername(username, password) {
		$.ajax({
			url: "/newusername",
			method: "POST",
			data: {
				username: username,
				password: password
			},
			success: (data) => {
				data = data.Data
				$.notify(`${data}`, "success");
			},
			error: (error) =>{
				error = error.responseJSON.Data;
				$.notify(`${error}`, "danger");
			}
		});
	}

	btnRegister.onclick = (e) => {
		e.preventDefault();
		$('#modalRegistro').modal('show');
	}

	btnCrearCuenta.onclick = () => {
		username = $('#usernameModal').val()
		password = $('#passwordModal').val()
		ajaxUsername(username,password)
	}

});