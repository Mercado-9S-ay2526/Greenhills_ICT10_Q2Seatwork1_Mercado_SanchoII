#The Nickname Atlas
from pyscript import document


NICKNAMES = {
    "Albania": "The Land of the Eagles",
    "Andorra": "The Land of the Pyrenees",
    "Armenia": "The Land of Noah",
    "Austria": "The Alpine Republic",
    "Azerbaijan": "The Land of Fire",
    "Belarus": "The White Rus",
    "Belgium": "The Heart of Europe",
    "Bosnia and Herzegovina": "The Heart-Shaped Land",
    "Bulgaria": "The Land of Roses",
    "Croatia": "The Land of a Thousand Islands",
    "Cyprus": "The Island of Aphrodite",
    "Czechia": "The Heart of Europe",
    "Denmark": "The Land of the Danes",
    "Estonia": "The Land of Singing",
    "Finland": "The Land of a Thousand Lakes",
    "France": "The Hexagon",
    "Georgia": "The Cradle of Wine",
    "Germany": "The Land of Poets and Thinkers",
    "Greece": "The Cradle of Western Civilization",
    "Hungary": "The Land of the Magyars",
    "Iceland": "The Land of Fire and Ice",
    "Ireland": "The Emerald Isle",
    "Italy": "The Bel Paese (Beautiful Country)",
    "Kazakhstan": "The Land of the Great Steppe",
    "Kosovo": "The Land of the Dardanians",
    "Latvia": "The Land That Sings",
    "Liechtenstein": "The Principality in the Alps",
    "Lithuania": "The Land of Amber",
    "Luxembourg": "The Green Heart of Europe",
    "Malta": "The Island of Honey",
    "Moldova": "The Land of the Open Door",
    "Monaco": "The Rock",
    "Montenegro": "The Black Mountain",
    "Netherlands": "The Low Countries",
    "North Macedonia": "The Land of the Sun",
    "Norway": "The Land of the Midnight Sun",
    "Poland": "The Land of Fields",
    "Portugal": "The Garden by the Sea",
    "Romania": "The Land of Dracula",
    "Russia": "The Motherland",
    "San Marino": "The Most Serene Republic",
    "Serbia": "The Land of the South Slavs",
    "Slovakia": "The Heart of Europe",
    "Slovenia": "The Sunny Side of the Alps",
    "Spain": "The Land of the Sun",
    "Sweden": "The Land of the Midnight Sun",
    "Switzerland": "The Land of the Alps",
    "Turkey": "The Land Between Two Continents",
    "Ukraine": "The Breadbasket of Europe",
    "United Kingdom": "The Sceptred Isle",
    "Vatican City": "The Holy See",
}

def reveal_nickname(event=None):
    country = document.querySelector("#country").value
    result = document.querySelector("#result")

    if not country:
        result.innerText = "Choose a country first."
        return

    nickname = NICKNAMES.get(
        country,
        "A nickname still waiting to be discovered",
    )

    result.innerText = f"{country}: {nickname}"