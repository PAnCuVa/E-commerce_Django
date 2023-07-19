let ENDPOINT = 'http://localhost:8000/'

let form = document.getElementById('formulario')

form.addEventListener('submit', async(event)=>{
    //event.preventDefault()
    let formData = new FormData(form)

    let data = {
        "contact_name": formData.get('nombre'),
        "contact_phone_number": formData.get('telefono'),
        "contact_email": formData.get('correo'),
        "contact_message": formData.get('mensaje')
    }

    let response = await fetch(ENDPOINT+'contact/getcontactform/', {
        method: 'POST',
        type: 'json',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    let info = await response.json()
})






