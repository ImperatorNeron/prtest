const swiper = new Swiper('.swiper', {
    loop: true,
    autoplay: {
        delay: 10000,
        disableOnInteraction: false,
    },

    allowTouchMove: true,

    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    breakpoints: {

        1023: {
            allowTouchMove: false,
        }
    }
});