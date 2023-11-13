let allfile = []

document.addEventListener('DOMContentLoaded', async () => {
    document.getElementById("allinone").checked = true;
    document.getElementById('submitt').addEventListener('click', () => {

        console.log("Uploading file...");
        const API_ENDPOINT = "/";
        const request = new XMLHttpRequest();
        const formData = new FormData();
      
        request.open("POST", API_ENDPOINT, true);
        for (let i = 0; i < allfile.length; i++) {
          formData.append(allfile[i].name, allfile[i])
        }
        request.send(formData);
    })

})

document.getElementById('fileinput').addEventListener('change', async () => {
    let filein = document.getElementById('fileinput');
    let filelist = document.getElementById('filelist');
    if (filein.files.length != 0) {
        Array.from(filein.files).forEach(element => {
            let tr = document.createElement('tr');
            let td = document.createElement('td');
            let img = document.createElement('img');
            img.src = URL.createObjectURL(element);
            img.width = '150'
            td.appendChild(img);
            let p = document.createElement('p');
            p.innerText = element.name;
            tr.appendChild(td);
            tr.appendChild(p);
            filelist.append(tr)
            allfile.push(element)

        });
        filein.value = null

    }

})
