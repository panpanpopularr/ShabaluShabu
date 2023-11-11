let allfile = []
document.getElementById('fileinput').addEventListener('change', async() => {
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