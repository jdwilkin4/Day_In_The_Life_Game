

define Jess = Character("Jessica")
define Jamal = Character("Jamal")
define gui.choice_button_text_idle_color = '#000000'


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
        "Music store":
            jump store
        "NYC Tour":
            jump local_gigs
        "US Tour":
            jump us_tour
        "International Tour":
            jump international_tour

    label store:
        scene music store with fade
        show jamal happy at right
        show jessica happy at left
        Jamal "What should we buy today?"
        jump home

    label local_gigs:
        show jamal happy at right with moveinright
        Jamal "This is the local gigs page"
        jump home

    label us_tour:
        scene airport with fade
        show jessica happy at left with moveinleft
        show jamal happy at right with moveinright
        Jamal "Where are we going again?"

        menu:
            "Los Angeles":
                jump la
            "Houston":
                jump houston
            "Chicago":
                jump chicago
            "Boston":
                jump boston

    label la:
        scene hollywood sign with fade
        show jessica happy at left with moveinleft
        Jess "We finally made it to LA!"
        show jamal happy at right with moveinright
        Jamal "This looks great! What should we do first?"
        menu:
            "Go to hotel":
                jump la_hotel
            "Head to gig":
                jump la_gigs
            "Sight see":
                jump sight_see_la
            "Network at jazz concert":
                jump network_la
        jump home

    label la_hotel:
        scene la hotel with fade
        show jamal happy at right
        show jessica happy at left
        Jamal "Let's get some rest"
        Jess "Good night Jamal!"
        Jamal "Good night Jess!"
        jump home


    label houston:
        show jamal happy at right
        show jessica happy at left

    label chicago:
        show jamal happy at right
        show jessica happy at left

    label boston:
        show jamal happy at right
        show jessica happy at left

    label international_tour:
        show jessica happy at left with moveinleft
        Jess "We are on the international tour"
        jump home

    label home:
        "This is home"

    return
