function openForm() {
  document.getElementById("registerForm").style.display = "block";
}

function closeForm() {
  document.getElementById("registerForm").style.display = "none";
}

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})
