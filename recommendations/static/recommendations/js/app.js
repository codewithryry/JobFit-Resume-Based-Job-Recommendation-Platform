const signUpBtn = document.getElementById("sign-up-btn");
const signInBtn = document.getElementById("sign-in-btn");
const signInForm = document.querySelector(".sign-in-form");
const signUpForm = document.querySelector(".sign-up-form");
const container = document.querySelector(".container");

signUpBtn.addEventListener("click", () => {
  signInForm.style.display = "none";
  signUpForm.style.display = "block";
  container.classList.add("sign-up-mode");
});

signInBtn.addEventListener("click", () => {
  signUpForm.style.display = "none";
  signInForm.style.display = "block";
  container.classList.remove("sign-up-mode");
});
