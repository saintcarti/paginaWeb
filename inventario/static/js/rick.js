

const apiRick=async(pagina)=>{
    let url="https://rickandmortyapi.com/api/character/?page="+pagina;
    const api= await fetch(url);
    const data=await api.json();
    console.log(data);
    divRes=document.querySelector("#resultado");
    divRes.innerHTML=""
    data.results.map(item=>{
        divItem=document.createElement('div')
        divItem.innerHTML=`
        <div class="card" style="width: 18rem; border-radius:15px;">
            <img src="${item.image}" class="card-img-top" style="border-radius:15px; " alt="...">
            <div class="card-body">
                <h5 class="card-title">${item.name}</h5>
                <p class="card-text"><b>Estatus: </b>${item.status}</p>
                <p class="card-text"><b>Epacie: </b>${item.specie}</p>
                <p class="card-text"><b>Genero: </b>${item.gender}</p>
            </div>
        </div>
        `
        divRes.appendChild(divItem);
    });

}

let currentPage = 1;

document.getElementById('next-button').addEventListener('click', function() {
  currentPage++;
    apiRick(currentPage);
});

document.getElementById('previous-button').addEventListener('click', function() {
    if (currentPage > 1) {
        currentPage--;
        apiRick(currentPage);
    }
});
apiRick(1)