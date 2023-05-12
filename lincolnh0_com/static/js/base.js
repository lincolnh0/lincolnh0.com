document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
      el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });
  }

});

document.addEventListener('DOMContentLoaded', () => {
  // Create handler for message delete button.
  (document.querySelectorAll('.message .message-header .delete') || []).forEach(($delete) => {
    const $notification = $delete.parentNode.parentNode;

    $delete.addEventListener('click', () => {
      $notification.parentNode.removeChild($notification);
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  // Create "login" backdoor to login screen.
  let passphrase = '';
  document.addEventListener('keyup', (e) => {
    passphrase += e.key;
    passphrase = passphrase.slice(-5);
    if (passphrase === 'login') {
      window.location.href = '/accounts/login';
    }
  });
});

document.addEventListener('DOMContentLoaded', () => {
  // Add handler for populating file field names.
  const allFileInputs = document.querySelectorAll('input[type="file"]');
  allFileInputs.forEach(fileInput => {
    fileInput.addEventListener('change', () => {
      if (fileInput.files.length > 0) {
        const fileName = document.querySelector('#' + fileInput.id + ' ~ .file-name');
        fileName.textContent = fileInput.files[0].name;
      }
    })
  })
});
