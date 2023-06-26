const robots = [
  {
    id: 1,
    name: 'Leanne Graham',
    username: 'Bret',
    email: 'Sincere@april.biz',
    image: 'https://robohash.org/1?200x200'
  },
  {
    id: 2,
    name: 'Ervin Howell',
    username: 'Antonette',
    email: 'Shanna@melissa.tv',
    image: 'https://robohash.org/2?200x200'
  },
  {
    id: 3,
    name: 'Clementine Bauch',
    username: 'Samantha',
    email: 'Nathan@yesenia.net',
    image: 'https://robohash.org/3?200x200'
  },
  {
    id: 4,
    name: 'Patricia Lebsack',
    username: 'Karianne',
    email: 'Julianne.OConner@kory.org',
    image: 'https://robohash.org/4?200x200'
  },
  {
    id: 5,
    name: 'Chelsey Dietrich',
    username: 'Kamren',
    email: 'Lucio_Hettinger@annie.ca',
    image: 'https://robohash.org/5?200x200'
  },
  {
    id: 6,
    name: 'Mrs. Dennis Schulist',
    username: 'Leopoldo_Corkery',
    email: 'Karley_Dach@jasper.info',
    image: 'https://robohash.org/6?200x200'
  },
  {
    id: 7,
    name: 'Kurtis Weissnat',
    username: 'Elwyn.Skiles',
    email: 'Telly.Hoeger@billy.biz',
    image: 'https://robohash.org/7?200x200'
  },
  {
    id: 8,
    name: 'Nicholas Runolfsdottir V',
    username: 'Maxime_Nienow',
    email: 'Sherwood@rosamond.me',
    image: 'https://robohash.org/8?200x200'
  },
  {
    id: 9,
    name: 'Glenna Reichert',
    username: 'Delphine',
    email: 'Chaim_McDermott@dana.io',
    image: 'https://robohash.org/9?200x200'
  },
  {
    id: 10,
    name: 'Clementina DuBuque',
    username: 'Moriah.Stanton',
    email: 'Rey.Padberg@karina.biz',
    image: 'https://robohash.org/10?200x200'
  }
];

// find the section to put robot divs
const Container = document.getElementById('Container');


// create each div for robot and 
// add robot pic, name, email to the div 
function createCard(robot) {
  // console.log("Entered!")
  const card = document.createElement('div');
  card.classList.add('card');

  const robotImg = document.createElement("img");
  robotImg.src = robot.image
  card.appendChild(robotImg)

  const robotName = document.createElement("p");
  robotName.textContent = robot.name;
  robotName.classList.add("robot-name");
  card.appendChild(robotName)

  const robotEmail = document.createElement("p");
  robotEmail.textContent = robot.email;
  card.appendChild(robotEmail)

  return card;
};


function displayCards() {
  robots.forEach(robot => {
    const card = createCard(robot);
    Container.appendChild(card);
  });
}

const searchBox = document.getElementById('user-search');

// Event listener for the search box input
searchBox.addEventListener('input', () => {
  const searchText = searchBox.value.toLowerCase();
  console.log(searchText)
  const filteredRobots = robots.filter(robot => {
    const robotName = robot.name.toLowerCase();
    return robotName.includes(searchText);
  });

  Container.innerHTML = '';

  filteredRobots.forEach(robot => {
    const card = createCard(robot);
    Container.appendChild(card);
  });
});

displayCards();
