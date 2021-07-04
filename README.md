# Welcome to the Radio Free Playlist Project

## Goals
Pull curated playlists from various radio stations and convert them to YouTube music video playlists.

This is a pet project of mine to stay current. I plan to add features as it serves my interest and needs at [the day job](https://www.linkedin.com/in/bfdmurray).

## Roadmap
Initially here are my thoughts (subject to change):

1. [X] Basic containerized parser, in python to force myself to try something different from my perfect C# language (prove me wrong)
2. [X] Integration with the YouTube API to host the playlists
   1. [X] Setup Channel: [Radio Free Playlist](https://www.youtube.com/channel/UCCwqY9d3WjLjtAzwfgUbl6w)
   2. [X] Purchase Domain and Redirect: [http://www.radiofreeplaylist.com/](http://www.radiofreeplaylist.com/)
   3. [ ] File for YouTube API extension, 10000 goes fast 1t 50/playlist add
3. [ ] Deploy via GitHub Actions to Cloud
   1. [ ] Azure
   2. [ ] AWS
   3. [ ] GCP
4. [ ] Integrate another station (KEXP?) & Kappa based architecture
5. [ ] Consider Kafka topics as a message queue / data store for analytics
6. [ ] Create analytics engine / parsing capability
   1. [ ] Playlist for most viewed youtube based on station past X time window
   2. [ ] Consider other useful / interesting analytics
7. [ ] Convert to other languages
   1. [ ] C# (of course)
   2. [ ] Go (why not)
8. [ ] See where things go from there and how much time I have to putz with this

If you have read all of the above and have questions / suggestions email [radiofreeplaylist@gmail.com](mailto:radiofreeplaylist@gmail.com)
