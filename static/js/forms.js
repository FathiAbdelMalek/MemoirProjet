function openForm() {
  document.getElementById("registerForm").style.display = "block";
}

function closeForm() {
  document.getElementById("registerForm").style.display = "none";
}

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})

var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
