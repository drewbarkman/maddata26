function requestHint() {
    console.log(hint2.classList);
    if (hint2.classList.contains("inactive")) {
        hint2.classList.remove("inactive");
    } else if (hint3.classList.contains("inactive")) {
        hint3.classList.remove("inactive");
        request_hint_button.classList.add("inactive");
    }
    console.log("complete")
}

// function winRound() {
//     toggle win h2
// }

const game_container = document.querySelector('#game');
const hint1 = document.querySelector('#hint1');
const hint2 = document.querySelector('#hint2');
const hint3 = document.querySelector('#hint3');
const request_hint_button = document.querySelector('#another-hint');
const form = document.querySelector('#start-game-form');

const start_button = document.querySelector('#start-game');

const game_intro = document.querySelector('#intro');

start_button.addEventListener("click", () => {
    game_intro.remove();
    game_container.classList.toggle('inactive');
});

form.addEventListener('submit', async (event) => {
  event.preventDefault();
});

request_hint_button.addEventListener('click', () => {
    console.log('hi');
    requestHint()
});