
let exampleNode = document.createElement("div");
exampleNode.classList.add("images__body");

let images__img = document.createElement("img");
images__img.classList.add("images__img");
images__img.src = "#";
images__img.alt = "nothing here";

let images__name = document.createElement("h2")
images__name.classList.add("images__name")
images__name.innerHTML = "Your Text"

exampleNode.appendChild(images__img)
exampleNode.appendChild(images__name)

console.log(exampleNode)

document.querySelector('#inp').onchange = function() {
    removeAllImages()
    for(i = 0; i < this.files.length; i++) {
        addImage(this.files[i], this.files[i].name)
    }
}

function addImage(file, name) {
    const reader = new FileReader();
    reader.onload = function() {
        upladed_img = this.result
        createImgElem(upladed_img, name)
    }

    function createImgElem(url, name) {
        const push_to = document.querySelector(".images");
        let copiedNode = exampleNode.cloneNode(true)
        copiedNode.querySelector('.images__img').src = `${url}`
        copiedNode.querySelector('.images__name').innerHTML = `${name}`
        console.log(name)
        copiedNode.style.display = "flex"
        push_to.appendChild(copiedNode)
    };

    reader.readAsDataURL(file)
};

function removeAllImages() {
    let list = document.querySelectorAll(".images__body")
    for(i = 0; i < list.length; i++ ) {
        list[i].remove()
    }
    console.log(list)
}