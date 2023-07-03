const url = 'https://www.swapi.tech/api/'

async function getCharacterData() {
  try {
    const characterId = Math.floor(Math.random() * 83) + 1;   // The API contains 83 different characters
    console.log(characterId)  // debug use 
    const characterUrl = `${url}/people/${characterId}`   //  URL looks like https://www.swapi.tech/api/people/83
    const response = await fetch(characterUrl);
    const characterJson = await response.json();
    const characterProperties = characterJson.result.properties;
    return (({ name, height, gender, birth_year, homeworld }) =>
      ({ name, height, gender, birth_year, homeworld }))(characterProperties);
  } catch (error) {
    console.log(error);
  }
}

async function fixPlanetName(obj) {
  try {
    const url = obj.homeworld;
    const response = await fetch(url);
    const characterJson = await response.json();
    const planetName = characterJson.result.properties.name
    obj.homeworld = planetName;
    return obj
  } catch (error) {
    console.log(error)
  }
}


async function getCharacterObject() {
  try {
    const character = await getCharacterData();
    console.log(character);
    const characterWithPlanet = await fixPlanetName(character);
    console.log(characterWithPlanet);
    return characterWithPlanet
  } catch (error) {
    console.log(error);
  }
}


async function displayContent(event) {
  const container = document.getElementById('information')
  container.innerHTML =
    `<i class="fa-solid fa-spinner fa-spin-pulse"></i>
      <h2>Loading...</h2>`
  try {
    const characterObj = await getCharacterObject();
    console.log(characterObj);
    container.innerHTML = `
        <h2>${characterObj.name}</h2>
        <p>Height: ${characterObj.height}</p>
        <p>Gender: ${characterObj.gender}</p>
        <p>Birth Year: ${characterObj.birth_year}</p>
        <p>Home World: ${characterObj.homeworld}</p>
      `;
  } catch (error) {
    container.innerHTML = `Oh No! That person isn't available`
  }
}

document.getElementById('search-button').addEventListener('click', displayContent);
