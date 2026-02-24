# Reviewdle
Reviewdle is a game that challenges the player on their local business knowledge while also providing a fun and engaging experience. We hope that this game allows players to connect to their community and learn all that Madison has to offer.

This was built during madData 2026, Madison’s biggest data-focused hackathon, by [Wesley Erpelding](https://github.com/werpelding) and [Drew Barkman](https://github.com/drewbarkman). This meant the program was entirely built in 24 hours, which was a fun challenge for both of us.

## How does the game work? 
The game starts with players picking modes and areas of the city to be questioned on, and then the game gives them hints: one good review, one bad review, and a map of the business’s approximate location. If the player can guess correctly, they get points (based on how many hints they needed) and a streak! We hope this game successfully promotes local businesses and helps people realize how much good food and drink there is in Madison.

## What was it built on? 
The app pulls Google Maps’ reviews for local restaurants, bars, and cafes from their Places API, and then formats this data and censors reviews. The backend, built on Flask, randomly selects a place based on the player's choices of mode and area and creates the map, and the frontend handles the scoring and game mechanics.

## What’s next for Reviewdle?

- [ ] Improving scoring methods
- [ ] Improve censoring function
- [ ] Publish the game!
- [ ] Add instructions for launching the game
- [ ] Add a leaderboard
- [ ] Add other cities? 
- [ ] Let the server refresh the reviews itself