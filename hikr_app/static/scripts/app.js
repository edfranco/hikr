console.log('Hello Hiker')
const likes = [];
const users = [];
const posts = [];

const getData = response => {
    response.likes.forEach(like => {
        likes.push(like)
    })
    response.users.forEach(user => {
        users.push(user)
    })
    response.posts.forEach(post => {
        posts.push(post)
    })
}

// AJAX Call
const getApi = () => {
    $.ajax({
        url: `/api`,
        method: 'GET',
        success: response => {
            getData(response)
        }, async: false
    })
}



// Event Listener
$('.thumb').on('click', event => {
    pk = event.target.parentNode.parentNode.id
    postLike(pk)
})

getApi();

console.log(posts[0])
// like.post.pk === post.pk
counter = 0
for (let i = 0; i < posts.length; i++) {
    for (let j = 0; j < likes.length; j++) {
        console.log(likes[j])
        if (likes[j].post.pk === posts[i].pk) {
            counter = counter + 1;
        }
    }
}
console.log(counter)