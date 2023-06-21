const planets = [
    { name: 'Mercury', moons: 0 },
    { name: 'Venus', moons: 0 },
    { name: 'Earth', moons: 1 },
    { name: 'Mars', moons: 2 },
    { name: 'Jupiter', moons: 79 },
    { name: 'Saturn', moons: 82 },
    { name: 'Uranus', moons: 27 },
    { name: 'Neptune', moons: 14 }
];

// Get the section where planets and moons will be rendered
const listPlanetsSection = document.querySelector('.listPlanets');

// Loop through the planets array
planets.forEach((planet) => {
    // Create a div for the planet
    const planetDiv = document.createElement('div');
    planetDiv.classList.add('planet');
    planetDiv.classList.add(planet.name.toLowerCase());

    // Create a div for each moon
    if (planet.moons > 0) {
        for (let i = 1; i <= planet.moons; i++) {
            const moonDiv = document.createElement('div');
            moonDiv.classList.add('moon');
            moonDiv.style.left = i * 10 + "px"
            planetDiv.appendChild(moonDiv);
        }
    }

    // Append the planet div to the listPlanets section
    listPlanetsSection.appendChild(planetDiv);
});