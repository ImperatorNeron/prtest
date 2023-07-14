const zero_button = document.querySelector('.zero-button');
zero_button.onclick = moveButtons;

let buttonsMoved = false; // Variable indicating whether the buttons have been moved

function moveButtons() {
  let firstButton = document.querySelector('.first-button');
  let secondButton = document.querySelector('.second-button');
  let firstButtonImg1 = document.querySelector('.zero-button-img-1');
  let firstButtonImg2 = document.querySelector('.zero-button-img-2');

  if (!buttonsMoved) {
    // Move the buttons to new positions
    firstButton.style.display = "flex";
    secondButton.style.display = "flex";
    firstButton.style.bottom = '85px';
    secondButton.style.bottom = '150px';
    buttonsMoved = true; // Set the flag indicating that the buttons have been moved
    firstButtonImg1.classList.add('no-active');
    firstButtonImg2.classList.remove('no-active');
    zero_button.classList.remove('pulse');
  } else {
    // Move the buttons back to the original positions
    firstButton.style.display = "none";
    secondButton.style.display = "none";
    firstButton.style.bottom = '20px';
    secondButton.style.bottom = '20px';
    buttonsMoved = false; // Reset the flag indicating the buttons' movement
    firstButtonImg1.classList.remove('no-active');
    firstButtonImg2.classList.add('no-active');
    zero_button.classList.add('pulse');
  }
}
