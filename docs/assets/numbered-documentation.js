document.addEventListener("DOMContentLoaded", function () {
  const content = document.querySelector(".md-content");

  // Match the path for the desired page
  if (window.location.pathname === "/documentation/") {
    content.classList.add("numbered-sections");
  }
});

