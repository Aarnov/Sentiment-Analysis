// static/js/firebase.js
// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCb9DDWuz2oBzwS7RnK8Ldwwjpj6aE6WQM",
  authDomain: "sentiment-analysis-d3902.firebaseapp.com",
  projectId: "sentiment-analysis-d3902",
  storageBucket: "sentiment-analysis-d3902.appspot.com",
  messagingSenderId: "247562608343",
  appId: "1:247562608343:web:1f1ac49254685d66d15a92",
  measurementId: "G-GT0GM8KYTF"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
var auth = firebase.auth();
const db = firebase.firestore();
// Signup function
// Firebase Auth state listener to toggle between login/signup and signout buttons
firebase.auth().onAuthStateChanged((user) => {
    if (user) {
        // User is logged in, hide login and signup buttons, show signout
        document.querySelector('.loginLink').style.display = 'none';
        document.querySelector('.signupLink').style.display = 'none';
        document.querySelector('#signout-btn').style.display = 'inline-block';
    } else {
        // No user is logged in, show login and signup buttons, hide signout
        document.querySelector('.loginLink').style.display = 'inline-block';
        document.querySelector('.signupLink').style.display = 'inline-block';
        document.querySelector('#signout-btn').style.display = 'none';
    }
});

// Signup function
function signupUser(event) {
    event.preventDefault();
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;
    const repassword = document.getElementById('repassword-2').value;
    const username = document.getElementById('signupName').value;  // Get the username

    // Ensure password and re-type password match
    if (password !== repassword) {
        alert("Passwords do not match!");
        return;
    }

 firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
        const user = userCredential.user;

        // Add user to Firestore database
        db.collection('users').doc(user.uid).set({
            username: username,
            email: email,
            signupDate: firebase.firestore.FieldValue.serverTimestamp()
        }).then(() => {
            alert('User signed up and added to Firestore successfully!');
            document.getElementById('signupForm').reset();  // Reset form
        }).catch((error) => {
            console.error("Error adding user to Firestore: ", error);
        });
    })
    .catch((error) => {
        const errorMessage = error.message;
        alert('Signup error: ' + errorMessage);
    });
}

// Login function
function loginUser(event) {
    event.preventDefault();  // Prevent form from submitting normally
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    // Firebase login with email and password
    firebase.auth().signInWithEmailAndPassword(email, password)
        .then((userCredential) => {
            // User logged in successfully
            alert('User logged in successfully!');
            document.getElementById('loginForm').reset();  // Reset form

        })
        .catch((error) => {
            // Handle login error
            const errorMessage = error.message;
            alert('Login error: ' + errorMessage);
        });
}

// Handle signout
function signoutUser() {
    firebase.auth().signOut().then(() => {
        alert('User signed out successfully!');
    }).catch((error) => {
        alert('Signout error: ' + error.message);
    });
}

// Event listener for the signout button
document.getElementById('signout-btn').addEventListener('click', (e) => {
    e.preventDefault();
    signoutUser();
});


