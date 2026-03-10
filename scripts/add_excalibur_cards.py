#!/usr/bin/env python3
"""
Add ~60 new Excalibur Con 2026 cards based on real convention data:
- Celebrity guests (SungWon Cho/ProZD, Marissa Lenti, Andrew Gray, etc.)
- DECC venue rooms (Pioneer Hall, Edmund Fitzgerald Hall, Split Rock, etc.)
- Gaming events (North Star Open, Lady of the Lake, Magic drafts, etc.)
- Panels, workshops, activities, community organizations
- Third pre-constructed deck: "Excalibur Experience"
"""

import json
import os

# ============================================================
# NEW CARDS — Excalibur Con 2026 Expansion
# ============================================================

NEW_CARDS = [
    # ==================== PEOPLE (20 cards) ====================
    {
        "id": "card_ex78",
        "name": "SungWon Cho",
        "type": "People",
        "rarity": "Legendary",
        "lp": 4,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 1},
        "totalCost": 2,
        "initiative": 4,
        "abilities": [
            {"trigger": "activate", "text": "Each player draws 1 card. You gain 1 LP for each People card you control with the Convention tag."},
            {"trigger": "played", "text": "All People you control gain +1 LP until end of Winter."}
        ],
        "flavorText": "His voice fills the hall — and somehow, everyone laughs at the same time.",
        "artNotes": "Charismatic man at a signing table, long line of excited fans, convention hall backdrop.",
        "image": "",
        "tags": ["Guest", "Pop Culture", "Convention"],
        "localConnection": {"type": "person", "name": "SungWon Cho (ProZD)", "description": "Voice actor and content creator, celebrity guest at Excalibur Con 2026"},
        "designerNotes": "Legendary headliner. Played trigger gives an immediate board-wide LP buff. Activate is generous (both draw) but you get the LP bonus. High initiative resolves first. 4 LP base is premium for 2 cost — justified by Legendary rarity.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex79",
        "name": "Marissa Lenti",
        "type": "People",
        "rarity": "Rare",
        "lp": 3,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "initiative": 3,
        "abilities": [
            {"trigger": "activate", "text": "Choose a People card you control. It gains +1 LP until end of Winter. If it has the Guest tag, gain 1 Expression token from the pool."},
            {"trigger": "summer", "text": "If you control 2 or more Guest-tagged cards, draw 1 card."}
        ],
        "flavorText": "She brought the Amazing Digital Circus to life — and Duluth couldn't get enough.",
        "artNotes": "Voice actress at a microphone during a panel, animated expressions, audience captivated.",
        "image": "",
        "tags": ["Guest", "Pop Culture", "Convention"],
        "localConnection": {"type": "person", "name": "Marissa Lenti", "description": "Voice of Pomni in The Amazing Digital Circus, panel guest at Excalibur Con"},
        "designerNotes": "Strong Rare. Activate buffs others and gives resource back if Guest synergy. Summer draw rewards a Guest-heavy board. 3 LP at 1 cost is pushed — Rare rarity justifies it.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex80",
        "name": "Andrew Gray",
        "type": "People",
        "rarity": "Uncommon",
        "lp": 2,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 1, "learning": 0},
        "totalCost": 2,
        "initiative": 3,
        "abilities": [
            {"trigger": "activate", "text": "Choose a People card you control. It becomes Ready. (It may activate again this Summer.)"},
            {"trigger": "combo", "text": "If Christina Masterson is in play, both gain +1 LP."}
        ],
        "flavorText": "The Red Ranger taught Superhero U — and the crowd paid close attention.",
        "artNotes": "Athletic man in a teaching pose, convention stage, fans in superhero costumes.",
        "image": "",
        "tags": ["Guest", "Pop Culture", "Convention"],
        "localConnection": {"type": "person", "name": "Andrew Gray", "description": "Power Rangers Megaforce actor, runs Superhero U workshop at Excalibur Con"},
        "designerNotes": "Readying another People is very strong action advantage. Combo with Christina rewards running both. 2 LP + 2 cost is fair for the powerful activate.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex81",
        "name": "Christina Masterson",
        "type": "People",
        "rarity": "Uncommon",
        "lp": 2,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 1, "learning": 0},
        "totalCost": 2,
        "initiative": 2,
        "abilities": [
            {"trigger": "activate", "text": "Draw 1 card. If you control a card with the Guest tag, draw 2 instead and discard 1."},
            {"trigger": "combo", "text": "If Andrew Gray is in play, both gain +1 LP."}
        ],
        "flavorText": "The Pink Ranger had stories that kept the whole panel room on the edge of their seats.",
        "artNotes": "Woman at a panel table sharing stories, engaged audience, colorful convention decorations.",
        "image": "",
        "tags": ["Guest", "Pop Culture", "Convention"],
        "localConnection": {"type": "person", "name": "Christina Masterson", "description": "Power Rangers Megaforce actress, panel guest at Excalibur Con"},
        "designerNotes": "Card draw engine. Combo pair with Andrew Gray — run both for mutual +1 LP. Activate draw is bread-and-butter useful. 2 LP base at 2 cost is standard.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex82",
        "name": "Elle Firespray",
        "type": "People",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "initiative": 1,
        "abilities": [
            {"trigger": "activate", "text": "Choose a People card you control. It gains the Artist tag until end of Winter."},
            {"trigger": "ongoing", "text": "People you control with the Artist tag have +1 LP."}
        ],
        "flavorText": "A steady hand, a fine brush, and suddenly that gray plastic becomes a hero.",
        "artNotes": "Person carefully painting a miniature figure at a workshop table, paint pots arrayed around them.",
        "image": "",
        "tags": ["Artist", "Convention", "Learning"],
        "localConnection": {"type": "person", "name": "Elle Firespray", "description": "Mini painting instructor who runs beginner and advanced classes at Excalibur Con"},
        "designerNotes": "Artist tag enabler. Her ongoing makes all Artists better, and her activate lets non-Artists join the party. Low cost, low LP base — value comes from synergy.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex83",
        "name": "Dave Wheeler",
        "type": "People",
        "rarity": "Common",
        "lp": 2,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "initiative": 2,
        "abilities": [
            {"trigger": "activate", "text": "Gain 1 LP if you control another card with the Artist tag."},
            {"trigger": "autumn", "text": "If you played an Event this Summer, draw 1 card."}
        ],
        "flavorText": "His pen never stopped moving — sketches for fans between every panel.",
        "artNotes": "Comic book artist sketching at a table, stacks of comics and prints, fans watching him draw.",
        "image": "",
        "tags": ["Artist", "Convention", "Pop Culture"],
        "localConnection": {"type": "person", "name": "Dave Wheeler", "description": "Returning comic book artist at Excalibur Con"},
        "designerNotes": "Solid Artist-synergy People. Activate LP with Artist on board, Autumn draw for playing Events. Good in a mixed deck.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex84",
        "name": "Dylan Jacobson",
        "type": "People",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 0, "learning": 0},
        "totalCost": 1,
        "initiative": 1,
        "abilities": [
            {"trigger": "activate", "text": "Both players draw 1 card. You gain 1 LP."},
            {"trigger": "combo", "text": "If you control a Location with the Convention tag, gain 2 LP instead of 1."}
        ],
        "flavorText": "Drink & Draw wasn't just about the art — it was about making friends over ink and laughter.",
        "artNotes": "Artist hosting a social drawing event, people laughing and sketching together at a table with drinks.",
        "image": "",
        "tags": ["Artist", "Community", "Social"],
        "localConnection": {"type": "person", "name": "Dylan Jacobson", "description": "Local artist who hosts Dylan's Drink & Draw social art events at Excalibur Con"},
        "designerNotes": "Community-focused artist. Activate is generous — both players draw — but you get LP. Combo with Convention Location doubles the LP payoff. Social gameplay mirrors the character.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex85",
        "name": "Erin Glesner",
        "type": "People",
        "rarity": "Rare",
        "lp": 2,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 0, "learning": 1},
        "totalCost": 2,
        "initiative": 4,
        "abilities": [
            {"trigger": "activate", "text": "Choose a Location you control. Advance it 1 level (ignore the advance condition this time)."},
            {"trigger": "winter", "text": "Gain 1 LP for each developed Location you control (level 2+)."}
        ],
        "flavorText": "She built this con from the ground up — and she wasn't done yet.",
        "artNotes": "Confident woman with a clipboard and headset coordinating a bustling convention floor.",
        "image": "",
        "tags": ["Leader", "Convention", "Community"],
        "localConnection": {"type": "person", "name": "Erin Glesner", "description": "Committee Chair of Excalibur Con, the driving force behind the convention"},
        "designerNotes": "Keystone card for Location development decks. Activate bypasses advance conditions — extremely powerful. Winter LP scales with developed Locations. High initiative (4) means she plans ahead. Rare justified.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex86",
        "name": "Dave Sabik",
        "type": "People",
        "rarity": "Uncommon",
        "lp": 2,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 1, "learning": 0},
        "totalCost": 2,
        "initiative": 3,
        "abilities": [
            {"trigger": "activate", "text": "Your opponent discards 1 card of their choice. You gain 1 LP."},
            {"trigger": "summer", "text": "If you control another People card with the Convention tag, gain 1 Community token from the pool."}
        ],
        "flavorText": "The wrestling promoter brought the hype — and the crowd brought the noise.",
        "artNotes": "Energetic promoter with a microphone hyping up a crowd in a convention hall wrestling ring area.",
        "image": "",
        "tags": ["Pop Culture", "Convention", "Community"],
        "localConnection": {"type": "person", "name": "Dave Sabik", "description": "Local wrestling promoter, brings Discover Pro Wrestling entertainment to Excalibur Con"},
        "designerNotes": "Interaction card — opponent discards. Not too punishing (they choose), but repeated activation is strong. Summer resource gain with Convention synergy. Good tempo card.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex87",
        "name": "RPG Game Master",
        "type": "People",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 1,
        "initiative": 2,
        "abilities": [
            {"trigger": "activate", "text": "Look at the top 2 cards of your deck. Put 1 in your hand and 1 on the bottom."},
            {"trigger": "ongoing", "text": "Cards with the Gamer tag you play cost 1 fewer total resource (minimum 0)."}
        ],
        "flavorText": "Roll for initiative. Actually, never mind — I'll just tell you what happens.",
        "artNotes": "Person behind a GM screen with dice, maps, and miniatures, players gathered around a table.",
        "image": "",
        "tags": ["Gamer", "Learning", "Convention"],
        "localConnection": {"type": "role", "name": "RPG Game Masters", "description": "Volunteer GMs who run tabletop RPG sessions at Excalibur Con"},
        "designerNotes": "Card selection on activate plus cost reduction for Gamers. Solid utility card that enables the Gamer archetype. Low LP but high utility value.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex88",
        "name": "Cosplay Judge",
        "type": "People",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "initiative": 2,
        "abilities": [
            {"trigger": "activate", "text": "Choose a People card with the Artist tag. It gains +2 LP until end of Winter."},
            {"trigger": "autumn", "text": "If you control 2 or more Artist-tagged People, gain 1 LP."}
        ],
        "flavorText": "Craftsmanship, creativity, presentation — every stitch tells a story.",
        "artNotes": "Person with a judging clipboard examining an elaborate cosplay costume, bright stage lights.",
        "image": "",
        "tags": ["Artist", "Convention", "Pop Culture"],
        "localConnection": {"type": "role", "name": "Cosplay Contest Judges", "description": "Judges at the Excalibur Con cosplay contest in Split Rock"},
        "designerNotes": "Strong Artist buffer. +2 LP to an Artist is a big swing. Autumn bonus rewards having multiple Artists. Pairs well with Elle Firespray who grants Artist tags.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex89",
        "name": "Volunteer Coordinator",
        "type": "People",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 0, "learning": 0},
        "totalCost": 1,
        "initiative": 3,
        "abilities": [
            {"trigger": "activate", "text": "Ready another People card you control with cost 1 or less."},
            {"trigger": "played", "text": "Gain 1 Community token from the shared pool."}
        ],
        "flavorText": "Sixty volunteers, two days, one clipboard. She made it look easy.",
        "artNotes": "Organized person in a volunteer T-shirt directing helpers with a confident smile.",
        "image": "",
        "tags": ["Community", "Leader", "Convention"],
        "localConnection": {"type": "role", "name": "Volunteer Pod Leaders", "description": "Volunteer coordinators like Haley and Jackie who manage con volunteer teams"},
        "designerNotes": "Readying cheap People gives extra actions. Played trigger grabs a Community token for tempo. High initiative (3) on a 1-cost is good for setting up combos.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex90",
        "name": "VIP Badge Holder",
        "type": "People",
        "rarity": "Uncommon",
        "lp": 2,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 1, "sustainability": 0, "community": 0, "expression": 0, "learning": 0},
        "totalCost": 1,
        "initiative": 1,
        "abilities": [
            {"trigger": "played", "text": "Draw 2 cards."},
            {"trigger": "spring", "text": "You may Forage twice instead of once this Spring (take 2 from pool instead of 1)."}
        ],
        "flavorText": "Early entry, exclusive merch, and a lanyard that opens doors.",
        "artNotes": "Person proudly wearing a VIP badge entering the convention before the crowd, exclusive swag in hand.",
        "image": "",
        "tags": ["Convention", "Community", "Gathering"],
        "localConnection": {"type": "feature", "name": "VIP Early Entry", "description": "VIP badge holders enter at 10:30 AM, 30 minutes before general admission"},
        "designerNotes": "Strong draw on entry (2 cards). Spring resource doubling accelerates your economy. Low initiative means you don't get combat priority, but the value is in resources and cards.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex91",
        "name": "501st Legionnaire",
        "type": "People",
        "rarity": "Uncommon",
        "lp": 2,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 1, "learning": 0},
        "totalCost": 2,
        "initiative": 2,
        "abilities": [
            {"trigger": "ongoing", "text": "Other People you control with the Pop Culture tag have +1 LP."},
            {"trigger": "activate", "text": "Gain 1 LP for each Pop Culture-tagged card you played this year."}
        ],
        "flavorText": "The armor is screen-accurate. The dedication is off the charts.",
        "artNotes": "Person in detailed stormtrooper armor posing heroically, kids taking photos, convention backdrop.",
        "image": "",
        "tags": ["Pop Culture", "Community", "Convention"],
        "localConnection": {"type": "organization", "name": "501st Legion", "description": "Star Wars costuming organization with a double booth and changing room at Excalibur Con"},
        "designerNotes": "Pop Culture lord. Ongoing buff to Pop Culture People, activate scales with Pop Culture cards played this year. Rewards committing to the Pop Culture theme.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex92",
        "name": "Nerd Nite Presenter",
        "type": "People",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 1,
        "initiative": 2,
        "abilities": [
            {"trigger": "activate", "text": "Both players draw 1 card. You gain 1 LP."},
            {"trigger": "combo", "text": "If played during Summer, gain 1 Learning token from the pool."}
        ],
        "flavorText": "It's like TED talks, but with more lightsabers and less pretension.",
        "artNotes": "Enthusiastic speaker at a podium with a quirky presentation slide, engaged laughing audience.",
        "image": "",
        "tags": ["Learning", "Community", "Convention"],
        "localConnection": {"type": "event", "name": "Nerd Nite", "description": "Community speaker series featured at Excalibur Con with short fun presentations"},
        "designerNotes": "Knowledge sharing — both draw, you get LP. Combo bonus for Summer timing. Good common role-player.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex93",
        "name": "Warhammer General",
        "type": "People",
        "rarity": "Common",
        "lp": 2,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 1, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 2,
        "initiative": 3,
        "abilities": [
            {"trigger": "activate", "text": "Gain 1 LP. If you control a Location with the Gamer tag, gain 2 LP instead."},
            {"trigger": "ongoing", "text": "This card has +1 LP if you control 3 or more Gamer-tagged cards."}
        ],
        "flavorText": "Two thousand points of painted perfection, marshaled across a table-sized battlefield.",
        "artNotes": "Focused player moving miniature figures on an elaborate terrain board, dice scattered nearby.",
        "image": "",
        "tags": ["Gamer", "Convention", "Learning"],
        "localConnection": {"type": "event", "name": "North Star Open", "description": "Warhammer miniatures tournament hosted at Excalibur Con"},
        "designerNotes": "Gamer archetype payoff. Activate LP doubles with Gamer Location. Ongoing scales with Gamer board presence. Solid 2-cost body.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex94",
        "name": "Duluth D&D Player",
        "type": "People",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 1,
        "initiative": 1,
        "abilities": [
            {"trigger": "activate", "text": "Roll a die (mentally). Gain 1 or 2 LP (your choice — honor system!)."},
            {"trigger": "combo", "text": "If you control RPG Hall, gain 2 LP instead and draw 1 card."}
        ],
        "flavorText": "Natural 20! ...okay fine, it was a 12, but the roleplay was worth it.",
        "artNotes": "Excited player at a table rolling dice with dramatic flair, character sheets and snacks visible.",
        "image": "",
        "tags": ["Gamer", "Convention", "Youth"],
        "localConnection": {"type": "event", "name": "DD&D (Duluth Dungeons & Dragons)", "description": "Local D&D games run at Excalibur Con RPG Hall"},
        "designerNotes": "Fun flavor card. Activate gives 1-2 LP (player decides, honor system mirrors actual RPG play). Combo with RPG Hall is the real payoff. Cheap and cheerful.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex95",
        "name": "Celebrity Handler",
        "type": "People",
        "rarity": "Uncommon",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 0, "learning": 0},
        "totalCost": 1,
        "initiative": 3,
        "abilities": [
            {"trigger": "ongoing", "text": "Guest-tagged People you control cost 1 fewer total resource to play (minimum 0)."},
            {"trigger": "activate", "text": "Search the top 5 cards of your deck for a People card with the Guest tag. Add it to your hand. Put the rest on the bottom."}
        ],
        "flavorText": "Water, schedule, smile. Water, schedule, smile. Repeat for twelve hours.",
        "artNotes": "Focused person in a staff shirt walking briskly through a corridor with a clipboard and water bottles.",
        "image": "",
        "tags": ["Community", "Convention", "Leader"],
        "localConnection": {"type": "role", "name": "Celebrity Handlers", "description": "Staff who manage celebrity guest logistics at Excalibur Con"},
        "designerNotes": "Guest enabler. Ongoing discount makes Guests cheaper to deploy. Activate tutors for Guests. Low LP but high utility — you play this to find your headliners.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex96",
        "name": "Keith Hopkins",
        "type": "People",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "initiative": 2,
        "abilities": [
            {"trigger": "activate", "text": "Gain 2 LP if you played an Event this Summer."},
            {"trigger": "played", "text": "Look at the top card of your deck. You may put it on the bottom."}
        ],
        "flavorText": "A local story told on a global screen — the premiere was packed.",
        "artNotes": "Filmmaker with a camera and clapperboard, excited audience behind him at a screening.",
        "image": "",
        "tags": ["Artist", "Pop Culture", "Duluth"],
        "localConnection": {"type": "person", "name": "Keith Hopkins", "description": "Local filmmaker premiering 'Man with a Mania' at Excalibur Con"},
        "designerNotes": "Event-rewards People. Activate pays off big if you played an Event this Summer. Played trigger gives minor card selection. Event-heavy decks love this.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex97",
        "name": "Con Security",
        "type": "People",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 1, "sustainability": 0, "community": 0, "expression": 0, "learning": 0},
        "totalCost": 1,
        "initiative": 1,
        "abilities": [
            {"trigger": "ongoing", "text": "Your Locations cannot be affected by opponent's card abilities."},
            {"trigger": "spring", "text": "If you control 2 or more Locations, gain 1 Growth token from the pool."}
        ],
        "flavorText": "Badge check. Bag check. Smile check. All clear.",
        "artNotes": "Friendly but firm security guard at a convention entrance, checking badges.",
        "image": "",
        "tags": ["Community", "Convention", "Leader"],
        "localConnection": {"type": "role", "name": "Convention Security", "description": "Security team keeping Excalibur Con safe for all attendees"},
        "designerNotes": "Defensive card. Location protection is unique and valuable for Location-heavy decks. Spring resource gain with Location board. Low stats but high defensive utility.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },

    # ==================== LOCATIONS (12 cards) ====================
    {
        "id": "card_ex98",
        "name": "Pioneer Hall",
        "type": "Location",
        "rarity": "Rare",
        "lp": 2,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 1, "sustainability": 0, "community": 1, "expression": 0, "learning": 0},
        "totalCost": 2,
        "maxLevel": 3,
        "advanceCondition": "Control 3 or more cards with the Vendor or Convention tag",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: +1 LP per Vendor-tagged People you control. Lvl 2: Also, when you play a card, gain 1 Growth token from the pool (once per turn). Lvl 3: Also, all your cards cost 1 fewer total resource (minimum 0)."},
            {"trigger": "autumn", "text": "If at max level, gain 2 LP."}
        ],
        "flavorText": "One hundred and sixty booths. Every single one a world unto itself.",
        "artNotes": "Massive convention vendor hall with rows of colorful booths, banners, and streams of attendees.",
        "image": "",
        "tags": ["Convention", "Vendor", "Gathering"],
        "localConnection": {"type": "location", "name": "Pioneer Hall (DECC)", "description": "Main vendor and exhibitor hall at the DECC, fitting 160 booth spaces"},
        "designerNotes": "Premium vendor Location. 3 levels of scaling — LP, resources, cost reduction. Advance condition wants Vendor/Convention board. Autumn LP at max level is the payoff for investment.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex99",
        "name": "Edmund Fitzgerald Hall",
        "type": "Location",
        "rarity": "Uncommon",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 1, "learning": 0},
        "totalCost": 2,
        "maxLevel": 2,
        "advanceCondition": "Control 2 or more People with the Artist or Community tag",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: People with the Artist tag you control gain +1 LP. Lvl 2: Also, when you play a People card, draw 1 card."},
            {"trigger": "winter", "text": "Gain 1 LP for each Artist-tagged card you control."}
        ],
        "flavorText": "Cosplay booths, community partners, and a silent auction that got surprisingly loud.",
        "artNotes": "Colorful hall with cosplay displays, community booths, activity tables, and bustling attendees.",
        "image": "",
        "tags": ["Convention", "Community", "Artist"],
        "localConnection": {"type": "location", "name": "Edmund Fitzgerald Hall (DECC)", "description": "Home of cosplay booths, community partners, TCGs, and activities at Excalibur Con"},
        "designerNotes": "Artist/Community hub. Artist LP buff at level 1, card draw at level 2. Winter LP scales with Artists. Advance condition is achievable with Artist People.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex100",
        "name": "Split Rock Stage",
        "type": "Location",
        "rarity": "Uncommon",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "maxLevel": 2,
        "advanceCondition": "Control a People card with the Guest or Artist tag",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: Guest-tagged People you control have +1 LP. Lvl 2: Also, when a Guest-tagged People enters play, gain 1 LP."},
            {"trigger": "summer", "text": "If you control a Guest-tagged People, you may look at the top 2 cards of your deck and keep 1."}
        ],
        "flavorText": "The spotlight hits, the crowd roars, and for a moment everyone shares the magic.",
        "artNotes": "Grand stage with dramatic lighting, a performer center stage, packed audience in silhouette.",
        "image": "",
        "tags": ["Convention", "Pop Culture", "Guest"],
        "localConnection": {"type": "location", "name": "Split Rock (DECC)", "description": "Largest event room at the DECC, hosts celebrity panels and the cosplay contest"},
        "designerNotes": "Guest-focused Location. Cheap to play (1 cost), easy advance condition. Guest LP buff and entry bonus at level 2. Summer card selection. Core Location for Guest decks.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex101",
        "name": "French River Panels",
        "type": "Location",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 1,
        "maxLevel": 2,
        "advanceCondition": "Play 2 or more Events in a single year",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: Events you play cost 1 fewer total resource (minimum 0). Lvl 2: Also, when you play an Event, gain 1 LP."},
            {"trigger": "autumn", "text": "Draw 1 card."}
        ],
        "flavorText": "Two rooms, back-to-back panels, zero downtime — just how the con likes it.",
        "artNotes": "Convention panel rooms with rows of chairs, projector screen, speakers at a table, full audience.",
        "image": "",
        "tags": ["Convention", "Learning", "Gathering"],
        "localConnection": {"type": "location", "name": "French River 1 & 2 (DECC)", "description": "Twin panel rooms at the DECC hosting panels all weekend at Excalibur Con"},
        "designerNotes": "Event cost reducer and payoff. Level 1 makes Events cheaper, Level 2 adds LP per Event. Autumn draw is reliable. Advance condition rewards Event-heavy play.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex102",
        "name": "RPG Hall",
        "type": "Location",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 1,
        "maxLevel": 2,
        "advanceCondition": "Control 2 or more People with the Gamer tag",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: People with the Gamer tag have +1 LP. Lvl 2: Also, at the start of Summer, each player draws 1 card."},
            {"trigger": "winter", "text": "Gain 1 LP for each Gamer-tagged People you control."}
        ],
        "flavorText": "Eleven tables, a hundred dice, and stories that only get better with retelling.",
        "artNotes": "Long hall lined with RPG tables, each running a different game, dice and character sheets everywhere.",
        "image": "",
        "tags": ["Convention", "Gamer", "Learning"],
        "localConnection": {"type": "location", "name": "RPG Hall", "description": "Dedicated hall with 11 tables running tabletop RPG sessions at Excalibur Con"},
        "designerNotes": "Gamer hub. LP buff for Gamers, Summer draw at level 2, Winter LP scales. Pairs with Duluth D&D Player and Warhammer General. Advance condition is straightforward.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex103",
        "name": "Tournament Arena",
        "type": "Location",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "maxLevel": 2,
        "advanceCondition": "Control a People with the Gamer tag and have played an Event this year",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: When you play a card with the Gamer tag, gain 1 LP. Lvl 2: Also, Gamer-tagged Events give you +1 LP when played."},
            {"trigger": "autumn", "text": "If at level 2, look at the top 3 cards. Keep 1."}
        ],
        "flavorText": "Magic drafts, Star Wars showdowns, Lorcana leagues — there's always a tournament firing.",
        "artNotes": "Competitive card game tournament area with players focused on matches, brackets on a board behind them.",
        "image": "",
        "tags": ["Convention", "Gamer", "Pop Culture"],
        "localConnection": {"type": "location", "name": "Tournament Area", "description": "Card game tournament area hosting MTG, Star Wars Unlimited, Lorcana, and Nostalgix at Excalibur Con"},
        "designerNotes": "Gamer/Event crossover Location. LP on Gamer plays, bonus LP on Gamer Events at level 2. Autumn card selection at max level. Rewards a Gamer + Event mix.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex104",
        "name": "Sensory Sanctuary",
        "type": "Location",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 1, "community": 0, "expression": 0, "learning": 0},
        "totalCost": 1,
        "maxLevel": 2,
        "advanceCondition": "Have 5 or fewer cards in hand at the start of Winter",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: At the start of each Spring, you may discard 1 card to draw 2. Lvl 2: Also, gain 1 LP at the start of each Spring."},
            {"trigger": "winter", "text": "If you have the fewest cards in hand, gain 2 LP."}
        ],
        "flavorText": "Sometimes the bravest thing at a con is knowing when to step away and breathe.",
        "artNotes": "Quiet, softly-lit room with comfortable seating, dim lamps, calming colors, away from the bustle.",
        "image": "",
        "tags": ["Self-Care", "Community", "Convention"],
        "localConnection": {"type": "location", "name": "Sensory Sanctuary (Gooseberry 1)", "description": "Quiet room for attendees who need a sensory break, open both days at Excalibur Con"},
        "designerNotes": "Self-care themed. Advance condition rewards having fewer cards (a downside turned into upside). Spring card filtering, Winter LP for being behind on cards. Unique design space.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex105",
        "name": "Lake Superior Ballroom",
        "type": "Location",
        "rarity": "Uncommon",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 0, "learning": 0},
        "totalCost": 1,
        "maxLevel": 2,
        "advanceCondition": "Control 3 or more People cards",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: Your People cards with the Social tag have +1 LP. Lvl 2: Also, at the start of Summer, gain 1 Community token from the pool."},
            {"trigger": "winter", "text": "Gain 1 LP for each Social-tagged card you control."}
        ],
        "flavorText": "The bar, the music, the crowd — Saturday night at the con is where friendships are forged.",
        "artNotes": "Elegant ballroom with a bar, people socializing in costume, warm lighting, Lake Superior visible.",
        "image": "",
        "tags": ["Convention", "Social", "Community"],
        "localConnection": {"type": "location", "name": "Lake Superior Ballroom (DECC)", "description": "Social and bar area at the DECC, hub for evening events at Excalibur Con"},
        "designerNotes": "Social archetype Location. People-count advance condition. LP buff for Social People, Community resource generation. Winter LP scales with Social board.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex106",
        "name": "Community Gaming Lounge",
        "type": "Location",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 0, "learning": 0},
        "totalCost": 1,
        "maxLevel": 2,
        "advanceCondition": "Both players control at least 1 People card",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: Both players draw 1 extra card in Spring. Lvl 2: Also, both players gain +1 LP in Winter."},
            {"trigger": "summer", "text": "You may trade 1 token with your opponent (give 1, take 1 of a different type)."}
        ],
        "flavorText": "Strangers walk in, sit down, roll dice — and leave as friends.",
        "artNotes": "Open gaming area with groups playing board games, dice games, card games at communal tables.",
        "image": "",
        "tags": ["Convention", "Gamer", "Community"],
        "localConnection": {"type": "location", "name": "Community Gaming Area", "description": "Open board game and social gaming area at Excalibur Con, sponsored by Dwarf King Taxi"},
        "designerNotes": "Generous shared-benefit Location. Both players draw and gain LP. The 0 LP base and shared benefits mean the owner needs to win via other means. Summer token trade adds interaction.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex107",
        "name": "Gooseberry Workshop",
        "type": "Location",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "maxLevel": 2,
        "advanceCondition": "Control a People with the Artist tag",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: When you play a People card with the Artist tag, gain 1 LP. Lvl 2: Also, Artist-tagged People you play enter Ready."},
            {"trigger": "autumn", "text": "If you control 2+ Artist-tagged People, draw 1 card."}
        ],
        "flavorText": "Painting minis, bead art, historical crafts — every table a different creative outlet.",
        "artNotes": "Workshop room with multiple activity stations, people crafting and creating together.",
        "image": "",
        "tags": ["Convention", "Artist", "Learning"],
        "localConnection": {"type": "location", "name": "Gooseberry Rooms 2 & 3 (DECC)", "description": "Workshop and activity rooms at the DECC hosting painting classes, demos, and creative events"},
        "designerNotes": "Artist deployment Location. LP on Artist entry, level 2 lets Artists enter Ready (can activate immediately). Autumn draw for Artist board. Easy advance condition.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex108",
        "name": "Celebrity Green Room",
        "type": "Location",
        "rarity": "Uncommon",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 0, "learning": 0},
        "totalCost": 1,
        "maxLevel": 2,
        "advanceCondition": "Control a People with the Guest tag",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: Guest-tagged People cost 1 fewer total resource (min 0). Lvl 2: Also, when a Guest enters play, both players gain 1 LP."},
            {"trigger": "spring", "text": "If you control a Guest, you may Barter without returning a token (just take 2 different)."}
        ],
        "flavorText": "Behind every great panel is a quiet room with good snacks and a patient handler.",
        "artNotes": "Comfortable backstage room with refreshments, a celebrity relaxing before their panel.",
        "image": "",
        "tags": ["Convention", "Guest", "Community"],
        "localConnection": {"type": "location", "name": "Celebrity Green Room (DECC)", "description": "Backstage room for celebrity guests to prepare between panels and signings"},
        "designerNotes": "Guest infrastructure. Cost reduction for Guests, LP on Guest entry (shared — community vibe). Spring resource economy boost with Guest on board. 0 LP base because value is in enabling Guests.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex109",
        "name": "DPW Wrestling Ring",
        "type": "Location",
        "rarity": "Common",
        "lp": 1,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "maxLevel": 2,
        "advanceCondition": "Your opponent has more LP than you",
        "abilities": [
            {"trigger": "ongoing", "text": "Lvl 1: When you play a People card, your opponent discards 1 card (they choose). Lvl 2: Also gain 1 LP when opponent discards."},
            {"trigger": "summer", "text": "If you have fewer LP than your opponent, gain 2 LP."}
        ],
        "flavorText": "From the top rope! The crowd goes wild in Edmund Fitzgerald Hall!",
        "artNotes": "Wrestling ring set up in a convention hall, wrestlers performing for a cheering crowd.",
        "image": "",
        "tags": ["Convention", "Pop Culture", "Community"],
        "localConnection": {"type": "feature", "name": "Discover Pro Wrestling (DPW)", "description": "Live wrestling entertainment brought to Excalibur Con by promoter Dave Sabik"},
        "designerNotes": "Comeback mechanic Location. Advance condition requires being behind on LP — underdog theme matches wrestling. Discard on People entry disrupts opponent. Level 2 turns disruption into LP.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },

    # ==================== EVENTS (28 cards) ====================
    {
        "id": "card_ex110",
        "name": "North Star Open",
        "type": "Event",
        "rarity": "Uncommon",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 1, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 2,
        "abilities": [
            {"trigger": "played", "text": "Gain 3 LP. If you control a People with the Gamer tag, gain 4 LP instead. If you also control a Location with the Gamer tag, gain 5 LP."}
        ],
        "flavorText": "Armies clash across miniature battlefields — and glory goes to the most strategic general.",
        "artNotes": "Epic miniature wargaming tournament, armies deployed on elaborate terrain, focused players.",
        "image": "",
        "tags": ["Convention", "Gamer", "Learning"],
        "localConnection": {"type": "event", "name": "North Star Open", "description": "Warhammer miniatures tournament held at Excalibur Con"},
        "designerNotes": "Scaling LP Event. 3 base, 4 with Gamer People, 5 with Gamer Location. Rewards committing to Gamer board. 2-cost for up to 5 LP is strong but conditional.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex111",
        "name": "Lady of the Lake",
        "type": "Event",
        "rarity": "Uncommon",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 1, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 2,
        "abilities": [
            {"trigger": "played", "text": "Choose a Location you control. Advance it 1 level (ignore the advance condition). Gain 1 LP."}
        ],
        "flavorText": "The sword rose from the lake — or in this case, from a very well-painted table.",
        "artNotes": "Dramatic Kings of War miniature scene with a sword-in-lake tableau, players strategizing.",
        "image": "",
        "tags": ["Convention", "Gamer", "Learning"],
        "localConnection": {"type": "event", "name": "Lady of the Lake (Kings of War)", "description": "Kings of War miniatures event held early morning at Excalibur Con"},
        "designerNotes": "Location advancement Event. Bypasses advance conditions — very powerful for Location-heavy decks. 2 cost is fair for the effect. Named after the KoW event.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex112",
        "name": "Sealed Draft Frenzy",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Both players draw 3 cards, then each discards 2. Gain 1 LP."}
        ],
        "flavorText": "Crack the packs, build the deck, pray to the shuffle gods.",
        "artNotes": "Excited players opening card packs, sorting cards rapidly, tournament clock ticking.",
        "image": "",
        "tags": ["Convention", "Gamer", "Pop Culture"],
        "localConnection": {"type": "event", "name": "Magic Sealed Draft", "description": "Magic: The Gathering sealed draft events running all weekend at Excalibur Con"},
        "designerNotes": "Shared card churn. Both players draw 3 / discard 2 — net +1 for both, but you get LP. Cheap at 1 cost. Good for decks that want to dig for specific cards.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex113",
        "name": "Star Wars Unlimited Showdown",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 2 LP. If you control a People with the Gamer or Pop Culture tag, draw 1 card."}
        ],
        "flavorText": "In a galaxy far, far away... well, actually it's right here in the tournament area.",
        "artNotes": "Players in an intense card game match, Star Wars imagery and cards spread on the table.",
        "image": "",
        "tags": ["Convention", "Gamer", "Pop Culture"],
        "localConnection": {"type": "event", "name": "Star Wars Unlimited Constructed", "description": "Star Wars Unlimited card game tournament held Saturday at Excalibur Con"},
        "designerNotes": "Efficient LP Event with conditional draw. 2 LP at 1 cost is good rate. Draw with Gamer/Pop Culture People makes it better. Solid common.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex114",
        "name": "Lorcana League Night",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 2 LP. If you control a Location with the Gamer tag, gain 1 token of your choice from the pool."}
        ],
        "flavorText": "Fairy tales and strategy — who knew Disney characters could be so competitive?",
        "artNotes": "Players at a colorful card game tournament, whimsical card art visible on the table.",
        "image": "",
        "tags": ["Convention", "Gamer", "Pop Culture"],
        "localConnection": {"type": "event", "name": "Lorcana Constructed", "description": "Disney Lorcana card game tournament held Sunday at Excalibur Con"},
        "designerNotes": "LP + conditional resource. 2 LP base, any-type token with Gamer Location. Flexible resource gain is valuable. Good synergy with Tournament Arena.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex115",
        "name": "Cosplay Prejudging",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Choose a People card you control with the Artist tag. It gains +2 LP until end of Winter. Draw 1 card."}
        ],
        "flavorText": "Every seam inspected, every prop examined — this is where craftsmanship speaks.",
        "artNotes": "Close-up of cosplay details being examined by judges, intricate costume work on display.",
        "image": "",
        "tags": ["Convention", "Artist", "Pop Culture"],
        "localConnection": {"type": "event", "name": "Cosplay Prejudging", "description": "Pre-contest judging for cosplay craftsmanship at Split Rock, Excalibur Con"},
        "designerNotes": "Artist buff + cantrip. +2 LP to an Artist is significant. Draw replaces itself. 1 cost for a buff + draw is solid. Pairs with Cosplay Crafter and Cosplay Judge.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex116",
        "name": "Cosplay Contest Finals",
        "type": "Event",
        "rarity": "Rare",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 1, "learning": 0},
        "totalCost": 2,
        "abilities": [
            {"trigger": "played", "text": "Gain 2 LP for each People card you control with the Artist tag (maximum 8 LP). Each Artist-tagged People gains +1 LP until end of Winter."}
        ],
        "flavorText": "The lights, the music, the crowd — and one unforgettable walk across the stage.",
        "artNotes": "Spectacular cosplay contest on stage, spotlight on a winner, cheering crowd, confetti.",
        "image": "",
        "tags": ["Convention", "Artist", "Pop Culture", "Ceremony"],
        "localConnection": {"type": "event", "name": "Cosplay Contest", "description": "Main cosplay competition held at 5 PM both days on the Split Rock stage at Excalibur Con"},
        "designerNotes": "Big Artist payoff Event. 2 LP per Artist (max 8) is the highest LP potential in the set — but needs 4 Artists for max value. Also buffs all Artists. Build-around Rare.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex117",
        "name": "Celebrity One Shot",
        "type": "Event",
        "rarity": "Rare",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 1},
        "totalCost": 2,
        "abilities": [
            {"trigger": "played", "text": "If you control a Guest-tagged People, gain 5 LP and draw 2 cards. Otherwise, gain 2 LP and draw 1 card."}
        ],
        "flavorText": "The voice actor picked up the dice and said 'I cast fireball.' The crowd lost it.",
        "artNotes": "Celebrity and fans playing an RPG together at a special table, excitement and laughter.",
        "image": "",
        "tags": ["Convention", "Guest", "Gamer"],
        "localConnection": {"type": "event", "name": "Celebrity One Shot", "description": "Special evening RPG session where celebrity guests play D&D with fans at Excalibur Con"},
        "designerNotes": "Guest payoff Event. With Guest: 5 LP + 2 cards is excellent for 2 cost. Without: 2 LP + 1 draw is baseline. Rewards having a Guest on board. Rare because of the high ceiling.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex118",
        "name": "Nerd Nite Live",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Both players draw 2 cards. You gain 2 LP."}
        ],
        "flavorText": "Five minutes on parasitic wasps. Five minutes on retro game design. Somehow both were riveting.",
        "artNotes": "Lively presentation event, speaker with funny slides, audience laughing and engaged.",
        "image": "",
        "tags": ["Convention", "Learning", "Community"],
        "localConnection": {"type": "event", "name": "Nerd Nite", "description": "Community speaker series with short fun presentations on nerdy topics, both days at Excalibur Con"},
        "designerNotes": "Generous shared draw (2 each) + LP for you. Helps both players but you get the LP bonus. Good in any deck, especially Event-heavy builds.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex119",
        "name": "Fandom & Mental Health",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 1, "community": 0, "expression": 0, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 2 LP. Choose a People card you control — it cannot be affected by your opponent's abilities until end of Winter."}
        ],
        "flavorText": "It's okay to love something deeply. It's also okay to take a break from it.",
        "artNotes": "Warm panel discussion about mental health and fandom, supportive audience, safe space.",
        "image": "",
        "tags": ["Convention", "Self-Care", "Community"],
        "localConnection": {"type": "event", "name": "Fandom & Mental Health Panel", "description": "Panel exploring the intersection of fandom passion and mental wellness at Excalibur Con"},
        "designerNotes": "LP + protection. 2 LP plus shielding a People from opponent effects is both thematic and practical. Sustainability cost fits the self-care theme.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex120",
        "name": "Dylan's Drink & Draw",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 0, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Both players draw 1 card. Each player with an Artist-tagged People gains 2 LP."}
        ],
        "flavorText": "Pencils, pints, and the kind of conversation that only happens when everyone's creating.",
        "artNotes": "Casual social art event, people sketching and chatting over drinks, friendly atmosphere.",
        "image": "",
        "tags": ["Convention", "Artist", "Social"],
        "localConnection": {"type": "event", "name": "Dylan's Drink & Draw", "description": "Social art event hosted by Dylan Jacobson at Excalibur Con"},
        "designerNotes": "Shared benefit Event. Both draw. Both can get LP if they have Artists. Truly community-oriented. The opponent benefits too, which fits Dylan's generous nature.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex121",
        "name": "Creative Anachronism",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 1 LP. Choose a People you control — it gains the Artist tag and +1 LP until end of Winter."}
        ],
        "flavorText": "Medieval calligraphy meets modern fandom. The quill is mightier than you think.",
        "artNotes": "Historical arts demonstration, calligraphy and medieval crafts, participants learning techniques.",
        "image": "",
        "tags": ["Convention", "Artist", "Learning"],
        "localConnection": {"type": "event", "name": "Creative Anachronism", "description": "Historical arts and crafts activity held both days at Excalibur Con"},
        "designerNotes": "Tag-granting Event. Gives Artist tag + LP to a People. Combos with Artist synergy cards. 1 LP base plus the buff. Cheap and versatile.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex122",
        "name": "Princess Party",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 0, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 2 LP. If you control a People with the Youth tag, gain 3 LP instead and draw 1 card."}
        ],
        "flavorText": "Every kid in the room was royalty for an afternoon.",
        "artNotes": "Kids in princess and fantasy costumes at a party, face painting, decorations, pure joy.",
        "image": "",
        "tags": ["Convention", "Youth", "Community"],
        "localConnection": {"type": "event", "name": "Princess Party", "description": "Family-friendly princess party event on Sunday at Excalibur Con"},
        "designerNotes": "Youth synergy Event. 2 LP base, 3 LP + draw with Youth People. Good rate for 1 cost. Supports the Youth/Community archetype.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex123",
        "name": "KPop Demon Hunters Screening",
        "type": "Event",
        "rarity": "Uncommon",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 3 LP. Each opponent also gains 1 LP. Draw 1 card."}
        ],
        "flavorText": "A haunted house, a K-pop soundtrack, and an audience that screamed in two languages.",
        "artNotes": "Movie screening in a darkened room, audience reacting with excitement, colorful film on screen.",
        "image": "",
        "tags": ["Convention", "Pop Culture", "Social"],
        "localConnection": {"type": "event", "name": "KPop Demon Hunters Screening", "description": "Special movie screening hosted by Marcus Theaters at Excalibur Con"},
        "designerNotes": "High LP but gives opponent 1 LP. 3 net LP + draw at 1 cost is pushed — the opponent benefit balances it. Thematic: movies are shared experiences.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex124",
        "name": "Man with a Mania Premiere",
        "type": "Event",
        "rarity": "Uncommon",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 1, "learning": 0},
        "totalCost": 2,
        "abilities": [
            {"trigger": "played", "text": "Gain 3 LP. If you control Keith Hopkins, gain 5 LP instead. All People you control with the Duluth tag gain +1 LP until end of Winter."}
        ],
        "flavorText": "A Minnesota story, a Minnesota premiere, a standing ovation from a Minnesota crowd.",
        "artNotes": "Film premiere at a convention, filmmaker on stage, audience giving a standing ovation.",
        "image": "",
        "tags": ["Convention", "Pop Culture", "Duluth"],
        "localConnection": {"type": "event", "name": "Man with a Mania Premiere", "description": "Minnesota premiere of Keith Hopkins' film at Excalibur Con 2026"},
        "designerNotes": "Named character combo. 3 LP base, 5 LP with Keith Hopkins. Duluth People buff adds value in Location/Duluth decks. 2 cost for high conditional LP.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex125",
        "name": "Improv Night",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 1 LP. Both players discard 1 card and draw 2 cards."}
        ],
        "flavorText": "Yes, and... the entire front row was crying from laughter by the end.",
        "artNotes": "Improv comedy show late at night, performers on stage, audience doubled over laughing.",
        "image": "",
        "tags": ["Convention", "Social", "Pop Culture"],
        "localConnection": {"type": "event", "name": "Improv Night", "description": "Late-night improv comedy show on Saturday at Excalibur Con"},
        "designerNotes": "Card cycling Event. Both discard 1 / draw 2. Net +1 card each. You get LP. Helps dig through decks. Good in combo-oriented builds.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex126",
        "name": "LARP Battle",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 2 LP. Your opponent loses 1 LP (minimum 0). If you control a People with the Gamer tag, draw 1 card."}
        ],
        "flavorText": "Foam swords at dawn. Well, foam swords at 4:30 PM, but the drama was real.",
        "artNotes": "Live action roleplay battle with foam weapons, participants in costume, cheering spectators.",
        "image": "",
        "tags": ["Convention", "Gamer", "Pop Culture"],
        "localConnection": {"type": "event", "name": "LARP Session", "description": "Live action roleplay session at Excalibur Con"},
        "designerNotes": "Aggressive Event. 2 LP gain + 1 LP loss for opponent = 3 LP swing. Conditional draw. One of the few cards that directly reduces opponent LP.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex127",
        "name": "Silent Auction Bid",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 1, "sustainability": 0, "community": 0, "expression": 0, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Return 1 token you control to the pool. Gain 3 LP and draw 1 card."}
        ],
        "flavorText": "She scribbled a higher bid and walked away whistling. The sword replica was hers.",
        "artNotes": "Silent auction table with bid sheets, collectibles on display, someone writing a bid sneakily.",
        "image": "",
        "tags": ["Convention", "Community", "Gathering"],
        "localConnection": {"type": "event", "name": "Silent Auction", "description": "Fundraising silent auction in Edmund Fitzgerald Hall at Excalibur Con"},
        "designerNotes": "Resource conversion. Spend 1 Growth + return any 1 token for 3 LP + draw. Net -2 tokens for 3 LP and a card. Good when you have excess tokens. Auction flavor.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex128",
        "name": "VIP Early Entry",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 1, "sustainability": 0, "community": 0, "expression": 0, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Draw 3 cards, then discard 1. Gain 1 LP."}
        ],
        "flavorText": "Thirty minutes before the doors open. The aisles are empty, the merch is untouched. Heaven.",
        "artNotes": "Early morning entry, VIP badge holder walking into an empty convention hall, pristine vendor booths.",
        "image": "",
        "tags": ["Convention", "Gathering", "Community"],
        "localConnection": {"type": "feature", "name": "VIP Early Entry", "description": "VIP ticket holders enter 30 minutes early at 10:30 AM at Excalibur Con"},
        "designerNotes": "Premium draw Event. Draw 3 / discard 1 = net +2 cards, plus 1 LP. Strong for 1 cost. Growth cost is the premium (VIP costs money).",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex129",
        "name": "Superhero U Workshop",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Choose a People you control. It gains +2 LP until end of Winter. If you control Andrew Gray, it gains +3 LP instead."}
        ],
        "flavorText": "Lesson one: heroes aren't born. They're trained. Now drop and give me twenty!",
        "artNotes": "Workshop where a confident instructor teaches hero poses and confidence to participants.",
        "image": "",
        "tags": ["Convention", "Guest", "Pop Culture"],
        "localConnection": {"type": "event", "name": "Superhero U", "description": "Workshop run by Andrew Gray (Power Rangers) teaching confidence and heroism at Excalibur Con"},
        "designerNotes": "People buff Event. +2 LP (or +3 with Andrew Gray). Clean and efficient. Named character combo adds deckbuilding interest. 1 cost for a big buff.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex130",
        "name": "Common House Bard",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 1, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 1 LP. All People you control gain +1 LP until end of Winter."}
        ],
        "flavorText": "A lute, a voice, and an audience that forgot they were in a convention center.",
        "artNotes": "Bard performing music in a fantasy-themed corner of the convention, enchanted listeners.",
        "image": "",
        "tags": ["Convention", "Social", "Artist"],
        "localConnection": {"type": "event", "name": "Common House Bard", "description": "Live musical performance held both days at Excalibur Con"},
        "designerNotes": "Board-wide buff Event. +1 LP to all People is strong with a wide board. 1 LP base too. Cheap at 1 cost. Best in People-heavy decks.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex131",
        "name": "Philosophy of D&D Panel",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Draw 2 cards. If you control a People with the Gamer or Learning tag, gain 1 LP."}
        ],
        "flavorText": "Is the alignment chart a moral framework? Discuss. You have five minutes.",
        "artNotes": "Thoughtful panel discussion about roleplaying games and philosophy, engaged audience.",
        "image": "",
        "tags": ["Convention", "Learning", "Gamer"],
        "localConnection": {"type": "event", "name": "Philosophy of D&D", "description": "Panel exploring philosophical themes in tabletop RPGs, Sunday at Excalibur Con"},
        "designerNotes": "Draw 2 with conditional LP. Solid card advantage at 1 cost. Gamer/Learning tag condition is easy to meet. Dependable common.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex132",
        "name": "Neurodiversity 101",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 1, "community": 0, "expression": 0, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 2 LP. If you control a Location with the Self-Care or Community tag, gain 3 LP instead."}
        ],
        "flavorText": "Understanding starts with listening. The room was very, very good at listening.",
        "artNotes": "Inclusive panel discussion about neurodiversity, attentive diverse audience, warm lighting.",
        "image": "",
        "tags": ["Convention", "Self-Care", "Community"],
        "localConnection": {"type": "event", "name": "Neurodiversity 101 Panel", "description": "Panel on neurodiversity awareness and inclusion, Sunday at Excalibur Con"},
        "designerNotes": "Self-Care archetype support. 2 LP base, 3 LP with Self-Care/Community Location. Sustainability cost is thematic. Good with Sensory Sanctuary.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex133",
        "name": "Local Game Dev Showcase",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 0, "expression": 0, "learning": 1},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 1 LP. Look at the top 4 cards of your deck. Keep 1, put the rest back in any order."}
        ],
        "flavorText": "Two people, one laptop, and a game that had everyone downloading the demo on the spot.",
        "artNotes": "Indie game developers showing their game at a booth, players gathered around screens.",
        "image": "",
        "tags": ["Convention", "Gamer", "Duluth"],
        "localConnection": {"type": "event", "name": "Local Game Developers Panel", "description": "Panel showcasing local game developers at Excalibur Con"},
        "designerNotes": "Deep card selection. Look at 4, keep 1 is very good for finding specific cards. 1 LP + card selection at 1 cost is efficient.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex134",
        "name": "Oaken Hollow Demo",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 1, "community": 0, "expression": 0, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 2 LP. You may return 1 Sustainability token to the pool to draw 2 cards."}
        ],
        "flavorText": "Tiny wooden gears, hand-carved joints — sometimes the old ways are the best ways.",
        "artNotes": "Woodworking and crafting demonstration, intricate wooden creations on display, fascinated onlookers.",
        "image": "",
        "tags": ["Convention", "Artist", "Sustainability"],
        "localConnection": {"type": "event", "name": "Oaken Hollow Demos", "description": "Crafting demonstrations and workshops by Oaken Hollow at Excalibur Con"},
        "designerNotes": "LP + optional draw. 2 LP guaranteed. Can spend an extra Sustainability for 2 cards. Flexible — take the LP or invest for cards. Sustainability theme.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex135",
        "name": "Sponsor Spotlight",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 1, "sustainability": 0, "community": 0, "expression": 0, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "Gain 2 tokens of your choice from the pool (may be different types). Gain 1 LP."}
        ],
        "flavorText": "Level Up, Collectors Connection, Radisson — every sponsor made this con possible.",
        "artNotes": "Sponsor banners and logos displayed prominently, appreciation ceremony moment.",
        "image": "",
        "tags": ["Convention", "Community", "Vendor"],
        "localConnection": {"type": "feature", "name": "Convention Sponsors", "description": "Major sponsors including Level Up, Collectors Connection, Radisson, and many more supporting Excalibur Con"},
        "designerNotes": "Resource generation Event. 2 flexible tokens + 1 LP for 1 Growth. Net +1 token + 1 LP. The flexibility of choosing any types is very valuable for multi-resource decks.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex136",
        "name": "Con Badge Trade",
        "type": "Event",
        "rarity": "Common",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 0, "learning": 0},
        "totalCost": 1,
        "abilities": [
            {"trigger": "played", "text": "You and your opponent each draw 1 card. You gain 2 LP. Your opponent gains 1 LP."}
        ],
        "flavorText": "Ribbons, pins, and the sacred art of the lanyard swap.",
        "artNotes": "Two attendees excitedly trading badge ribbons and pins, lanyards covered in collectibles.",
        "image": "",
        "tags": ["Convention", "Community", "Social"],
        "localConnection": {"type": "feature", "name": "Badge Ribbons and Trading", "description": "Attendee tradition of collecting and trading badge ribbons at Excalibur Con"},
        "designerNotes": "Social interaction Event. Both draw, both gain LP (you more). Shared benefit fits the trading theme. Community cost is appropriate. Solid role-player.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
    {
        "id": "card_ex137",
        "name": "Closing Ceremony",
        "type": "Event",
        "rarity": "Uncommon",
        "lp": 0,
        "set": "Excalibur Con 2026",
        "cost": {"growth": 0, "sustainability": 0, "community": 1, "expression": 1, "learning": 0},
        "totalCost": 2,
        "abilities": [
            {"trigger": "played", "text": "Gain 1 LP for each unique tag among cards you control (maximum 6 LP). Draw 1 card."}
        ],
        "flavorText": "See you next year, Duluth. Same place, same magic, whole new memories.",
        "artNotes": "Emotional closing moment on stage, committee waving to cheering crowd, convention banners.",
        "image": "",
        "tags": ["Convention", "Community", "Ceremony"],
        "localConnection": {"type": "event", "name": "Excalibur Con Committee Panel", "description": "Closing panel and ceremony wrapping up the convention"},
        "designerNotes": "Diversity payoff. LP scales with unique tags you control — rewards a varied board. Max 6 LP at 2 cost is excellent if you hit it. Build diverse boards.",
        "created": "2026-03-09T00:00:00Z",
        "modified": "2026-03-09T00:00:00Z"
    },
]


# ============================================================
# THIRD PRE-CON DECK: "Excalibur Experience"
# ============================================================

THIRD_DECK = {
    "name": "Excalibur Experience",
    "description": "Guest-heavy, Event-driven, con-themed burst. Expression (Red) + Community (White), splash Learning.",
    "strategy": "Deploy celebrity Guests backed by convention Locations. Fire off convention Events for burst LP. Celebrity Handler and Split Rock Stage discount and buff Guests. Celebrity One Shot and Cosplay Contest Finals are your big finishers. Win through high LP Events and Guest synergy.",
    "primaryResources": ["expression", "community"],
    "secondaryResources": ["learning"],
    "keyTags": ["Convention", "Guest", "Pop Culture", "Artist"],
    "cards": [
        # People (14)
        "card_ex78",   # SungWon Cho (Legendary)
        "card_ex79",   # Marissa Lenti
        "card_ex80",   # Andrew Gray
        "card_ex81",   # Christina Masterson
        "card_ex82",   # Elle Firespray
        "card_ex84",   # Dylan Jacobson
        "card_ex86",   # Dave Sabik
        "card_ex88",   # Cosplay Judge
        "card_ex89",   # Volunteer Coordinator
        "card_ex91",   # 501st Legionnaire
        "card_ex92",   # Nerd Nite Presenter
        "card_ex95",   # Celebrity Handler
        "card_ex96",   # Keith Hopkins
        "card_ex01",   # Cosplay Crafter (from original set)
        # Locations (8)
        "card_ex100",  # Split Rock Stage
        "card_ex101",  # French River Panels
        "card_ex107",  # Gooseberry Workshop
        "card_ex99",   # Edmund Fitzgerald Hall
        "card_ex108",  # Celebrity Green Room
        "card_ex109",  # DPW Wrestling Ring
        "card_ex103",  # Tournament Arena
        "card_ex105",  # Lake Superior Ballroom
        # Events (14)
        "card_ex116",  # Cosplay Contest Finals (Rare)
        "card_ex117",  # Celebrity One Shot (Rare)
        "card_ex115",  # Cosplay Prejudging
        "card_ex118",  # Nerd Nite Live
        "card_ex120",  # Dylan's Drink & Draw
        "card_ex121",  # Creative Anachronism
        "card_ex123",  # KPop Demon Hunters Screening
        "card_ex124",  # Man with a Mania Premiere
        "card_ex125",  # Improv Night
        "card_ex129",  # Superhero U Workshop
        "card_ex130",  # Common House Bard
        "card_ex136",  # Con Badge Trade
        "card_ex113",  # Star Wars Unlimited Showdown
        "card_ex137",  # Closing Ceremony
    ],
    "cardCount": 36,
    "typeSplit": {
        "People": 14,
        "Location": 8,
        "Event": 14
    }
}


def main():
    # Load existing cards
    cards_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cards.json')
    with open(cards_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_count = len(data['cards'])
    print(f"Existing cards: {existing_count}")

    # Validate no duplicate IDs
    existing_ids = {c['id'] for c in data['cards']}
    new_ids = {c['id'] for c in NEW_CARDS}
    dupes = existing_ids & new_ids
    if dupes:
        print(f"ERROR: Duplicate IDs: {dupes}")
        return

    # Add new cards
    data['cards'].extend(NEW_CARDS)
    data['meta']['lastModified'] = '2026-03-09'

    new_count = len(data['cards'])
    print(f"New total: {new_count} (+{new_count - existing_count})")

    # Type/rarity breakdown of new cards
    types = {}
    rarities = {}
    for c in NEW_CARDS:
        types[c['type']] = types.get(c['type'], 0) + 1
        rarities[c['rarity']] = rarities.get(c['rarity'], 0) + 1
    print(f"New card types: {types}")
    print(f"New card rarities: {rarities}")

    # Write updated cards
    with open(cards_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {cards_path}")

    # Update starter decks
    decks_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'starter-decks.json')
    with open(decks_path, 'r', encoding='utf-8') as f:
        deck_data = json.load(f)

    # Add third deck
    deck_data['decks'].append(THIRD_DECK)

    # Update meta
    deck_data['meta']['description'] = (
        "Three starter decks for the Excalibur Con 2026 set. "
        "Convention Life (36 cards), Duluth Spirit (36 cards), and Excalibur Experience (36 cards)."
    )

    # Update unbound cards — add new unbound cards (not in any deck)
    all_deck_cards = set()
    for deck in deck_data['decks']:
        all_deck_cards.update(deck['cards'])

    all_card_ids = {c['id'] for c in data['cards']}
    unbound = sorted(all_card_ids - all_deck_cards)
    deck_data['unboundCards']['cards'] = unbound
    deck_data['unboundCards']['notes'] = (
        f"{len(unbound)} cards not assigned to any starter deck. "
        "Available for custom deckbuilding."
    )

    with open(decks_path, 'w', encoding='utf-8') as f:
        json.dump(deck_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {decks_path}")
    print(f"Third deck: {THIRD_DECK['name']} ({THIRD_DECK['cardCount']} cards)")
    print(f"Unbound cards: {len(unbound)}")

    # Validate third deck card count
    assert len(THIRD_DECK['cards']) == THIRD_DECK['cardCount'], \
        f"Deck card count mismatch: {len(THIRD_DECK['cards'])} != {THIRD_DECK['cardCount']}"

    # Validate all deck cards exist
    for card_id in THIRD_DECK['cards']:
        assert card_id in all_card_ids, f"Deck card {card_id} not in card database!"

    print("All validations passed!")


if __name__ == '__main__':
    main()
