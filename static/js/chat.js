document.addEventListener('DOMContentLoaded', () => {
  const chatContainer = document.querySelector('.space-y-4');
  if (chatContainer) {
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }

  const micBtn = document.getElementById('mic-btn');
  const messageBox = document.querySelector('textarea[name="message"]');

  if (micBtn && messageBox) {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    micBtn.addEventListener('click', () => {
      recognition.start();
      micBtn.innerText = '🎤 Listening...';
    });

    recognition.onresult = (event) => {
      const speech = event.results[0][0].transcript;
      messageBox.value = speech;
      micBtn.innerText = '🎤';
    };

    recognition.onerror = () => {
      micBtn.innerText = '🎤';
    };
  }
});