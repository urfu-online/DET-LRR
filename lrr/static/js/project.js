let resourceListHideElement = document.getElementById('resurse-list-hide');
if (resourceListHideElement != null) {
    resourceListHideElement.addEventListener("click", function () {
        resourceListHideElement.parentNode.classList.toggle('resurse-list-hide')
    })
}


