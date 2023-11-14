let allfile = []

document.addEventListener('DOMContentLoaded', async () => {
    document.getElementById("allinone").checked = true;
    document.getElementById('submitt').addEventListener('click', () => {

        console.log("Uploading file...");
        const API_ENDPOINT = "/";
        const request = new XMLHttpRequest();
        const formData = new FormData();

        request.open("POST", API_ENDPOINT, true);
        request.responseType = 'blob';
        for (let i = 0; i < allfile.length; i++) {
            formData.append(allfile[i].name, allfile[i])
        }
        console.log(document.getElementById("allinone").checked)
        formData.append('filetype', document.getElementById("allinone").checked ? 'allinone' : 'onetoone')
        request.send(formData);
        let dwntab = document.getElementById('downloadtab')
        request.onload = () => {
            var link = document.createElement('a');
            if (request.readyState === request.DONE && request.status === 200) {
                if (document.getElementById("allinone").checked) {

                    var blob = new Blob([request.response], { type: 'application/pdf' });
                    
                    link.href = window.URL.createObjectURL(blob);
                    link.download = 'images.pdf';
                } else {
                    var blob = new Blob([request.response], { type: 'application/zip' });
                    var link = document.createElement('a');
                    link.href = window.URL.createObjectURL(blob);
                    link.download = 'images.zip';
                }
                let img = document.createElement('img')
                img.src = document.getElementById("allinone").checked ? "https://icons.veryicon.com/png/o/file-type/system-icon/pdf-45.png" : "https://cdn-icons-png.flaticon.com/512/5105/5105197.png"
                img.style.width = "40px"
                link.innerText = "Download here"
                let dwntb = document.getElementById('downloadlist')
                let downloader = document.createElement('div')
                downloader.appendChild(img)
                downloader.appendChild(link)
                link.click()
                let row = dwntb.insertRow(0)
                row.appendChild(downloader)
                
            }
        }
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
