function sendForm() {
	var formData = new FormData(document.getElementById('contactForm'));
	fetch('/contact/send_message/', {
		method: 'POST',
		body: formData,
	})
		.then(response => response.json())
		.then(data => {
			if (data.status === 'success') {
				alert('Message sent successfully.');
			} else {
				alert('Error: ' + data.message);
			}
		})
		.catch(error => {
			console.error('Error:', error);
			alert('Error: Something went wrong.');
		});
}
