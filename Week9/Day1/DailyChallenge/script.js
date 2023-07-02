let myForm = document.forms.myForm;

myForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const fname = myForm.fname.value;
    const lname = myForm.lname.value;

    const formData = {
        name: fname,
        lastname: lname,
    };

    const dataStr = JSON.stringify(formData);
    console.log(dataStr)

    const additional = document.createElement("p")
    additional.textContent = dataStr;
    document.body.appendChild(additional);
})