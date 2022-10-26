let resourceListHideElement = document.getElementById('resource-list-hide');
if (resourceListHideElement != null) {
    resourceListHideElement.addEventListener("click", function () {
        resourceListHideElement.parentNode.classList.toggle('resource-list-hide')
    })
}

document.onreadystatechange = function () {
    if (document.readyState === "complete") {

        function alertize(alertEl) {
            setTimeout(function () {
                let pb = alertEl.querySelector(".progress-bar");
                let progress = parseInt(pb.getAttribute('aria-valuenow'));
                progress -= 5;
                if (progress >= 0) {
                    pb.setAttribute('aria-valuenow', progress)
                    pb.style.width = progress + '%';
                    alertize(alertEl);
                } else {
                    alertEl.remove();
                    nextAlert();
                }
            }, 200);
        }

        function nextAlert() {
            let alertsSidebar = document.querySelector('#alerts-sidebar');
            if (!alertsSidebar) return;
            let alerts = alertsSidebar.querySelectorAll(' .alert');
            if (alerts.length > 0) {
                alertize(alerts[alerts.length - 1]);

            }
        }

        nextAlert();
    }
}





