const mastery = [
  ["Glycolysis", 82, "Strong"],
  ["Krebs Cycle", 61, "Developing"],
  ["Electron Transport", 43, "Needs practice"],
  ["ATP Production", 52, "Needs support"],
  ["Membrane Gradients", 73, "Ready"],
];

const questions = [
  {
    type: "Multiple select",
    difficulty: "0.58",
    bloom: "Application",
    objective: "Explain how NADH supports ATP production",
    source: "Lecture 8, slide 24",
    status: "Needs professor approval",
  },
  {
    type: "Matching",
    difficulty: "0.50",
    bloom: "Understand",
    objective: "Connect transport-chain proteins to electron movement",
    source: "Chapter 6 notes",
    status: "Ready",
  },
  {
    type: "Short answer",
    difficulty: "0.64",
    bloom: "Analyze",
    objective: "Distinguish proton pumping from ATP synthesis",
    source: "Lab 3 + Lecture 8",
    status: "Rubric review",
  },
  {
    type: "Process ordering",
    difficulty: "0.45",
    bloom: "Apply",
    objective: "Order ETC events from NADH donation to ATP synthase",
    source: "Lecture diagram",
    status: "Ready",
  },
  {
    type: "Multiple choice",
    difficulty: "0.36",
    bloom: "Remember",
    objective: "Identify the role of oxygen in electron transport",
    source: "Professor summary",
    status: "Ready",
  },
];

const interfaces = [
  ["AIModelProvider", "generate_explanation, generate_question, evaluate_answer"],
  ["KnowledgeRetriever", "search course chunks, return citations, rank authority tiers"],
  ["MasteryStrategy", "compute mastery and confidence from attempts"],
  ["DifficultyPolicy", "raise, lower, or hold difficulty from performance"],
  ["TeachingStrategy", "socratic, worked example, hints, analogy, misconception correction"],
  ["ScheduleEngine", "M/W, M/W/F, T/Th, and custom calendars from config"],
  ["QuestionGenerator", "weighted question mix with objective and Bloom metadata"],
  ["DocumentParser", "PDF, PPTX, DOCX, TXT, Markdown extraction"],
];

const entities = [
  "User",
  "Course",
  "Enrollment",
  "Module",
  "Topic",
  "Concept",
  "LearningObjective",
  "Document",
  "DocumentChunk",
  "Question",
  "QuestionVersion",
  "QuestionAttempt",
  "Assessment",
  "AssessmentAttempt",
  "MasteryState",
  "TutorSession",
  "StudentQuestion",
  "InstructorFeedback",
  "AIConfiguration",
  "AIOutput",
  "EvaluationResult",
  "CourseSession",
];

const masteryList = document.querySelector("#mastery-list");
const questionStack = document.querySelector("#question-stack");
const interfaceGrid = document.querySelector("#interface-grid");
const entityGrid = document.querySelector("#entity-grid");
const navItems = document.querySelectorAll(".nav-item");
const views = document.querySelectorAll(".view");
const title = document.querySelector("#view-title");
const feedback = document.querySelector("#feedback");

masteryList.innerHTML = mastery
  .map(
    ([label, score, state]) => `
      <div class="mastery-item">
        <div class="mastery-label">
          <strong>${label}</strong>
          <span>${score}% - ${state}</span>
        </div>
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
        <p><strong>${question.objective}</strong></p>
        <dl class="question-meta">
          <div><dt>Difficulty</dt><dd>${question.difficulty}</dd></div>
          <div><dt>Bloom</dt><dd>${question.bloom}</dd></div>
          <div><dt>Source</dt><dd>${question.source}</dd></div>
        </dl>
        <button class="secondary-action">Edit Before Release</button>
      </article>
    `,
  )
  .join("");

interfaceGrid.innerHTML = interfaces
  .map(
    ([name, detail]) => `
      <div>
        <strong>${name}</strong>
        <span>${detail}</span>
      </div>
    `,
  )
  .join("");

entityGrid.innerHTML = entities.map((entity) => `<span>${entity}</span>`).join("");

navItems.forEach((item) => {
  item.addEventListener("click", () => {
    const viewName = item.dataset.view;
    navItems.forEach((nav) => nav.classList.toggle("active", nav === item));
    views.forEach((view) => view.classList.toggle("active", view.id === viewName));
    title.textContent = item.textContent;
  });
});

document.querySelector("#grade-demo").addEventListener("click", () => {
  feedback.innerHTML = `
    <strong>Decision complete.</strong>
    Retrieved Tier 1 lecture chunks, selected hint progression, generated a short-answer prompt at difficulty 0.46, logged the attempt, and updated Electron Transport mastery from 43% to 47% with low confidence.
  `;
});
