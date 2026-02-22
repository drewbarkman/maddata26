function requestHint() {
    console.log(hint2box.classList);
    if (hint2box.classList.contains("inactive")) {
        hint2box.classList.remove("inactive");
    } else if (hint3box.classList.contains("inactive")) {
        hint3box.classList.remove("inactive");
        request_hint_button.classList.add("inactive");
    }
    console.log("complete")
}

// function winRound() {
//     toggle win h2
// }

const arrayRange = (start, stop, step) =>
    Array.from(
    { length: (stop - start) / step + 1 },
    (value, index) => start + index * step
    );

console.log(arrayRange(1, 5, 1)); // [1,2,3,4,5]

const game_container = document.querySelector('#game');
const hint1box = document.querySelector('#hint1box');
const hint2box = document.querySelector('#hint2box');
const hint3box = document.querySelector('#hint3box');
const request_hint_button = document.querySelector('#another-hint');
const form = document.querySelector('#start-game-form');

const start_button = document.querySelector('#start-game');

const game_intro = document.querySelector('#intro');

// start_button.addEventListener("click", () => {
//     game_intro.remove();
//     game_container.classList.toggle('inactive');
// });

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    try {
        const res = await fetch('/data', {
            method: 'POST',
            body: formData
        });
        const data = await res.json();
        console.log('server response', data);
    } catch (err) {
        console.error('Failed to send form data', err);
    }

    game_intro.remove();
    game_container.classList.toggle('inactive');
});

request_hint_button.addEventListener('click', () => {
    console.log('hi');
    requestHint()
});

const fakeData = {
    'options': ['Colectivo', 'Taco Bell Cantina', 'Papa Johns', "Mooyah"],
    'answer': 'Starbucks'
}

function loadData(data) {
    // load options
    secret = Math.floor(Math.random() * 5)
    console.log(secret)
    answer_hidden = fakeData['options'].concat(fakeData['answer'])

    // load hint one
}

const hint1 = document.querySelector('#hint1')
// hint1.text = x

// from stackoverflow!
function shuffle(array) {
  let currentIndex = array.length;

  while (currentIndex != 0) {

    let randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex], array[currentIndex]];
  }
}

let index_array = [0, 1, 2, 3, 4];
shuffle(index_array);

const answer_buttons = document.querySelectorAll('.answer-option');

index_array.forEach((i) => {
    answer_buttons[i].textContent = answer_hidden[i]
})