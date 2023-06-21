// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :

//     title,
//     author,
//     image : a url,
//     alreadyRead : which is a boolean (true or false).
// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)
const allBooks = [
    {
        title: 'Python Crash Course',
        author: 'Eric Matthes',
        image: 'https://m.media-amazon.com/images/I/71sL0Qpd+YL._AC_UF1000,1000_QL80_.jpg',
        alreadyRead: true
    },
    {
        title: 'Head First Python',
        author: 'Paul Barry',
        image: 'https://m.media-amazon.com/images/I/51I1iu7LvQL._AC_UF1000,1000_QL80_.jpg',
        alreadyRead: false
    }
];

//Requirements : All the instructions below need to be coded in the js file:

//   Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
//   For each book :
//       You have to display the book’s title and the book’s author.
//       Example: HarryPotter written by JKRolling.
//       The width of the image has to be set to 100px.
//       If the book is already read. Set the color of the book’s details to red.

const listBooksSection = document.querySelector('.listBooks');

allBooks.forEach((book) => {
    // Create a div for the book
    const bookDiv = document.createElement('div');
    bookDiv.classList.add('book');

    const imageStyle = `width: 100px;`;
    const detailsStyle = book.alreadyRead ? `color: red;` : '';

    const bookContent = `
    <img src="${book.image}" style="${imageStyle}" alt="${book.title}">
    <p>${book.title} by ${book.author}</p>
    <p style="${detailsStyle}">Already Read: ${book.alreadyRead}</p>
  `;

    bookDiv.innerHTML = bookContent;
    listBooksSection.appendChild(bookDiv);

});