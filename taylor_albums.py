import streamlit as st
import os
import pandas as pd

def taylor_main(era_name, surprise_song):
  st.title(f"All About _{era_name}_")
  st.header("Basic Information:")
  if era_name == "reputation":
    st.write(f"_{era_name}_ is Taylor Swift's sixth studio album, released in a tumultuous time of her career, hence the title.")
    st.write("The album is of the electro-pop and contemporary R&B genre that completely redefined Swift's brand as an artist.")
    st.write("It has 15 tracks and was as big as any of Swift's other releases commercially. It sold 2 million copies globally within the first week.")
    st.write(f"Although its reception upon release was not at all negative, _{era_name}_ has stood the test of time as one of Swift's most endurings albums, gaining more of a fanbase years after its release than before.")
    st.image("Images/reputation.png", width=200)
    st.write("---")
    st.header("Guess how the singles from this album performed on the Billboard Hot 100!")
    # NEW
    if st.slider("Look What You Made Me Do") == 1:
      st.write("Correct! This single peaked at #1.")
    if st.slider("...Ready For It?") == 4:
      st.write("Correct! This single peaked at #4.")
    if st.slider("Endgame") == 20:
      st.write("Correct! This single peaked at #20.")
    if st.slider("Delicate") == 12:
      st.write("Correct! This single peaked at #12.")
    
    st.header("Tracklist and Guess the Show Game")
    tab1, tab2 = st.tabs(["Tracklist", "Guess the Song"])
    with tab1:
      # NEW
      col1, col2 = st.columns(2)
      col1.write(f"Here is the _{era_name}_ tracklist:")
      col2.write("Guess which song is my favorite!")
      with col1:
        tracklist = pd.DataFrame(reputation_data)
        st.dataframe(tracklist, column_config={
          "tracks": "Tracks",
          "runtime": "Track Runtime"},
          hide_index = True,
        )
      with col2:
        answer = st.text_input("Enter your answer here.")
        if answer != "Dress":
          st.write("Guess again!")
        else:
          st.write("Correct!")
    with tab2:
      st.subheader(f"Guess which show _{surprise_song}_ was performed at as a surprise song!")
      # NEW
      choices = st.radio("Choose:", ["Seattle Night 1", "East Rutherford Night 1", "Los Angeles Night 4", "Buenos Aires Night Night 1"])
      if choices != "Los Angeles Night 4":
        st.write("Guess again!")
      else:
        st.write("Correct!")
  elif era_name == "evermore":
    st.write(f"_{era_name}_ is Taylor Swift's ninth studio album, her second to be released in 2020.")
    st.write("It's a sister album of its predecessor _folklore_, and it continues Swift's dip into the folk/indie genre.")
    st.write(f"It has 15 tracks and its bonus version include the bonus songs 'right where you left me' and 'it's time to go'. _{era_name}_ sold 1 million copies globally in its first week.")
    st.write(f"Despite its masterful songwriting and eloquent product, fans (myself included) assert that _{era_name}_ was not given its due flowers like its sibling, _folklore_.")
    st.image("Images/evermore.png", width=200)
    st.write("---")
    st.header("Guess how the single from this album performed on the Billboard Hot 100!")
    # NEW
    if st.slider("willow") == 1:
      st.write("Correct! This single peaked at #1.")
    
    st.header("Tracklist and Guess the Show Game")
    tab1, tab2 = st.tabs(["Tracklist", "Guess the Song"])
    with tab1:
      # NEW
      col1, col2 = st.columns(2)
      col1.write(f"Here is the _{era_name}_ tracklist:")
      col2.write("Guess which song is my favorite!")
      with col1:
        tracklist = pd.DataFrame(evermore_data)
        st.dataframe(tracklist, column_config={
          "tracks": "Tracks",
          "runtime": "Track Runtime"},
          hide_index = True,
        )
      with col2:
        answer = st.text_input("Enter your answer here.")
        if answer != "marjorie":
          st.write("Guess again!")
        else:
          st.write("Correct!")
    with tab2:
      st.subheader(f"Guess which show _{surprise_song}_ was performed at as a surprise song!")
      # NEW
      choices = st.radio("Choose:", ["Houston Night 3", "Seattle Night 2", "Cincinatti Night 2", "Philadelphia Night 1"])
      if choices != "Philadelphia Night 1":
        st.write("Guess again!")
      else:
        st.write("Correct!")
  elif era_name == "Lover":
    st.write(f"_{era_name}_ is Taylor Swift's seventh studio album, released in 2019.")
    st.write("It's her first after switching labels from Big Machine Records to Republic Records, following outrage and her personal statement over her lack of ownership of her previous masters.")
    st.write(f"It has 18 tracks, five of which are singles, and is of the pop genre. _{era_name}_ sold 3 million copies globally in its first week.")
    st.write(f"_{era_name}_ is a standout in Swift's discography not only because of its traditional album elements, but also because of its longevity. It has endured as one of her most personal and relatable albums, and a fan-favorite song from it - Cruel Summer - was released as a radio single this year, four years after the album's release.")
    st.image("Images/lover.png", width=200)
    st.write("---")
    st.header("Guess how the singles from this album performed on the Billboard Hot 100!")
    # NEW
    if st.slider("ME!") == 2:
      st.write("Correct! This single peaked at #2.")
    if st.slider("You Need To Calm Down") == 2:
      st.write("Correct! This single peaked at #2.")
    if st.slider("Lover") == 10:
      st.write("Correct! This single peaked at #10.")
    if st.slider("The Man") == 23:
      st.write("Correct! This single peaked at #23.")
    if st.slider("Cruel Summer") == 1:
      st.write("Correct! This single peaked at #1.")
    
    st.header("Tracklist and Guess the Show Game")
    tab1, tab2 = st.tabs(["Tracklist", "Guess the Song"])
    with tab1:
      # NEW
      col1, col2 = st.columns(2)
      col1.write(f"Here is the _{era_name}_ tracklist:")
      col2.write("Guess which song is my favorite!")
      with col1:
        tracklist = pd.DataFrame(lover_data)
        st.dataframe(tracklist, column_config={
          "tracks": "Tracks",
          "runtime": "Track Runtime"},
          hide_index = True,
        )
      with col2:
        answer = st.text_input("Enter your answer here.")
        if answer != "False God":
          st.write("Guess again!")
        else:
          st.write("Correct!")
    with tab2:
      st.subheader(f"Guess which show _{surprise_song}_ was performed at as a surprise song!")
      # NEW
      choices = st.radio("Choose:", ["Buenos Aires Night 2", "Mexico City Night 4", "Los Angeles Night 3", "Glendale Night 1"])
      if choices != "Mexico City Night 4":
        st.write("Guess again!")
      else:
        st.write("Correct!")
  elif era_name == "folklore":
    st.write(f"_{era_name}_ is Taylor Swift's eighth studio album, the first of two sister albums to be released in 2020.")
    st.write(f"Unlike her previous lengthy album campaigns, _{era_name}_ was a surprise album that was announced the day it dropped, a complete curveball by Swift.")
    st.write(f"It has 16 tracks, one of which is a single, and has the bonus track 'the lakes' on its deluxe version. This was Swift's first foray into the folk/indie genre. _{era_name}_ sold 2 million copies globally in its first week.")
    st.write(f"_{era_name}_ is widely regarded by critics and fans alike as one of Swift's best. Swift did something she had never done before on this album: creating fictional stories to tell through songs. _{era_name}_ won Album of the Year at the 2021 Grammy Awards.")
    st.image("Images/folklore.png", width=200)
    st.write("---")
    st.header("Guess how the single from this album performed on the Billboard Hot 100!")
    # NEW
    if st.slider("cardigan") == 1:
      st.write("Correct! This single peaked at #1.")
    
    st.header("Tracklist and Guess the Show Game")
    tab1, tab2 = st.tabs(["Tracklist", "Guess the Song"])
    with tab1:
      col1, col2 = st.columns(2)
      col1.write(f"Here is the _{era_name}_ tracklist:")
      col2.write("Guess which song is my favorite!")
      with col1:
        tracklist = pd.DataFrame(folklore_data)
        st.dataframe(tracklist, column_config={
          "tracks": "Tracks",
          "runtime": "Track Runtime"},
          hide_index = True,
        )
      with col2:
        answer = st.text_input("Enter your answer here.")
        if answer != "the last great american dynasty":
          st.write("Guess again!")
        else:
          st.write("Correct!")
    with tab2:
      st.subheader(f"Guess which show _{surprise_song}_ was performed at as a surprise song!")
      # NEW
      choices = st.radio("Choose:", ["Foxborough Night 1", "Arlington Night 2", "Las Vegas Night 1", "Tampa Night 3"])
      if choices != "Tampa Night 3":
        st.write("Guess again!")
      else:
        st.write("Correct!")

st.sidebar.title("Era")
era_choice = st.sidebar.radio("Select an era to learn about:", ["reputation", "evermore", "Lover", "folklore"])

if era_choice == "reputation":
  reputation_data = {"tracks": ["...Ready For It?", "Endgame", "I Did Something Bad", "Don't Blame Me", "Delicate", "Look What You Made Me Do", "...So It Goes", "Gorgeous", "Getaway Car", "King of My Heart", "Dancing With Our Hands Tied", "Dress", "This is Why We Can't Have Nice Things", "Call It What You Want", "New Year's Day"],
                                                   "runtime": ["3:28", "4:04", "3:58", "3:56", "3:52", "3:31", "3:47", "3:29", "3:53", "3:34", "3:31", "3:50", "3:27", "3:23", "3:55"]}
  taylor_main("reputation", "Dress")
elif era_choice == "evermore":
  evermore_data = {"tracks": ["willow", "champagne problems", "gold rush", "'tis the damn season", "tolerate it", "no body, no crime", "happiness", "dorothea", "coney island", "ivy", "cowboy like me", "long story short", "marjorie", "closure", "evermore"], 
                   "runtime": ["3:34", "4:04", "3:05", "3:49", "4:05", "3:35", "5:15", "3:45", "4:35", "4:20", "4:35", "3:35", "4:17", "3:00", "5:04"]}
  taylor_main("evermore", "gold rush")
elif era_choice == "Lover":
  lover_data = {"tracks": ["I Forgot That You Existed", "Cruel Summer", "Lover", "The Man", "The Archer", "I Think He Knows", "Miss Americana & The Heartbreak Prince", "Paper Rings", "Cornelia Street", "Death By A Thousand Cuts", "London Boy", "Soon You'll Get Better", "False God", "You Need To Calm Down", "Afterglow", "ME!", "It's Nice To Have A Friend", "Daylight"], 
                "runtime": ["2:50", "2:58", "3:41", "3:10", "3:31", "2:53", "3:54", "3:42", "4:47", "3:18", "3:10", "3:21", "3:20", "2:51", "3:43", "3:13", "2:30", "4:53"]}
  taylor_main("Lover", "Afterglow")
elif era_choice == "folklore":
  folklore_data = {"tracks": ["the 1", "cardigan", "the last great american dynasty", "exile", "my tears ricochet", "mirrorball", "seven", "august", "this is me trying", "illicit affairs", "invisible string", "mad woman", "epiphany", "betty", "peace", "hoax"], 
                   "runtime": ["3:30", "3:59", "3:50", "4:45", "4:15", "3:28", "3:28", "4:21", "3:15", "3:10", "4:12", "3:57", "4:49", "4:54", "3:54", "3:40"]}
  taylor_main("folklore", "folklore_data")