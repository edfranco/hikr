console.log('Hello Hiker')

// Got this code from https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
// End stolen code

// AJAX Call
const getApi = () => {
    $.ajax({
        url: `/api`,
        method: 'GET',
        success: response => {
            console.log(`Here is what I got`, response)
        }
    })
}

const postLike = (pk) => {
    $.ajax({
        url: `/like_post/${pk}`,
        method: 'POST',
        success: function (response) {
            console.log(response)
        }

    })
}

// Event Listener
$('.thumb').on('click', event => {
    pk = event.target.parentNode.parentNode.id
    postLike(pk)
})

getApi();