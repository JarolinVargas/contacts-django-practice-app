const contactComponents = document.querySelectorAll(".contact");
const addButton = document.querySelector(".btn-add");

contactComponents.forEach((component) => {
  component.querySelector(".btn-action").addEventListener("click", (event) => {
    event.preventDefault();
    if (component.classList.contains("save-mode")) {
      component.submit();
    }
    component.classList.toggle("save-mode");
  });

  const deleteCheckbox = component.querySelector(".delete-checkbox");
  if(  deleteCheckbox ) {
    deleteCheckbox.addEventListener("change", () => {
      component.submit();
    });
  }
});

addButton.addEventListener("click", () => {
  document.querySelector("#new-contact").classList.toggle("visible")
});