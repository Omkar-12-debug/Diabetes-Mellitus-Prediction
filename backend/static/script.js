// Dark Mode Toggle
const darkToggle = document.getElementById('darkToggle');
const html = document.documentElement;

// Check for saved theme preference
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
  html.setAttribute('data-theme', currentTheme);
  
  // Update button text based on theme
  if (currentTheme === 'dark') {
    darkToggle.textContent = '☀️ Toggle Light Mode';
  } else {
    darkToggle.textContent = '🌙 Toggle Dark Mode';
  }
}

// Form validation
document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  if (form) {
    form.addEventListener('submit', function(e) {
      let isValid = true;
      
      // Validate all required inputs
      const inputs = form.querySelectorAll('input[required], select[required]');
      inputs.forEach(input => {
        if (!input.value) {
          isValid = false;
          input.style.borderColor = 'red';
        } else {
          input.style.borderColor = '';
        }
      });
      
      // Additional validation for number inputs
      const numberInputs = form.querySelectorAll('input[type="number"]');
      numberInputs.forEach(input => {
        const min = parseFloat(input.min) || -Infinity;
        const max = parseFloat(input.max) || Infinity;
        const value = parseFloat(input.value);
        
        if (isNaN(value) || value < min || value > max) {
          isValid = false;
          input.style.borderColor = 'red';
        }
      });
      
      if (!isValid) {
        e.preventDefault();
        alert('Please fill in all fields with valid values.');
      }
    });
  }
});