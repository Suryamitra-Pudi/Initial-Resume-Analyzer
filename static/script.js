const roleInput = document.getElementById("role");
const jobDesc = document.getElementById("job_desc");

roleInput.addEventListener("input", () => {
  let role = roleInput.value.trim();

  if (role.length > 2 && jobDesc.value === "") {
    jobDesc.value = `We are looking for candidates for the role of ${role}. The candidate should have strong skills in Python, SQL, Machine Learning, Data Analysis, and good communication skills. Experience with tools like TensorFlow and cloud platforms is a plus.`;
  }
});