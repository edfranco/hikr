$('.btn').on('click', function(event){
    event.preventDefault();
    const element = $(this);
    $.ajax({
      url: '/like_post/',
      method: 'GET',
      data: {post_id: element.attr('data-id')},
      success: function(response) {
          element.html('likes')
      }

    })
})