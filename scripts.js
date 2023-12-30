```javascript
// Establish connection with server
const socket = io.connect('http://localhost:5000');

// Get DOM elements
const scriptInput = document.getElementById('script-input');
const processScriptButton = document.getElementById('process-script');
const outlineContent = document.getElementById('outline-content');
const dialogueContent = document.getElementById('dialogue-content');
const standardizedContent = document.getElementById('standardized-content');
const feedbackContent = document.getElementById('feedback-content');
const collaborativeContent = document.getElementById('collaborative-content');

// Event listener for process script button
processScriptButton.addEventListener('click', () => {
    // Emit script input to server
    socket.emit('script_input', {
        script: scriptInput.value
    });
});

// Listen for script output from server
socket.on('script_output', (data) => {
    // Update DOM with processed script
    outlineContent.textContent = data.script_outline;
    dialogueContent.textContent = data.enhanced_dialogue;
    standardizedContent.textContent = data.standardized_script;
    feedbackContent.textContent = data.narrative_feedback;
    collaborativeContent.textContent = data.collaborative_script;
});
```
