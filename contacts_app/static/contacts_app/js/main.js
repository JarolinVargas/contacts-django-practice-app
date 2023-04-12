const contactComponents = document.querySelectorAll(".contact");
const addButton = document.querySelector("#add-contact");

addButton.addEventListener("click", () => {
  document.querySelector("#new-contact").classList.toggle("visible")
});

contactComponents.forEach((component) => {
  const deleteCheckbox = component.querySelector(".delete-checkbox");
  
  component.querySelector(".btn-action").addEventListener("click", (event) => {
    event.preventDefault();
    if (component.classList.contains("save-mode")) {
      component.submit();
    }
    component.classList.toggle("save-mode");
  });

  if( deleteCheckbox ) {
    deleteCheckbox.addEventListener("change", () => {
      component.submit();
    });
  }
});