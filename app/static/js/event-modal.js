function confirmDelete() {
  return confirm("Are you sure you want to delete this event?");
}

function openModal() {
  document.getElementById("editEventModal").classList.remove("hidden");
}

function closeModal() {
  document.getElementById("editEventModal").classList.add("hidden");
}

window.onclick = function (event) {
  const modal = document.getElementById("editEventModal");
  if (event.target === modal) {
    closeModal();
  }
};
