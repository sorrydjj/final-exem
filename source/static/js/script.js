function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function acceptStatus(event) {
    let pk = event.target.dataset.pk
    let pathname = window.location.pathname
    let element = document.getElementById("block_moderated_" + pk)
    let csrftokens = getCookie('csrftoken');
    let url = "/api/accept/announcemen/".replace(pathname, '')
    let response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({"id": pk, "status": "accept"}),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftokens
        }
    })
    if (response.ok) {
        element.remove()
    } else {
        alert("Операция не удалась")
    }
}

async function rejectStatus(event) {
    let pk = event.target.dataset.pk
    let pathname = window.location.pathname
    let element = document.getElementById("block_moderated_" + pk)
    let csrftokens = getCookie('csrftoken');
    let url = "/api/reject/announcemen/".replace(pathname, '')
    let response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({"id": pk, "status": "reject"}),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftokens
        }
    })
    if (response.ok) {
        element.remove()
    } else {
        alert("Операция не удалась")
    }
}


async function commentModalOpen() {
    let element = document.getElementById("CommentModalOpen")
    element.style.display = "block"
    element.focus()
}

async function modalCommentClose() {
    let element = document.getElementById("CommentModalOpen")
    element.style.display = "none"
}