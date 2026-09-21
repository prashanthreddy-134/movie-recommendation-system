import csv
from pathlib import Path


movies = [
    [
        "Baahubali: The Beginning",
        "Telugu",
        "Action|Adventure|Drama",
        "epic kingdom warrior battle royal family revenge",
        "A young man discovers his royal heritage and becomes involved in a battle for a kingdom.",
        8.0
    ],
    [
        "Baahubali 2: The Conclusion",
        "Telugu",
        "Action|Adventure|Drama",
        "kingdom warrior revenge family empire battle",
        "A royal heir fights to reclaim the kingdom and uncover the truth behind his father's death.",
        8.2
    ],
    [
        "RRR",
        "Telugu",
        "Action|Drama|Historical",
        "freedom fighters friendship revolution british india action",
        "Two legendary revolutionaries form a powerful friendship while fighting British rule.",
        7.9
    ],
    [
        "Pushpa: The Rise",
        "Telugu",
        "Action|Crime|Drama",
        "red sandalwood smuggling forest worker crime ambition",
        "A determined laborer rises through a red sandalwood smuggling syndicate.",
        7.6
    ],
    [
        "Pushpa 2: The Rule",
        "Telugu",
        "Action|Crime|Drama",
        "smuggling power politics revenge police forest ambition",
        "Pushpa faces powerful enemies while expanding his influence in the smuggling world.",
        8.0
    ],
    [
        "Arjun Reddy",
        "Telugu",
        "Drama|Romance",
        "medical college love anger addiction relationship intense",
        "A brilliant but troubled surgeon struggles with love, anger and self-destruction.",
        8.1
    ],
    [
        "Jersey",
        "Telugu",
        "Drama|Sport",
        "cricket father son comeback ambition family emotional",
        "A former cricketer attempts a late comeback to fulfill his dream and support his son.",
        8.5
    ],
    [
        "Eega",
        "Telugu",
        "Action|Fantasy|Romance",
        "revenge reincarnation fly fantasy love villain",
        "A murdered man is reincarnated as a fly and seeks revenge while protecting his loved one.",
        7.7
    ],
    [
        "Ala Vaikunthapurramuloo",
        "Telugu",
        "Action|Drama|Comedy",
        "family identity inheritance comedy music wealthy rivalry",
        "A young man discovers a hidden family truth that changes his life.",
        7.3
    ],
    [
        "Rangasthalam",
        "Telugu",
        "Action|Drama|Period",
        "village politics revenge brother election rural corruption",
        "A hearing-impaired villager challenges a powerful local political system.",
        8.4
    ],
    [
        "Mahanati",
        "Telugu",
        "Biography|Drama",
        "actress cinema biography fame love tragedy classic film",
        "A biographical drama about the rise and struggles of a celebrated Indian actress.",
        8.5
    ],
    [
        "Agent Sai Srinivasa Athreya",
        "Telugu",
        "Crime|Mystery|Comedy",
        "detective investigation mystery railway crime clues",
        "An enthusiastic detective investigates a mysterious case involving unidentified bodies.",
        8.4
    ],
    [
        "Goodachari",
        "Telugu",
        "Action|Spy|Thriller",
        "spy intelligence mission conspiracy secret agent action",
        "A secret agent becomes trapped in an international conspiracy.",
        8.0
    ],
    [
        "Kshanam",
        "Telugu",
        "Mystery|Thriller",
        "missing child investigation suspense relationship clues",
        "A man helps his former lover search for a missing child while uncovering a mystery.",
        8.2
    ],
    [
        "HIT: The First Case",
        "Telugu",
        "Crime|Mystery|Thriller",
        "police investigation missing woman serial crime detective",
        "A police officer investigates the disappearance of a young woman.",
        7.7
    ],
    [
        "Jathi Ratnalu",
        "Telugu",
        "Comedy",
        "friends city politics confusion humor friendship",
        "Three naive friends move to the city and become entangled in an unexpected political situation.",
        7.9
    ],
    [
        "Pelli Choopulu",
        "Telugu",
        "Comedy|Romance|Drama",
        "startup food business love friendship entrepreneurship",
        "Two young people meet through an arranged marriage setup and build a food business together.",
        8.2
    ],
    [
        "C/O Kancharapalem",
        "Telugu",
        "Drama|Romance",
        "small town relationships love community human stories",
        "Multiple interconnected love stories unfold in a small-town community.",
        8.8
    ],
    [
        "Sita Ramam",
        "Telugu",
        "Romance|Drama|Mystery",
        "letters love army soldier palace mystery historical",
        "A mysterious letter leads to a romantic story involving an army lieutenant.",
        8.6
    ],
    [
        "Hi Nanna",
        "Telugu",
        "Drama|Romance|Family",
        "father daughter memory love family emotional photography",
        "A father and daughter confront the mysteries of their past and family.",
        8.0
    ],
    [
        "Dasara",
        "Telugu",
        "Action|Drama",
        "village coal mines friendship revenge politics alcohol",
        "A rural friendship story turns into a struggle involving power, revenge and politics.",
        7.6
    ],
    [
        "Major",
        "Telugu",
        "Biography|Action|Drama",
        "soldier army biography mumbai attacks patriotism sacrifice",
        "A biographical drama portraying the life and sacrifice of an Indian Army officer.",
        8.1
    ],

    # KANNADA MOVIES

    [
        "Kantara",
        "Kannada",
        "Action|Drama|Mystery",
        "village forest folklore tradition deity land conflict",
        "A village faces a conflict involving land, tradition, folklore and the forest.",
        8.6
    ],
    [
        "KGF: Chapter 1",
        "Kannada",
        "Action|Crime|Drama",
        "gold mines gangster power ambition poverty underworld",
        "A determined man rises from poverty to become a powerful figure in the gold-mining underworld.",
        8.2
    ],
    [
        "KGF: Chapter 2",
        "Kannada",
        "Action|Crime|Drama",
        "gold mines gangster empire revenge power politics",
        "Rocky consolidates his empire while facing political and criminal enemies.",
        8.3
    ],
    [
        "777 Charlie",
        "Kannada",
        "Adventure|Drama",
        "dog friendship journey healing loneliness animal road trip",
        "A lonely man forms a deep bond with a dog and embarks on a transformative journey.",
        8.8
    ],
    [
        "Kirik Party",
        "Kannada",
        "Comedy|Romance|Drama",
        "college friendship youth engineering campus love",
        "A college student's life changes through friendship, love and growing up.",
        8.0
    ],
    [
        "Garuda Gamana Vrishabha Vahana",
        "Kannada",
        "Crime|Drama",
        "friends crime coastal rivalry violence power",
        "Two childhood friends rise through a violent criminal world and face a dangerous rivalry.",
        8.1
    ],
    [
        "Ulidavaru Kandanthe",
        "Kannada",
        "Crime|Drama|Mystery",
        "coastal crime multiple perspectives fishing mystery gangsters",
        "A complex crime story is told through multiple perspectives in coastal Karnataka.",
        8.4
    ],
    [
        "Avane Srimannarayana",
        "Kannada",
        "Adventure|Comedy|Fantasy",
        "detective treasure village mystery humor adventure",
        "A quirky police officer investigates a treasure mystery in a fictional town.",
        8.0
    ],
    [
        "Kavaludaari",
        "Kannada",
        "Crime|Mystery|Thriller",
        "police cold case investigation bodies mystery secrets",
        "A traffic police officer investigates a decades-old murder mystery.",
        8.0
    ],
    [
        "Gantumoote",
        "Kannada",
        "Drama|Romance",
        "school friendship teenage love growing up memories",
        "A coming-of-age story about teenage love, friendship and school life.",
        8.1
    ],
    [
        "Dia",
        "Kannada",
        "Romance|Drama",
        "love relationships heartbreak emotional college destiny",
        "A young woman's life changes through love, loss and unexpected relationships.",
        8.0
    ],
    [
        "Sapta Sagaradaache Ello: Side A",
        "Kannada",
        "Romance|Drama",
        "love prison separation dreams emotional relationship",
        "A romantic drama about love, separation and the consequences of a life-changing decision.",
        8.0
    ],
    [
        "Sapta Sagaradaache Ello: Side B",
        "Kannada",
        "Romance|Drama",
        "second chance love separation healing emotional",
        "A man attempts to rebuild his life and confront the memories of a lost relationship.",
        8.2
    ],
    [
        "Lucia",
        "Kannada",
        "Mystery|Psychological|Thriller",
        "dream reality insomnia cinema identity psychological mystery",
        "A projectionist experiences a mysterious pill that blurs the boundary between dreams and reality.",
        8.3
    ],
    [
        "RangiTaranga",
        "Kannada",
        "Mystery|Thriller|Drama",
        "village house secrets investigation supernatural suspense",
        "A couple visiting a remote village become involved in a mystery surrounding an old house.",
        8.1
    ],
    [
        "Bell Bottom",
        "Kannada",
        "Comedy|Crime|Mystery",
        "detective police robbery investigation retro humor",
        "A clever police detective investigates a series of unusual robberies.",
        7.4
    ]
]


# --------------------------------------------------
# Create data directory
# --------------------------------------------------

data_folder = Path(__file__).parent / "data"
data_folder.mkdir(exist_ok=True)


csv_file = data_folder / "movies.csv"


# --------------------------------------------------
# Write dataset
# --------------------------------------------------

with open(
    csv_file,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "title",
        "language",
        "genres",
        "keywords",
        "description",
        "rating"
    ])

    writer.writerows(movies)


print("======================================")
print("Movie dataset created successfully!")
print("======================================")
print(f"Total movies: {len(movies)}")
print("Telugu + Kannada movies only")
print(f"Dataset location: {csv_file}")