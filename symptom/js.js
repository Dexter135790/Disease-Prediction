const input1 = document.getElementById('input1');
const input2 = document.getElementById('input2');
const output = document.getElementById('output');

input1.addEventListener('input', updateOutput);
input2.addEventListener('input', updateOutput);

function updateOutput() {
  const selectedValues = [];

  if (input1.value !== '') {
    selectedValues.push(input1.value);
  }

  if (input2.value !== '') {
    selectedValues.push(input2.value);
  }

  output.value = selectedValues.join(', ');
}
