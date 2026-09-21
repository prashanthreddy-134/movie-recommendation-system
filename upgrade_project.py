from pathlib import Path
import csv

# ============================================================
# PROJECT UPGRADE SCRIPT
# Telugu + Kannada Movie Recommendation System
# ============================================================

PROJECT_DIR = Path(__file__).parent
DATA_DIR = PROJECT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

CSV_FILE = DATA_DIR / "movies.csv"


# ============================================================
# MOVIE DATA
# ============================================================

movies = [

    # ---------------------- TELUGU ----------------------

    {
        "title": "RRR",
        "language": "Telugu",
        "year": 2022,
        "genres": "Action|Drama|Historical",
        "rating": 7.9,
        "director": "S. S. Rajamouli",
        "cast": "N. T. Rama Rao Jr.|Ram Charan|Alia Bhatt|Ajay Devgn",
        "keywords": "freedom fighters friendship revolution british india action brotherhood sacrifice",
        "description": "Two legendary revolutionaries form a powerful friendship while fighting British rule in colonial India."
    },

    {
        "title": "Baahubali: The Beginning",
        "language": "Telugu",
        "year": 2015,
        "genres": "Action|Adventure|Drama",
        "rating": 8.0,
        "director": "S. S. Rajamouli",
        "cast": "Prabhas|Rana Daggubati|Anushka Shetty|Tamannaah Bhatia",
        "keywords": "kingdom warrior battle royal family revenge empire courage",
        "description": "A young man discovers his royal heritage and becomes involved in a battle for a powerful kingdom."
    },

    {
        "title": "Baahubali 2: The Conclusion",
        "language": "Telugu",
        "year": 2017,
        "genres": "Action|Adventure|Drama",
        "rating": 8.2,
        "director": "S. S. Rajamouli",
        "cast": "Prabhas|Rana Daggubati|Anushka Shetty|Sathyaraj",
        "keywords": "kingdom warrior revenge royal family empire battle betrayal",
        "description": "A royal heir fights to reclaim the kingdom and uncover the truth behind his father's death."
    },

    {
        "title": "Pushpa: The Rise",
        "language": "Telugu",
        "year": 2021,
        "genres": "Action|Crime|Drama",
        "rating": 7.6,
        "director": "Sukumar",
        "cast": "Allu Arjun|Rashmika Mandanna|Fahadh Faasil",
        "keywords": "red sandalwood smuggling forest worker crime ambition gangster power",
        "description": "A determined laborer rises through a red sandalwood smuggling syndicate and challenges powerful enemies."
    },

    {
        "title": "Pushpa 2: The Rule",
        "language": "Telugu",
        "year": 2024,
        "genres": "Action|Crime|Drama",
        "rating": 8.0,
        "director": "Sukumar",
        "cast": "Allu Arjun|Rashmika Mandanna|Fahadh Faasil",
        "keywords": "smuggling power politics revenge police forest gangster empire ambition",
        "description": "Pushpa expands his influence while facing powerful political and criminal enemies."
    },

    {
        "title": "Arjun Reddy",
        "language": "Telugu",
        "year": 2017,
        "genres": "Drama|Romance",
        "rating": 8.1,
        "director": "Sandeep Reddy Vanga",
        "cast": "Vijay Deverakonda|Shalini Pandey|Rahul Ramakrishna",
        "keywords": "medical college doctor love anger addiction relationship heartbreak intense",
        "description": "A brilliant but troubled surgeon struggles with love, anger, addiction and self-destruction."
    },

    {
        "title": "Jersey",
        "language": "Telugu",
        "year": 2019,
        "genres": "Drama|Sport",
        "rating": 8.5,
        "director": "Gowtam Tinnanuri",
        "cast": "Nani|Shraddha Srinath|Ronan Smith",
        "keywords": "cricket father son comeback ambition family sports emotional dream",
        "description": "A former cricketer attempts a late comeback to fulfill his dream and support his son."
    },

    {
        "title": "Eega",
        "language": "Telugu",
        "year": 2012,
        "genres": "Action|Fantasy|Romance",
        "rating": 7.7,
        "director": "S. S. Rajamouli",
        "cast": "Nani|Samantha Ruth Prabhu|Sudeep",
        "keywords": "revenge reincarnation fly fantasy love villain supernatural transformation",
        "description": "A murdered man is reincarnated as a fly and seeks revenge while protecting his loved one."
    },

    {
        "title": "Ala Vaikunthapurramuloo",
        "language": "Telugu",
        "year": 2020,
        "genres": "Action|Drama|Comedy",
        "rating": 7.3,
        "director": "Trivikram Srinivas",
        "cast": "Allu Arjun|Pooja Hegde|Tabu|Jayaram",
        "keywords": "family identity inheritance wealthy rivalry comedy music relationships",
        "description": "A young man discovers a hidden family truth that changes his life and relationships."
    },

    {
        "title": "Rangasthalam",
        "language": "Telugu",
        "year": 2018,
        "genres": "Action|Drama|Period",
        "rating": 8.4,
        "director": "Sukumar",
        "cast": "Ram Charan|Samantha Ruth Prabhu|Aadhi Pinisetty|Jagapathi Babu",
        "keywords": "village politics revenge brother election rural corruption leadership",
        "description": "A hearing-impaired villager challenges a powerful political system controlling his village."
    },

    {
        "title": "Mahanati",
        "language": "Telugu",
        "year": 2018,
        "genres": "Biography|Drama",
        "rating": 8.5,
        "director": "Nag Ashwin",
        "cast": "Keerthy Suresh|Dulquer Salmaan|Samantha Ruth Prabhu|Vijay Deverakonda",
        "keywords": "actress cinema biography fame love tragedy classic film career",
        "description": "A biographical drama portraying the rise and struggles of a celebrated Indian actress."
    },

    {
        "title": "Agent Sai Srinivasa Athreya",
        "language": "Telugu",
        "year": 2019,
        "genres": "Crime|Mystery|Comedy",
        "rating": 8.4,
        "director": "Swaroop RSJ",
        "cast": "Naveen Polishetty|Shruti Sharma|Krishna Kanth",
        "keywords": "detective investigation mystery railway crime clues bodies case comedy",
        "description": "An enthusiastic detective investigates a mysterious case involving unidentified bodies."
    },

    {
        "title": "Goodachari",
        "language": "Telugu",
        "year": 2018,
        "genres": "Action|Spy|Thriller",
        "rating": 8.0,
        "director": "Sashi Kiran Tikka",
        "cast": "Adivi Sesh|Sobhita Dhulipala|Jagapathi Babu",
        "keywords": "spy intelligence mission conspiracy secret agent terrorism action",
        "description": "A secret agent becomes trapped in a dangerous international conspiracy."
    },

    {
        "title": "Kshanam",
        "language": "Telugu",
        "year": 2016,
        "genres": "Mystery|Thriller",
        "rating": 8.2,
        "director": "Ravikanth Perepu",
        "cast": "Adivi Sesh|Adah Sharma|Anasuya Bharadwaj",
        "keywords": "missing child investigation suspense relationship clues mystery search",
        "description": "A man helps his former lover search for a missing child while uncovering a mystery."
    },

    {
        "title": "HIT: The First Case",
        "language": "Telugu",
        "year": 2020,
        "genres": "Crime|Mystery|Thriller",
        "rating": 7.7,
        "director": "Sailesh Kolanu",
        "cast": "Vishwak Sen|Ruhani Sharma|Murali Sharma",
        "keywords": "police investigation missing woman crime detective suspense case",
        "description": "A police officer investigates the disappearance of a young woman while dealing with his own struggles."
    },

    {
        "title": "Jathi Ratnalu",
        "language": "Telugu",
        "year": 2021,
        "genres": "Comedy",
        "rating": 7.9,
        "director": "Anudeep KV",
        "cast": "Naveen Polishetty|Priyadarshi|Rahul Ramakrishna|Faria Abdullah",
        "keywords": "friends city politics confusion humor friendship comedy journey",
        "description": "Three naive friends move to the city and become unexpectedly involved in politics."
    },

    {
        "title": "Pelli Choopulu",
        "language": "Telugu",
        "year": 2016,
        "genres": "Comedy|Romance|Drama",
        "rating": 8.2,
        "director": "Tharun Bhascker",
        "cast": "Vijay Deverakonda|Ritu Varma|Priyadarshi",
        "keywords": "startup food business love friendship entrepreneurship marriage youth",
        "description": "Two young people meet through an arranged marriage setup and build a food business together."
    },

    {
        "title": "C/O Kancharapalem",
        "language": "Telugu",
        "year": 2018,
        "genres": "Drama|Romance",
        "rating": 8.8,
        "director": "Venkatesh Maha",
        "cast": "Subba Rao|Radha Bessy|Kesava Karri",
        "keywords": "small town relationships love community human stories romance life",
        "description": "Multiple interconnected love stories unfold within a small-town community."
    },

    {
        "title": "Sita Ramam",
        "language": "Telugu",
        "year": 2022,
        "genres": "Romance|Drama|Mystery",
        "rating": 8.6,
        "director": "Hanu Raghavapudi",
        "cast": "Dulquer Salmaan|Mrunal Thakur|Rashmika Mandanna",
        "keywords": "letters love army soldier palace mystery historical romance",
        "description": "A mysterious letter leads to a romantic story involving an army lieutenant."
    },

    {
        "title": "Hi Nanna",
        "language": "Telugu",
        "year": 2023,
        "genres": "Drama|Romance|Family",
        "rating": 8.0,
        "director": "Shouryuv",
        "cast": "Nani|Mrunal Thakur|Kiara Khanna",
        "keywords": "father daughter memory love family emotional photography relationship",
        "description": "A father and daughter confront the mysteries surrounding their past and family."
    },

    {
        "title": "Dasara",
        "language": "Telugu",
        "year": 2023,
        "genres": "Action|Drama",
        "rating": 7.6,
        "director": "Srikanth Odela",
        "cast": "Nani|Keerthy Suresh|Dheekshith Shetty",
        "keywords": "village coal mines friendship revenge politics rural alcohol power",
        "description": "A rural friendship story becomes a struggle involving power, revenge and politics."
    },

    {
        "title": "Major",
        "language": "Telugu",
        "year": 2022,
        "genres": "Biography|Action|Drama",
        "rating": 8.1,
        "director": "Sashi Kiran Tikka",
        "cast": "Adivi Sesh|Saiee Manjrekar|Sobhita Dhulipala",
        "keywords": "soldier army biography mumbai attacks patriotism sacrifice military",
        "description": "A biographical drama portraying the life and sacrifice of an Indian Army officer."
    },

    # ---------------------- KANNADA ----------------------

    {
        "title": "Kantara",
        "language": "Kannada",
        "year": 2022,
        "genres": "Action|Drama|Mystery",
        "rating": 8.6,
        "director": "Rishab Shetty",
        "cast": "Rishab Shetty|Sapthami Gowda|Kishore|Achyuth Kumar",
        "keywords": "village forest folklore tradition deity land conflict culture ritual",
        "description": "A village faces a conflict involving land, tradition, folklore and the forest."
    },

    {
        "title": "KGF: Chapter 1",
        "language": "Kannada",
        "year": 2018,
        "genres": "Action|Crime|Drama",
        "rating": 8.2,
        "director": "Prashanth Neel",
        "cast": "Yash|Srinidhi Shetty|Ramachandra Raju|Anant Nag",
        "keywords": "gold mines gangster power ambition poverty underworld empire action",
        "description": "A determined man rises from poverty to become a powerful figure in the gold-mining underworld."
    },

    {
        "title": "KGF: Chapter 2",
        "language": "Kannada",
        "year": 2022,
        "genres": "Action|Crime|Drama",
        "rating": 8.3,
        "director": "Prashanth Neel",
        "cast": "Yash|Sanjay Dutt|Srinidhi Shetty|Raveena Tandon",
        "keywords": "gold mines gangster empire revenge power politics underworld action",
        "description": "Rocky consolidates his empire while facing political and criminal enemies."
    },

    {
        "title": "777 Charlie",
        "language": "Kannada",
        "year": 2022,
        "genres": "Adventure|Drama",
        "rating": 8.8,
        "director": "Kiranraj K",
        "cast": "Rakshit Shetty|Sangeetha Sringeri|Raj B. Shetty",
        "keywords": "dog friendship journey healing loneliness animal road trip emotional",
        "description": "A lonely man forms a deep bond with a dog and embarks on a transformative journey."
    },

    {
        "title": "Kirik Party",
        "language": "Kannada",
        "year": 2016,
        "genres": "Comedy|Romance|Drama",
        "rating": 8.0,
        "director": "Rishab Shetty",
        "cast": "Rakshit Shetty|Rashmika Mandanna|Samyuktha Hegde",
        "keywords": "college friendship youth engineering campus love students comedy",
        "description": "A college student's life changes through friendship, love and growing up."
    },

    {
        "title": "Garuda Gamana Vrishabha Vahana",
        "language": "Kannada",
        "year": 2021,
        "genres": "Crime|Drama",
        "rating": 8.1,
        "director": "Raj B. Shetty",
        "cast": "Raj B. Shetty|Gopalkrishna Deshpande|Gopalkrishna Deshpande",
        "keywords": "friends crime coastal rivalry violence power gangsters revenge",
        "description": "Two childhood friends rise through a violent criminal world and face a dangerous rivalry."
    },

    {
        "title": "Ulidavaru Kandanthe",
        "language": "Kannada",
        "year": 2014,
        "genres": "Crime|Drama|Mystery",
        "rating": 8.4,
        "director": "Rakshit Shetty",
        "cast": "Rakshit Shetty|Kishore|Yagna Shetty|Tara",
        "keywords": "coastal crime multiple perspectives fishing mystery gangsters investigation",
        "description": "A complex crime story is told through multiple perspectives in coastal Karnataka."
    },

    {
        "title": "Avane Srimannarayana",
        "language": "Kannada",
        "year": 2019,
        "genres": "Adventure|Comedy|Fantasy",
        "rating": 8.0,
        "director": "Sachin Ravi",
        "cast": "Rakshit Shetty|Shanvi Srivastava|Achyuth Kumar",
        "keywords": "detective treasure village mystery humor adventure fantasy police",
        "description": "A quirky police officer investigates a treasure mystery in a fictional town."
    },

    {
        "title": "Kavaludaari",
        "language": "Kannada",
        "year": 2019,
        "genres": "Crime|Mystery|Thriller",
        "rating": 8.0,
        "director": "Hemanth M. Rao",
        "cast": "Rishi|Anant Nag|Roshni Prakash|Suman Ranganathan",
        "keywords": "police cold case investigation bodies mystery secrets detective crime",
        "description": "A traffic police officer investigates a decades-old murder mystery."
    },

    {
        "title": "Gantumoote",
        "language": "Kannada",
        "year": 2019,
        "genres": "Drama|Romance",
        "rating": 8.1,
        "director": "Roopa Rao",
        "cast": "Teju Belawadi|Nischith Korodi",
        "keywords": "school friendship teenage love growing up memories youth romance",
        "description": "A coming-of-age story about teenage love, friendship and school life."
    },

    {
        "title": "Dia",
        "language": "Kannada",
        "year": 2020,
        "genres": "Romance|Drama",
        "rating": 8.0,
        "director": "K. S. Ashoka",
        "cast": "Pruthvi Ambaar|Deekshith Shetty|Kushee Ravi",
        "keywords": "love relationships heartbreak emotional college destiny romance",
        "description": "A young woman's life changes through love, loss and unexpected relationships."
    },

    {
        "title": "Sapta Sagaradaache Ello: Side A",
        "language": "Kannada",
        "year": 2023,
        "genres": "Romance|Drama",
        "rating": 8.0,
        "director": "Hemanth M. Rao",
        "cast": "Rakshit Shetty|Rukmini Vasanth|Chaithra J. Achar",
        "keywords": "love prison separation dreams emotional relationship sacrifice romance",
        "description": "A romantic drama about love, separation and the consequences of a life-changing decision."
    },

    {
        "title": "Sapta Sagaradaache Ello: Side B",
        "language": "Kannada",
        "year": 2023,
        "genres": "Romance|Drama",
        "rating": 8.2,
        "director": "Hemanth M. Rao",
        "cast": "Rakshit Shetty|Rukmini Vasanth|Chaithra J. Achar",
        "keywords": "second chance love separation healing emotional relationship memories",
        "description": "A man attempts to rebuild his life and confront memories of a lost relationship."
    },

    {
        "title": "Lucia",
        "language": "Kannada",
        "year": 2013,
        "genres": "Mystery|Psychological|Thriller",
        "rating": 8.3,
        "director": "Pawan Kumar",
        "cast": "Sathish Ninasam|Sruthi Hariharan|Achyuth Kumar",
        "keywords": "dream reality insomnia cinema identity psychological mystery pill",
        "description": "A projectionist experiences a mysterious pill that blurs the boundary between dreams and reality."
    },

    {
        "title": "RangiTaranga",
        "language": "Kannada",
        "year": 2015,
        "genres": "Mystery|Thriller|Drama",
        "rating": 8.1,
        "director": "Anup Bhandari",
        "cast": "Nirup Bhandari|Avantika Shetty|Radhika Chetan",
        "keywords": "village house secrets investigation supernatural suspense mystery family",
        "description": "A couple visiting a remote village become involved in a mystery surrounding an old house."
    },

    {
        "title": "Bell Bottom",
        "language": "Kannada",
        "year": 2019,
        "genres": "Comedy|Crime|Mystery",
        "rating": 7.4,
        "director": "Jayathirtha",
        "cast": "Rishab Shetty|Hariprriya|Yograj Bhat",
        "keywords": "detective police robbery investigation retro humor crime mystery",
        "description": "A clever police detective investigates a series of unusual robberies."
    }
]


# ============================================================
# CREATE DATASET
# ============================================================

fieldnames = [
    "title",
    "language",
    "year",
    "genres",
    "rating",
    "director",
    "cast",
    "keywords",
    "description"
]

with open(
    CSV_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(movies)


print()
print("=" * 60)
print("MOVIE RECOMMENDATION DATASET CREATED")
print("=" * 60)
print(f"Total Movies : {len(movies)}")
print("Languages    : Telugu + Kannada")
print(f"Dataset      : {CSV_FILE}")
print("=" * 60)
print()