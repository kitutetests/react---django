
    // Initialize Swiper
    var mySwiper = new Swiper('.swiper-container', {
       
        loop: true, // enables loop mode
        pagination: {
            el: '.swiper-pagination', // pagination container
            clickable: true, // allows clicking on pagination bullets
        },
        navigation: {
            nextEl: '.swiper-button-next', // next button selector
            prevEl: '.swiper-button-prev', // previous button selector
        },
        
    });

    // Pause button event listener
    document.querySelector('.play-button').addEventListener('click', function () {

        if (mySwiper.autoplay.running) {
            mySwiper.autoplay.stop();
            this.innerHTML = '<i class="fa fa-play" aria-hidden="true"></i>';
        } else {
            mySwiper.autoplay.start();
            this.innerHTML = '<i class="fa fa-pause" aria-hidden="true"></i>';
        }// stop autoplay
    });

    
