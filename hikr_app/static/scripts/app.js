console.log('Hello Hiker')
// AJAX Call
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
}

)