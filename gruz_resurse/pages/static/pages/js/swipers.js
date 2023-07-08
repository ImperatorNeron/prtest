var swipers = [
  { container: ".mySwiper", thumbsContainer: ".mySwiper2" },
  { container: ".mySwiper4", thumbsContainer: ".mySwiper3" },
  { container: ".mySwiper6", thumbsContainer: ".mySwiper5" }
];

swipers.forEach(function(swiperData) {
  var swiper = new Swiper(swiperData.container, {
    loop: true,
    spaceBetween: 10,
    slidesPerView: 3,
    freeMode: true,
    watchSlidesProgress: true,
    breakpoints: {
      1101: {
        slidesPerView: 4
      }
    }
  });

  var thumbsSwiper = new Swiper(swiperData.thumbsContainer, {
    loop: true,
    slidesPerView: 1,
    spaceBetween: 30,
    centeredSlides: true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev"
    },
    thumbs: {
      swiper: swiper
    },
    breakpoints: {
      1100: {
        slidesPerView: 1.3
      }
    }
  });
});
