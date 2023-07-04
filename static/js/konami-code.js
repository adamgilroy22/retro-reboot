var pattern = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
var current = 0;
var modal = document.getElementById("konamiModal");
let closeButton = document.querySelector(".close-button");

var keyHandler = function (event) {

	// If the key isn't in the pattern, or isn't the current key in the pattern, reset
	if (pattern.indexOf(event.key) < 0 || event.key !== pattern[current]) {
		current = 0;
		return;
	}

	// Update how much of the pattern is complete
	current++;

	// If complete, alert and reset
	if (pattern.length === current) {
		modal.style.display = "block";
		current = 0;
	}

};

// Close modal on button click
closeButton.addEventListener("click", () => {
    modal.style.display = "none";
});

// Close modal when clicking outside it
window.addEventListener("click", (e) => {
    if (e.target == modal) {
        modal.style.display = "none";
    }
});

// Listen for keydown events
document.addEventListener('keydown', keyHandler, false);