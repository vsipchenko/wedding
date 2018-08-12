// Select all links with hashes
$('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
    // On-page links
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '')
      &&
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      var header = $('header');
      if (target.length && header.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        var offset = target.offset().top - header.height() - 15;
        $('html, body').animate({scrollTop: offset}, 800);
      }
    }
  });
