// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.

//     Create a class named Video. The class should be constructed with the following parameters:
//         title (a string)
//         uploader (a string, the person who uploaded it)
//         time (a number, the duration of the video - in seconds)

class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

    //     Create a method called watch() which displays a string as follows:
    //     “uploader parameter watched all time parameter of title parameter!”

    watch() {
        console.log(`${this.uploader} watched all ${this.time} of ${this.title}!`);
    }
}


// Instantiate a new Video instance and call the watch() method.
const video = new Video("Something", "Someone", "60");
video.watch();

// Instantiate a second Video instance with different values.
const another = new Video("Can't not think of any title", "a decent name", "30");
another.watch();

// Bonus: Use an array to store data for five Video instances (ie. title, uploader, time)
// Think of the best data structure to save this information within the array.
const videosArray = [
    new Video("Video 1", "User 1", 30),
    new Video("Video 2", "User 2", 60),
    new Video("Video 3", "User 3", 90),
    new Video("Video 4", "User 4", 120),
    new Video("Video 5", "User 5", 150)
];

// Bonus: Loop through the array to instantiate those instances.
videosArray.forEach((video) => video.watch());