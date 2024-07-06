document.getElementById("btn__registrar").addEventListener("click", register);
document.getElementById("btn__iniciar-sesion").addEventListener("click", iniciarSesion);
window.addEventListener("resize", anchoPagina);


//declaracion de variables
var contenedor_login_register = document.querySelector(".contenedor__login-register");
var formulario_login = document.querySelector(".formulario__login");
var formulario_register = document.querySelector(".formulario__register");
var caja_trasera_login = document.querySelector(".caja__trasera-login");
var caja_trasera_register = document.querySelector(".caja__trasera-register");


//funciones

function anchoPagina(){
    if(window.innerWidth > 850){
        caja_trasera_login.style.display = "block";
        caja_trasera_register.style.display = "block";
    }else{
        caja_trasera_register.style.display = "block";
        caja_trasera_register.style.opacity = "1";
        caja_trasera_login.style.display = "none";
        formulario_login.style.display = "block";
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "0px";
    }
}
anchoPagina();

function iniciarSesion(){
    if(window.innerWidth > 850){
    formulario_register.style.display = "none";
    contenedor_login_register.style.left = "10px";
    formulario_login.style.display = "block";
    caja_trasera_register.style.opacity = "1";
    caja_trasera_login.style.opacity = "0";
    }else{
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "0px";
        formulario_login.style.display = "block";
        caja_trasera_register.style.display = "block";
        caja_trasera_login.style.display = "none";
    }

    
}

function register(){
    if(window.innerWidth > 850){
    formulario_register.style.display = "block";
    contenedor_login_register.style.left = "410px";
    formulario_login.style.display = "none";
    caja_trasera_register.style.opacity = "0";
    caja_trasera_login.style.opacity = "1";
    }else{
        formulario_register.style.display = "block";
        contenedor_login_register.style.left = "0px";
        formulario_login.style.display = "none";
        caja_trasera_register.style.display = "none";
        caja_trasera_login.style.display = "block";
        caja_trasera_login.style.opacity = "1";
    }
}


function mostrarCamaras(){
    let url="http://localhost:3300/mercado";
    fetch(url)
        .then(response => response.json())
        .then(data=>mostrarDatos(data))
        .catch(error=> console.log(error))

    const mostrarDatos=(data)=>{
        console.log(data)
        let body=""
        for (var i = 0;i<data.length;i++){
            body+=`<tr>
                <td class="table-success">ID<br>${data[i].id}</td>
                <td class="table-success">Nombre<br>${data[i].name}</td>
                <td style="display:grid; justify-content:center;  " class="table-success">Imagen<br><img src="${data[i].image}" class="imagenscript"></td>
                <td class="table-success">Precio<br>${data[i].price}</td>
                <td class="table-success">Descripcion<br>${data[i].description}</td>
                </tr>`

        };
        document.getElementById('camaras').innerHTML=body
    }
}



const pass = document.getElementById("pass"),
    icon = document.querySelector(".bx");

icon.addEventListener("click", e=>{
    if(pass.type==="password"){
        pass.type="text";
        icon.classList.remove('bx-show-alt')
        icon.classList.add('bx-hide')

    }else{
        pass.type="password";
        icon.classList.add('bx-show-alt')
        icon.classList.remove('bx-hide')
    }
});


const pass2 = document.getElementById("pass2"),
    icon2 = document.getElementById("icono2");

icon2.addEventListener("click", e=>{
    if(pass2.type==="password"){
        pass2.type="text";
        icon2.classList.remove('bx-show-alt')
        icon2.classList.add('bx-hide')

    }else{
        pass2.type="password";
        icon2.classList.add('bx-show-alt')
        icon2.classList.remove('bx-hide')
    }
});