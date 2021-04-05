import random


def roll(upto):
    return random.randint(1, upto)


def clothes(roll1):
    if roll1 == 1:
        return "Clothes: Bike leathers"
    elif roll1 == 2:
        return "Clothes: Blue jeans"
    elif roll1 == 3:
        return "Clothes: Corporate suits"
    elif roll1 == 4:
        return "Clothes: Jumpsuits"
    elif roll1 == 5:
        return "Clothes: Miniskirts"
    elif roll1 == 6:
        return "Clothes: High Fashion"
    elif roll1 == 7:
        return "Clothes: Cammos"
    elif roll1 == 8:
        return "Clothes: Normal clothes"
    elif roll1 == 9:
        return "Clothes: Nude"
    elif roll1 == 10:
        return "Clothes: Bag Lady Chic"


def hairstyle(roll2):
    if roll2 == 1:
        return "Hairstyle: Mohawk"
    elif roll2 == 2:
        return "Hairstyle: Long & Ratty"
    elif roll2 == 3:
        return "Hairstyle: Short & Spiked"
    elif roll2 == 4:
        return "Hairstyle: Wild & all over"
    elif roll2 == 5:
        return "Hairstyle: Bald"
    elif roll2 == 6:
        return "Hairstyle: Striped"
    elif roll2 == 7:
        return "Hairstyle: Tinted"
    elif roll2 == 8:
        return "Hairstyle: Neat, short"
    elif roll2 == 9:
        return "Hairstyle: Short, curly"
    elif roll2 == 10:
        return "Hairstyle: Long, straight"


def affectations(roll3):
    if roll3 == 1:
        return "Affectations: Tattoos"
    elif roll3 == 2:
        return "Affectations: Mirrorshades"
    elif roll3 == 3:
        return "Affectations: Ritual Scars"
    elif roll3 == 4:
        return "Affectations: Spiked gloves"
    elif roll3 == 5:
        return "Affectations: Nose Rings"
    elif roll3 == 6:
        return "Affectations: Earrings"
    elif roll3 == 7:
        return "Affectations: Long fingernails"
    elif roll3 == 8:
        return "Affectations: Spike heeled boots"
    elif roll3 == 9:
        return "Affectations: Weird Contact Lenses"
    elif roll3 == 10:
        return "Affectations: Fingerless gloves"


def ethnic(roll4):
    if roll4 == 1:
        return "Ethnic group: Anglo-American"
    elif roll4 == 2:
        return "Ethnic group: African"
    elif roll4 == 3:
        return "Ethnic group: Japanese/Korean"
    elif roll4 == 4:
        return "Ethnic group: Central European/Soviet"
    elif roll4 == 5:
        return "Ethnic group: Pacific Islander"
    elif roll4 == 6:
        return "Ethnic group: Chinese/Southeast Asian"
    elif roll4 == 7:
        return "Ethnic group: Black American"
    elif roll4 == 8:
        return "Ethnic group: Hispanic American"
    elif roll4 == 9:
        return "Ethnic group: Central/South American"
    elif roll4 == 10:
        return "Ethnic group: European"


def family_rank(roll5):
    if roll5 == 1:
        return "Family rank: Corporate Executive"
    elif roll5 == 2:
        return "Family rank: Corporate Manager"
    elif roll5 == 3:
        return "Family rank: Corporate Technician"
    elif roll5 == 4:
        return "Family rank: Nomad Pack"
    elif roll5 == 5:
        return "Family rank: Pirate Fleet"
    elif roll5 == 6:
        return "Family rank: Gang Family"
    elif roll5 == 7:
        return "Family rank: Crime Lord"
    elif roll5 == 8:
        return "Family rank: Combat Zone Poor"
    elif roll5 == 9:
        return "Family rank: Urban homeless"
    elif roll5 == 10:
        return "Family rank: Arcology family"


def parents(roll6):
    def something_happened(roll7):
        if roll7 == 1:
            return (
                "Something has happened to your parents: Your parent(s) died in warfare"
            )
        elif roll7 == 2:
            return "Something has happened to your parents: Your parent(s) died in an accident"
        elif roll7 == 3:
            return (
                "Something has happened to your parents: Your parent(s) were murdered"
            )
        elif roll7 == 4:
            return "Something has happened to your parents: Your parent(s) have amnesia and don't remember you"
        elif roll7 == 5:
            return (
                "Something has happened to your parents: You never knew your parent(s)"
            )
        elif roll7 == 6:
            return "Something has happened to your parents: Your parent(s) are in hiding to protect you"
        elif roll7 == 7:
            return "Something has happened to your parents: You were left with relatives for safekeeping"
        elif roll7 == 8:
            return "Something has happened to your parents: You grew up on the Street and never had parents"
        elif roll7 == 9:
            return "Something has happened to your parents: Your parent(s) gave you up for adoption"
        elif roll7 == 10:
            return "Something has happened to your parents: Your parent(s) sold you for money"

    if roll6 < 7:
        return "Both parents are living"
    else:
        return something_happened(roll(10))


def family_status(roll8):
    if roll8 < 7:
        def family_tragedy(roll9):
            if roll9 == 1:
                return "Family status is in danger, and you risk losing everything (if you haven't already: Family lost everything through betrayal"
            elif roll9 == 2:
                return "Family status is in danger, and you risk losing everything (if you haven't already: Family lost everything through bad management"
            elif roll9 == 3:
                return "Family status is in danger, and you risk losing everything (if you haven't already: Family exiled or otherwise driven from their original home/nation/corporation"
            elif roll9 == 4:
                return "Family status is in danger, and you risk losing everything (if you haven't already: Family is imprisoned and you alone escaped"
            elif roll9 == 5:
                return "Family status is in danger, and you risk losing everything (if you haven't already: Family vanished. You are the only remaining remember"
            elif roll9 == 6:
                return "Family status is in danger, and you risk losing everything (if you haven't already: Family was murdered/killed and you were the only survivor"
            elif roll9 == 7:
                return "Family status is in danger, and you risk losing everything (if you haven't already: Family is involved in a longterm conspiracy, organization or association, such as crime family or revolutionary group"
            elif roll9 == 8:
                return "Family status is in danger, and you risk losing everything (if you haven't already: Your family was scattered to the winds due to misfortune"
            elif roll9 == 9:
                return "Family status is in danger, and you risk losing everything (if you haven't already: Your family is cursed with a hereditary feud that has lasted for generations"
            elif roll9 == 10:
                return "Family status is in danger, and you risk losing everything (if you haven't already: You are the inheritor of a family debt; you must honor this debt before moving on with your life"

        return family_tragedy(roll(10))
    else:
        return "Family status is OK, even if parents are missing or dead"


def childhood_env(roll10):
    if roll10 == 1:
        return "Childhood enviroment: Spent on the Street, with no adult supervision"
    elif roll10 == 2:
        return "Childhood enviroment: Spent on in a safe Corporate Suburbia"
    elif roll10 == 3:
        return "Childhood enviroment: In a Nomad Pack moving from town to town"
    elif roll10 == 4:
        return "Childhood enviroment: In a decaying, once upscale neighborhood"
    elif roll10 == 5:
        return "Childhood enviroment: In a defended Corporate Zone in the central city"
    elif roll10 == 6:
        return "Childhood enviroment: In the heart of the Combat Zone"
    elif roll10 == 7:
        return "Childhood enviroment: In a small village or town far from the City"
    elif roll10 == 8:
        return "Childhood enviroment: In a large arcology city"
    elif roll10 == 9:
        return "Childhood enviroment: In a aquatic Pirate pack"
    elif roll10 == 10:
        return (
            "Childhood enviroment: On a Corporate controlled Farm or Research Facility"
        )


def siblings(roll11):
    def gender(roll12):
        if (roll12 % 2) == 0:
            return "Sibling gender: Female. "
        else:
            return "Sibling gender: Male. "

    def age_difference(roll13):
        if roll13 < 6:
            return "Sibling relative to yourself: Older. "
        elif roll13 == 10:
            return "Sibling relative to yourself: Twin. "
        else:
            return "Sibling relative to yourself: Younger. "

    def feelings(roll14):
        if roll14 < 3:
            return "Sibling feelings about you: Sibling dislikes you| "
        elif roll14 == 3:
            return "Sibling feelings about you: Sibling likes you.| "
        elif roll14 == 4:
            return "Sibling feelings about you: Sibling likes you.| "
        elif roll14 == 5:
            return "Sibling feelings about you: Sibling are neutral.| "
        elif roll14 == 6:
            return "Sibling feelings about you: Sibling are neutral.| "
        elif roll14 == 7:
            return "Sibling feelings about you: They hero worship you.| "
        elif roll14 == 8:
            return "Sibling feelings about you: They hero worship you.| "
        else:
            return "Sibling feelings about you: They hate you.| "

    if roll11 > 7:
        return "Sibling: You are a only child"
    else:
        s = ""
        for i in range(roll11):
            s += gender(roll(10)) + age_difference(roll(10)) + feelings(roll(10))
        return s


def personality(roll15):
    if roll15 == 1:
        return "Personality: Shy and secretive"
    elif roll15 == 2:
        return "Personality: Rebellious, antisocial, violent"
    elif roll15 == 3:
        return "Personality: Arrogant, proud and aloof"
    elif roll15 == 4:
        return "Personality: Moody, rash and headstrong"
    elif roll15 == 5:
        return "Personality: Picky, fussy and nervous"
    elif roll15 == 6:
        return "Personality: Stable and serious"
    elif roll15 == 7:
        return "Personality: Silly and fluffheaded"
    elif roll15 == 8:
        return "Personality: Sneaky and deceptive"
    elif roll15 == 9:
        return "Personality: Intellectual and detached"
    elif roll15 == 10:
        return "Personality: Friendly and outgoing"


def person_you_value(roll16):
    if roll16 == 1:
        return "Person you value the most: A parent"
    elif roll16 == 2:
        return "Person you value the most: Brother or sister"
    elif roll16 == 3:
        return "Person you value the most: Lover"
    elif roll16 == 4:
        return "Person you value the most: Friend"
    elif roll16 == 5:
        return "Person you value the most: Yourself"
    elif roll16 == 6:
        return "Person you value the most: A pet"
    elif roll16 == 7:
        return "Person you value the most: Teacher or mentor"
    elif roll16 == 8:
        return "Person you value the most: Public figure"
    elif roll16 == 9:
        return "Person you value the most: A personal hero"
    elif roll16 == 10:
        return "Person you value the most: No one"


def do_you_value(roll17):
    if roll17 == 1:
        return "What do you value the most: Money"
    elif roll17 == 2:
        return "What do you value the most: Honor"
    elif roll17 == 3:
        return "What do you value the most: Your word"
    elif roll17 == 4:
        return "What do you value the most: Honesty"
    elif roll17 == 5:
        return "What do you value the most: Knowledge"
    elif roll17 == 6:
        return "What do you value the most: Vengeance"
    elif roll17 == 7:
        return "What do you value the most: Love"
    elif roll17 == 8:
        return "What do you value the most: Power"
    elif roll17 == 9:
        return "What do you value the most: Having a good time"
    elif roll17 == 10:
        return "What do you value the most: Friendship"


def feeling_people(roll18):
    if (roll18 == 1) or (roll18 == 2):
        return "How do you feel about most people: Neutral"
    elif roll18 == 3:
        return "How do you feel about most people: I like almost everyone"
    elif roll18 == 4:
        return "How do you feel about most people: I hate almost everyone"
    elif roll18 == 5:
        return "How do you feel about most people: People are tools. Use them for your own goals and discard them"
    elif roll18 == 6:
        return "How do you feel about most people: Every person is valuable individual"
    elif roll18 == 7:
        return "How do you feel about most people: People are obstacles to be destroyed if they cross me"
    elif roll18 == 8:
        return "How do you feel about most people: People are untrustworthy. Don't depend on anyone"
    elif roll18 == 9:
        return "How do you feel about most people: Wipe'em all out and give the place to the cockroaches"
    elif roll18 == 10:
        return "How do you feel about most people: People are wonderful"


def thing_you_value(roll19):
    if roll19 == 1:
        return "Your most valued possession: A weapon"
    elif roll19 == 2:
        return "Your most valued possession: A tool"
    elif roll19 == 3:
        return "Your most valued possession: A piece of clothing"
    elif roll19 == 4:
        return "Your most valued possession: A photograph"
    elif roll19 == 5:
        return "Your most valued possession: A book or diary"
    elif roll19 == 6:
        return "Your most valued possession: A recording"
    elif roll19 == 7:
        return "Your most valued possession: A musical instrument"
    elif roll19 == 8:
        return "Your most valued possession: A piece of jewelry"
    elif roll19 == 9:
        return "Your most valued possession: A toy"
    elif roll19 == 10:
        return "Your most valued possession: A letter"


def happenings(age):
    def life_events(roll20):
        if roll20 < 4:
            return big_problems_big_wins(roll(10))
        elif (roll20 == 7) or (roll20 == 8):
            return romantic_involvement(roll(10))
        elif roll20 > 8:
            return "Nothing happened that year"
        else:
            return friends_and_enemies(roll(10))

    def big_problems_big_wins(roll21):
        def get_lucky(roll22):
            if roll22 == 1:

                def powerful_connection(roll24):
                    if roll24 < 5:
                        return "Big Problems, Big Wins; You scored big and made a powerful connection: It's Police Debt"
                    if roll24 > 7:
                        return "Big Problems, Big Wins; You scored big and made a powerful connection: In the mayor's office"
                    else:
                        return "Big Problems, Big Wins; You scored big and made a powerful connection: It's in the District Attorney's Office"

                return powerful_connection(roll(10))
            elif roll22 == 2:
                return "Big Problems, Big Wins; You scored big and had a Finnancial Windfall: " + str(roll(10) * 100) + " Eurodollars"
            elif roll22 == 3:
                return "Big Problems, Big Wins; You scored big and got a big score on job or deal of " + str(roll(10) * 100) + " Eurodollars"
            elif roll22 == 4:
                return "Big Problems, Big Wins; You scored big and found a Sensei(teacher): Begin at +2 or add +1 to a Martial Arts Skill of your choice."
            elif roll22 == 5:
                return "Big Problems, Big Wins; You scored big and found a Teacher: Add +1 to any INT based skill, or begin a new INT based skill at +2"
            elif roll22 == 6:
                return "Big Problems, Big Wins; You scored big and a Power Corporate Exec owes you one favor"
            elif roll22 == 7:
                return "Big Problems, Big Wins; You scored big and the Local Nomad Pack befriends you. You can call upon them for one favor a month, equivalent to a Family Special ability of +2."
            elif roll22 == 8:
                return "Big Problems, Big Wins; You scored big and made a Friend on the Police Force. You may use him for inside information at a level of +2 Streetwise on any police related situation"
            elif roll22 == 9:
                return "Big Problems, Big Wins; You scored big and the Local Boostergang likes you (Who knows why These are Boosters, right?) You can call upon them for 1 favor a month, equivalent to a Family Special Ability of +2. But don't push it."
            elif roll22 == 10:
                return "Big Problems, Big Wins; You scored big and found a Combat Teacher. Add +1 to any weapon skill with the exception of Martial Arts or Brawling, or begin a new combat skill at +2"

        def disaster_strikes(roll24):
            if roll24 == 1:
                return "You took a hit: Financial loss or Debt of" + str(roll(10) * 100) + " Eurodollars"
            elif roll24 == 2:
                return "You took a hit; Imprisonment: You have been in prison, or held hostage (your choice) for " + str(roll(10)) + "months."
            elif roll24 == 3:
                return "You took a hit: Illness or addiction: You have contracted either an illness or drug habit in this time. Lost 1 pt of REF permanently as a result."
            elif roll24 == 4:

                def betrayal(roll25):
                    if roll25 < 4:
                        return "You took a hit; Betrayal: you have been backstabbed in following manner: You are being blackmailed"
                    if roll25 > 7:
                        return "You took a hit; Betrayal: you have been backstabbed in following manner: You were betrayed by a close friend in either romance or career"
                    else:
                        return "You took a hit; Betrayal: you have been backstabbed in following manner: A secret was exposed"

                return betrayal(roll(10))
            elif roll24 == 5:

                def accident(roll26):
                    if roll26 < 5:
                        return "You were in some kind of terrible accident: You were terribly disfigured and must substract -5 from your ATT."
                    elif (roll26 == 5) or (roll26 == 6):
                        return "You were in some kind of terrible accident: You were hospitalized for " + str(roll(10)) + " months that year"
                    elif roll26 == 7:
                        return "You were in some kind of terrible accident: You've lost " + str(roll(10)) + " months of memory that year"
                    elif roll26 == 8:
                        return "You were in some kind of terrible accident: You've lost " + str(roll(10)) + " months of memory that year"
                    else:
                        return "You were in some kind of terrible accident: You constantly relieve nightmares (8 in 10 each night) of the accident and wake up screaming"

                return accident(roll(10))
            elif roll24 == 6:

                def lover_killed(roll27):
                    if roll27 < 6:
                        return "Lover, friend or relative killed, You lost someone you really cared about: They died accidentaly"
                    elif roll27 > 8:
                        return "Lover, friend or relative killed, You lost someone you really cared about: They were murdered and you know who did it. You just need the proof"
                    else:
                        return "Lover, friend or relative killed, You lost someone you really cared about: They were murdered by unknown parties"

                return lover_killed(roll(10))
            elif roll24 == 7:

                def set_up(roll28):
                    if roll28 < 4:
                        return "You were set up, false accusation: The accusation is theft"
                    elif roll28 == 4:
                        return "You were set up, false accusation: it's cowardice"
                    elif roll28 == 5:
                        return "You were set up, false accusation: it's cowardice"
                    elif roll28 == 9:
                        return "You were set up, false accusation: It's rape"
                    elif roll28 == 10:
                        return "You were set up, false accusation: It's lying or betrayal"
                    else:
                        return "You were set up, false accusation: It's murder"

                return set_up(roll(10))
            elif roll24 == 8:

                def crime(roll29):
                    if roll29 < 4:
                        return "Haunted by the law: You are haunted by the law for crimes you may or may not have committed (your choice): Only a couple of local cops want you"
                    elif roll29 == 7:
                        return "Haunted by the law: You are haunted by the law for crimes you may or may not have committed (your choice): It's the State Police or Militia"
                    elif roll29 == 8:
                        return "Haunted by the law: You are haunted by the law for crimes you may or may not have committed (your choice): It's the State Police or Militia"
                    elif (roll29 == 9) or (roll29 == 10):
                        return "Haunted by the law: You are haunted by the law for crimes you may or may not have committed (your choice): It's the FBI or equivalent national police force"
                    else:
                        return "Haunted by the law: You are haunted by the law for crimes you may or may not have committed (your choice): It's the entire local force"

                return crime(roll(10))
            elif roll24 == 9:

                def mad_corporation(roll30):
                    if roll30 < 4:
                        return "Haunted by a Corporation: You have angered some corporate honcho: It's a small, local firm"
                    elif (roll30 == 7) or (roll30 == 8):
                        return "Haunted by a Corporation: You have angered some corporate honcho: It's a big national corp with agents in major cities nationwide"
                    elif (roll30 == 9) or (roll30 == 10):
                        return "Haunted by a Corporation: You have angered some corporate honcho: It's a huge multinational with armies, ninjas and spies everywhere"
                    else:
                        return "Haunted by a Corporation: You have angered some corporate honcho: It's a larger corp with offices statewide"

                return mad_corporation(roll(10))
            elif roll24 == 10:

                def incapacitation(roll31):
                    if roll31 < 4:
                        return "Mental or physical incapacitation: You have experienced some type of mental breakdown: It's some type of nervous disorder, probably from a bioplague=lose 1 pt. REF"
                    elif roll31 > 7:
                        return "Mental or physical incapacitation: You have experienced some type of mental breakdown: it's a major psychosis. You hear voices, are violent, irrational, depressive. Lose 1 pt from your CL, 1 from REF"
                    else:
                        return "Mental or physical incapacitation: You have experienced some type of mental breakdown: It's some kind of mental problem; you suffer anxiety attacks and phobias. Lose 1 pt from your CL stat"

                return incapacitation(roll(10))

        def what_ya_do(roll32):
            if roll32 < 3:
                return "What you're going to do about it: Clear your name"
            elif (roll32 == 3) or (roll32 == 4):
                return "What you're going to do about it: Live it down and try to forget it"
            elif (roll32 == 5) or (roll32 == 6):
                return "What you're going to do about it: Hunt down those responsible and make them pay"
            elif (roll32 == 7) or (roll32 == 8):
                return "What you're going to do about it: Get what's rightfully yours"
            elif roll32 > 8:
                return "What you're going to do about it: Save, if possible, anyone else involved in the situation"

        if (roll21 % 2) == 0:
            return get_lucky(roll(10))
        else:
            return disaster_strikes(roll(10)), what_ya_do(roll(10))

    def romantic_involvement(roll33):
        if roll33 < 5:
            return "Romantic Involvement: Happy love affair"
        elif roll33 == 5:

            def tragic_love(roll34):
                if roll34 == 1:
                    return "Romantic involvement resulted in a Tragic love affair: Lover died in accident"
                elif roll34 == 2:
                    return "Romantic involvement resulted in a Tragic love affair: Lover mysteriously vanished"
                elif roll34 == 3:
                    return "Romantic involvement resulted in a Tragic love affair: It didn't work out"
                elif roll34 == 4:
                    return "Romantic involvement resulted in a Tragic love affair: A personal goal or vendetta came between you"
                elif roll34 == 5:
                    return "Romantic involvement resulted in a Tragic love affair: Lover kidnapped"
                elif roll34 == 6:
                    return "Romantic involvement resulted in a Tragic love affair: Lover went insane"
                elif roll34 == 7:
                    return "Romantic involvement resulted in a Tragic love affair: Lover committed suicide"
                elif roll34 == 8:
                    return "Romantic involvement resulted in a Tragic love affair: Lover killed in a fight"
                elif roll34 == 9:
                    return "Romantic involvement resulted in a Tragic love affair: Rival cut you out of the action"
                elif roll34 == 10:
                    return "Romantic involvement resulted in a Tragic love affair: Lover imprisoned or exiled"

            def mutual_feelings(roll35):
                if roll35 == 1:
                    return "Mutual feelings: They still love you"
                elif roll35 == 2:
                    return "Mutual feelings: You still love them"
                elif roll35 == 3:
                    return "Mutual feelings: You still love each other"
                elif roll35 == 4:
                    return "Mutual feelings: You hate them"
                elif roll35 == 5:
                    return "Mutual feelings: They hate you"
                elif roll35 == 6:
                    return "Mutual feelings: You hate each other"
                elif roll35 == 7:
                    return "Mutual feelings: You're friends"
                elif roll35 == 8:
                    return "Mutual feelings: No feeling's either way; it's over"
                elif roll35 == 9:
                    return "Mutual feelings: You like them, they hate you"
                elif roll35 == 10:
                    return "Mutual feelings: They like you, you hate them"

            return tragic_love(roll(10)), mutual_feelings(roll(10))
        elif (roll33 == 6) or (roll33 == 7):

            def love_with_problems(roll36):
                if roll36 == 1:
                    return "Romantic involvement resulted in love affair with problems: Your lover's friend/family hate you"
                elif roll36 == 2:
                    return "Romantic involvement resulted in love affair with problems: Your lover's friends/family would use any means \
                    to get rid of you"
                elif roll36 == 3:
                    return "Romantic involvement resulted in love affair with problems: You friend's/family hate your lover"
                elif roll36 == 4:
                    return "Romantic involvement resulted in love affair with problems: One of you has a romantic rival"
                elif roll36 == 5:
                    return "Romantic involvement resulted in love affair with problems: You fight constantly"
                elif roll36 == 6:
                    return "Romantic involvement resulted in love affair with problems: Concentrate and ask again"
                elif roll36 == 7:
                    return "Romantic involvement resulted in love affair with problems: You're professional rivals"
                elif roll36 == 8:
                    return "Romantic involvement resulted in love affair with problems: One of you is insanely jealous"
                elif roll36 == 9:
                    return 'Romantic involvement resulted in love affair with problems: One of you is "messin\' around" '
                elif roll36 == 10:
                    return "Romantic involvement resulted in love affair with problems: You have conflicting backgrounds and families"

            return love_with_problems(roll(10))
        else:
            return "Romantic Involvement: Fast Affairs and Hot Dates"

    def friends_and_enemies(roll37):
        if roll37 < 6:

            def friend_gender(roll38):
                if (roll38 % 2) == 0:
                    return "Friends & Enemies: You made a friend and that friend is male "
                else:
                    return "Friends & Enemies: You made a friend and that friend is female "

            def friend_relationship(roll39):
                if roll39 == 1:
                    return "The friend is: Like a big brother/sister to you"
                elif roll39 == 2:
                    return "The friend is: Like a kid sister/brother to you"
                elif roll39 == 3:
                    return "The friend is: A teacher or mentor"
                elif roll39 == 4:
                    return "The friend is: A partner or co-worker"
                elif roll39 == 5:
                    return "The friend is: An old lover (choose which one)"
                elif roll39 == 6:
                    return "The friend is: An old enemy (choose which one)"
                elif roll39 == 7:
                    return "The friend is: Like a foster parent to you"
                elif roll39 == 8:
                    return "The friend is: A relative"
                elif roll39 == 9:
                    return "The friend is: Reconnect with an old childhood friend"
                elif roll39 == 10:
                    return "The friend is: Met through a common interest"

            return friend_gender(roll(10)), friend_relationship(roll(10))
        else:

            def enemy_gender(roll40):
                if (roll40 % 2) == 0:
                    return "You made an enemy and the enemy is male"
                else:
                    return "You made an enemy and the enemy is female"

            def enemy_kind(roll41):
                if roll41 == 1:
                    return "The enemy is a: Ex friend"
                elif roll41 == 2:
                    return "The enemy is a: Ex lover"
                elif roll41 == 3:
                    return "The enemy is a: Relative"
                elif roll41 == 4:
                    return "The enemy is a: Childhood enemy"
                elif roll41 == 5:
                    return "The enemy is a: Person working for you"
                elif roll41 == 6:
                    return "The enemy is a: Person you work for"
                elif roll41 == 7:
                    return "The enemy is a: Partner or co-worker"
                elif roll41 == 8:
                    return "The enemy is a: Booster gang member"
                elif roll41 == 9:
                    return "The enemy is a: Corporate Exec"
                elif roll41 == 10:
                    return "The enemy is a: government Official"

            def cause_of_enemy(roll42):
                if roll42 == 1:
                    return "The enmity started when one of you: Caused the other to lose face"
                elif roll42 == 2:
                    return "The enmity started when one of you: Caused the loss of a lover, friend or relative"
                elif roll42 == 3:
                    return "The enmity started when one of you: Caused a major humiliation"
                elif roll42 == 4:
                    return "The enmity started when one of you: Accused the other of cowardice or some other personal flaw"
                elif roll42 == 5:

                    def disability(roll43):
                        if roll43 < 3:
                            return "The enmity started when one of you caused a physical disability: Lose eye"
                        elif roll43 > 4:
                            return "The enmity started when one of you caused a physical disability: badly scarred"
                        else:
                            return "The enmity started when one of you caused a physical disability: Lose arm"

                    return disability(roll(6))
                elif roll42 == 6:
                    return "The enmity started when one of you: Deserted or betrayed each other"
                elif roll42 == 7:
                    return "The enmity started when one of you: Turned down other's offer of jobs or romantic involvement"
                elif roll42 == 8:
                    return "The enmity started when one of you: You just didn't like each other"
                elif roll42 == 9:
                    return "The enmity started when one of you: Was a romantic rival"
                elif roll42 == 10:
                    return "The enmity started when one of you: Foiled a plan of the other's"

            def whos_mad(roll44):
                if roll44 < 5:
                    return "Who's fracked off: They hate you"
                elif roll44 > 7:
                    return "Who's fracked off: The feeling's mutual"
                else:
                    return "Who's fracked off: You hate them"

            def watcha_gonna_do(roll45):
                if (roll45 == 1) or (roll45 == 2):
                    return "If the two met face to face, the injured party would most likely: Go into a murderous, killing rage and rip his face off!"
                elif (roll45 == 3) or (roll45 == 4):
                    return "If the two met face to face, the injured party would most likely: Avoid the scum"
                elif (roll45 == 5) or (roll45 == 6):
                    return "If the two met face to face, the injured party would most likely: Backstab him indirectly"
                elif (roll45 == 7) or (roll45 == 8):
                    return "If the two met face to face, the injured party would most likely: Ignore the scum"
                else:
                    return "If the two met face to face, the injured party would most likely: Rip into him verbally"

            def enemy_potential(roll46):
                if roll46 < 4:
                    return "What can he throw against you: Just himself"
                elif (roll46 == 4) or (roll46 == 5):
                    return "What can he throw against you: Himself and a few friends"
                elif (roll46 == 6) or (roll46 == 7):
                    return "What can he throw against you: An entire gang"
                elif roll46 == 8:
                    return "What can he throw against you: A small corporation"
                elif roll46 == 9:
                    return "What can he throw against you: A large corporation"
                elif roll46 == 10:
                    return "An entire government Agency"

            return (
                enemy_gender(roll(10)),
                enemy_kind(roll(10)),
                cause_of_enemy(roll(10)),
                whos_mad(roll(10)),
                watcha_gonna_do(roll(10)),
                enemy_potential(roll(10)),
            )

    t = ""
    for i in range(age - 16):
        t = t + str(life_events(roll(10))) + "\n"
    return t


while True:
    age = roll(6) + roll(6) + 16
    input("Type anything to generate your new lifepath ")
    a = clothes(roll(10))
    b = hairstyle(roll(10))
    c = affectations(roll(10))
    d = ethnic(roll(10))
    e = family_rank(roll(10))
    f = parents(roll(10))
    g = family_status(roll(10))
    h = childhood_env(roll(10))
    j = siblings(roll(10))
    k = personality(roll(10))
    l = person_you_value(roll(10))
    m = do_you_value(roll(10))
    n = feeling_people(roll(10))
    o = thing_you_value(roll(10))
    p = happenings(age)
    print("You are " + str(age) + " years old")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(k)
    print(l)
    print(m)
    print(n)
    print(o)
    print("")
    print("About siblings:")
    print(j)
    print("")
    print("These are the major events in your life: ")
    print(p)
    print("")
