$(document).ready(function () {

  // running the code after some delay to make sure that the DOM is ready once we run the code below

  setTimeout(() => {

    // will work for both statically and dynamically created elements

    $(document).on('mouseover', '.dropdown button', function () {
      let state = $(this).attr('aria-expanded');
      if (state === 'false') $(this).click();
    });


    // when the user clicks on a menu option close the previous ones (if any)

    $(document).on('click', 'a.dropdown-item', function () {
      $('.dropdown_root').click(); // the best way I found it to simulate a click on the menu root, any better way is welcomed
    });

  }, 1000);

});



