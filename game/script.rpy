﻿

define Jess = Character("Jessica")
define Jamal = Character("Jamal")


image jessica happy = im.Flip("jessica happy.png", horizontal=True)
image jessica sad = im.Flip("jessica sad.png", horizontal=True)
define audio.jazz = "audio/jazz.mp3"

label start:

    scene nyc horizon with fade
    play music jazz loop
    show jessica happy at left with moveinleft
    Jess "I can't belive we are in New York City!"
    Jess "Are you seeing all of this?"
    show jessica sad at left with fade
    Jess "Jamal? Where are you?"
    show jamal happy at right with moveinright
    Jamal "Here I am. Just soaking it all in."
    show jessica happy at left with moveinleft
    Jess "Ok good. What should we do first?"

    # add menu of options
    menu:
        "Go to the music store":
            jump store
        "Perform locally":
            jump local_gigs
        "Go on a US Tour":
            jump us_tour
        "Go on an International Tour":
            jump international_tour

    label store:
        scene music store with fade
        show jamal happy at right
        show jessica happy at left
        Jamal "What should be buy today?"
        jump home

    label local_gigs:
        show jamal happy at right with moveinright
        Jamal "This is the local gigs page"
        jump home

    label us_tour:
        show jamal happy at right with moveinright
        Jamal "We are on the US tour"
        jump home

    label international_tour:
        show jessica happy at left with moveinleft
        Jess "We are on the international tour"
        jump home

    label home:
        "This is home"

    return