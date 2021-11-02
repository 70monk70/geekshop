window.onload = function render_baskets(){
    $('.basket_list ').on('click', 'input[type="number"]', function () {
        let t_href = event.target;
        console.log(t_href)

        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function(data) {
                $('.basket_list').html(data.result);
            }
        })
    })
}

window.onload = function add (){
    $('.products ').on('click', 'button[type="button"]', function () {
        let z_href = event.target;

        $.ajax({
            url: '/baskets/add/' + z_href.id + '/',
            success: function(data) {
                console.log(z_href)
                $('.products').html(data.result);
            }
        })
    })
}