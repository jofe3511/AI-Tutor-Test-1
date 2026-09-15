const mastery = [
  ["Membrane Transport", 78],
  ["Osmosis", 84],
  ["Ion Channels", 64],
  ["ATPase Pumps", 52],
];

const questions = [
  {
    type: "Multiple select",
    prompt: "Which mechanisms can move molecules against a concentration gradient?",
    status: "High priority review",
  },
  {
    type: "Matching",
    prompt: "Match each transport type to its energy source and membrane protein.",
    status: "Ready",
  },
  {
    type: "Short answer",
    prompt: "Explain why a sodium-potassium pump helps maintain resting membrane potential.",
    status: "Needs rubric check",
  },
  {
    type: "Process ordering",
    prompt: "Order the ATPase cycle steps from ion binding through pump reset.",
    status: "Ready",
  },
  {
    type: "Multiple choice",
    prompt: "Which observation best distinguishes diffusion from facilitated diffusion?",
    status: "Ready",
  },
];

const masteryList = document.querySelector("#mastery-list");
const questionStack = document.querySelector("#question-stack");
const navItems = document.querySelectorAll(".nav-item");
const views = document.querySelectorAll(".view");
const title = document.querySelector("#view-title");
const feedback = document.querySelector("#feedback");

masteryList.innerHTML = mastery
  .map(
    ([label, score]) => `
      <div class="mastery-item">
        <div class="mastery-label"><strong>${label}</strong><span>${score}%</span></div>
        <div class="bar" aria-label="${label} mastery"><span style="width: ${score}%"></span></div>
      </div>
    `,
  )
  .join("");

questionStack.innerHTML = questions
  .map(
    (question, index) => `
      <article class="question-card">
        <div class="panel-header">
          <div>
            <p class="eyebrow">${question.type}</p>
            <h3>Question ${index + 1}</h3>
          </div>
          <span class="pill">${question.status}</span>
        </div>
        <p>${question.prompt}</p>
        <button class="secondary-action">Edit Question</button>
      </article>
    `,
  )
  .join("");

navItems.forEach((item) => {
  item.addEventListener("click", () => {
    const viewName = item.dataset.view;
    navItems.forEach((nav) => nav.classList.toggle("active", nav === item));
    views.forEach((view) => view.classList.toggle("active", view.id === viewName));
    title.textContent = item.textContent;
  });
});

document.querySelector("#grade-demo").addEventListener("click", () => {
  feedback.innerHTML =
    "<strong>Score: 2 / 3.</strong> Correct: primary active transport and secondary active transport. Review: facilitated diffusion uses proteins but does not move solutes against the gradient without coupled energy.";
});
