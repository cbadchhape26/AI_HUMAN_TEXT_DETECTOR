document.addEventListener("DOMContentLoaded", function () {

    // ── Button loading state ──
    const form   = document.getElementById("detector-form");
    const btn    = document.getElementById("submit-btn");
    const btnText = btn.querySelector(".btn-text");
    const btnIcon = btn.querySelector(".btn-icon");

    form.addEventListener("submit", function () {
        btnText.textContent = "Analysing...";
        btnIcon.textContent = "⟳";
        btnIcon.style.animation = "spin 0.8s linear infinite";
        btn.disabled = true;
    });

    // ── Character counter ──
    const textarea  = document.getElementById("text-input");
    const charCount = document.getElementById("char-count");

    function updateCount() {
        const n = textarea.value.length;
        const words = textarea.value.trim() === "" ? 0 : textarea.value.trim().split(/\s+/).length;
        charCount.textContent = `${n.toLocaleString()} chars · ${words} words`;
    }

    textarea.addEventListener("input", updateCount);
    updateCount(); // run on load in case text is pre-filled

    // ── Scroll to result if present ──
    const result = document.getElementById("result");
    if (result) {
        setTimeout(() => {
            result.scrollIntoView({ behavior: "smooth", block: "start" });
        }, 200);
    }

});

// spin keyframe via JS (avoids needing it in CSS)
const style = document.createElement("style");
style.textContent = `@keyframes spin { to { transform: rotate(360deg); } }`;
document.head.appendChild(style);