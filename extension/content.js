// Shopping Footprint - Carbon Emission Display

function addCarbonEmission() {
  // Find Amazon product price elements
  const prices = document.querySelectorAll(".a-price");

  prices.forEach((price) => {
    // Avoid adding the emission more than once
    if (price.parentElement.querySelector(".carbon-footprint")) {
      return;
    }

    // Create carbon emission display
    const emission = document.createElement("div");
    emission.className = "carbon-footprint";

    emission.innerHTML = "🌱 Carbon: <b>4.2 kg CO₂e</b>";

    // Styling
    emission.style.fontSize = "14px";
    emission.style.color = "#16803c";
    emission.style.marginTop = "5px";
    emission.style.fontWeight = "500";

    // Add below the price
    price.parentElement.appendChild(emission);
  });
}

// Run when page loads
addCarbonEmission();

// Detect products loaded dynamically
const observer = new MutationObserver(() => {
  addCarbonEmission();
});

observer.observe(document.body, {
  childList: true,
  subtree: true
});