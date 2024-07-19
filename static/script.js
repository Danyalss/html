document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const textInput = document.getElementById('textInput').value.trim();

    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('result').innerText = data;
        if (textInput) {
            navigator.clipboard.writeText(textInput).then(() => {
                console.log('متن به کلیپبورد کپی شد.');
            });
        }
    })
    .catch(error => {
        console.error('خطا:', error);
    });
});
