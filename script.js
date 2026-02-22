function requestHint() {
    console.log(hint2box.classList);
    if (hint2box.classList.contains("inactive")) {
        hint2box.classList.remove("inactive");
        potentialRoundScore -= 1;
    } else if (hint3box.classList.contains("inactive")) {
        hint3box.classList.remove("inactive");
        request_hint_button.classList.add("inactive");
        potentialRoundScore -= 1;
    }
}

const game_container = document.querySelector('#game');
const hint1box = document.querySelector('#hint1box');
const hint2box = document.querySelector('#hint2box');
const hint3box = document.querySelector('#hint3box');
const request_hint_button = document.querySelector('#another-hint');
const form = document.querySelector('#start-game-form');
const hint1 = document.querySelector('#hint1')
const hint2 = document.querySelector('#hint2')
const hint3 = document.querySelector('#hint3')
const result_pop_up = document.querySelector('.result')
const correct_answer = document.querySelector('#correct-answer')
const score = document.querySelector('.score')
const streak = document.querySelector('.streak')
const score_report = document.querySelector('.core-report')
let potentialRoundScore = 3;


const start_button = document.querySelector('#start-game');

const game_intro = document.querySelector('#intro');

const answer_buttons = document.querySelectorAll('.answer-option');


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
        loadData(data);
    } catch (err) {
        console.error('Failed to send form data', err);
    }

    game_intro.remove();
    game_container.classList.toggle('inactive');
});

request_hint_button.addEventListener('click', () => {
    requestHint()
});

const mapHolder = document.querySelector(".image-space");
const map = document.createElement('img');

function loadData(data) {
    // load options
    all_options = data['options'].concat(data['answer'])
    index_array = [0, 1, 2, 3, 4]
    shuffle(index_array)
    for (let i = 0; i < 5; i++) {
            random = index_array[i]
            answer_buttons[random].textContent = all_options[i]
                if (answer_buttons[random].textContent == data['answer']) {
                    answer_buttons[random].classList.add('correct');
            } else {
                answer_buttons[random].classList.add('wrong');
            }
        }
    hint1.textContent = data['positive_text'];
    hint2.textContent = data['negative_text'];

    answer_buttons.forEach((button) => {
        button.addEventListener('click', (e) => {
            const btn = e.currentTarget;
            if (btn.classList.contains('wrong')) {
                streak.textContent = 0
                result_message.classList.remove('inactive');
                result_message.textContent = `Incorrect, the correct answer was ${data['answer']}`
                result_pop_up.classList.remove('inactive');
            } else if (btn.classList.contains('correct')) {
                streak.textContent = parseInt(streak.textContent) + 1
                score.textContent = parseInt(score.textContent) + potentialRoundScore
                result_message.textContent = "Correct!"
                result_pop_up.classList.remove('inactive');
            }
            game_container.classList.add('inactive')
        });
    });

    map.src = 'map.svg'
    mapHolder.appendChild(map);

    const url = document.querySelector('#google_url');
    url.href = data['url'];

    const hint1stars = document.querySelector('#hint1stars');
    hint1stars.textContent = '*'.repeat(data['positive_rating']);

    const hint2stars = document.querySelector('#hint2stars');
    hint2stars.textContent = '*'.repeat(data['negative_rating']);

    }

const result_message = document.querySelector('#winning-message')
const result_correct = document.querySelector('#correct')


    // mark which one is the answer
    // load hint one



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

// loadData(data);
let index_array = [0, 1, 2, 3, 4];
shuffle(index_array);


// loadData(data);