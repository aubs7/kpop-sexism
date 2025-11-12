const scanBtn = document.getElementById("scanBtn");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const progressBar = document.getElementById("progressBar");

scanBtn.addEventListener("click", () => {
  scanBtn.style.display = "none";
  loading.style.display = "block";

  const url = document.getElementById("websiteInput").value;

  // Fake loading animation
  progressBar.style.width = "20%";
  setTimeout(() => (progressBar.style.width = "60%"), 500);
  setTimeout(() => (progressBar.style.width = "100%"), 1000);

  fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url: url }),
  })
    .then((res) => res.json())
    .then((data) => {
      result.innerHTML = ""; // Clear previous results

      if (Array.isArray(data) && data.length > 0) {
        data.forEach((item, index) => {
          const entry = document.createElement("div");
          const labelClass =
            item.label === "Sexist" ? "label-sexist" : "label-not-sexist";

          entry.style.marginBottom = "20px";
          entry.innerHTML = `
            <div><strong>Text ${index + 1}</strong></div>
            <div class="text-placeholder">${item.text}</div>
            <div class="result-text ${labelClass}">
              ${item.label} (${(item.probability * 100).toFixed(2)}%)
            </div>
            <hr />
          `;
          result.appendChild(entry);
        });
      } else {
        result.innerHTML = "<div>No results returned.</div>";
      }

      loading.style.display = "none";
      result.style.display = "block";
      scanBtn.style.display = "block";
    })
    .catch((error) => {
      result.innerHTML = `<div class="text-placeholder">Error: ${error.message}</div>`;
      loading.style.display = "none";
      result.style.display = "block";
      scanBtn.style.display = "block";
      console.error("Error:", error);
    });
});