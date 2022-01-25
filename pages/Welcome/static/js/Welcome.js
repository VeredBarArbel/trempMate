const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});

function signIn() {
    document.getElementById("signToHome").onclick = function () {
        location.href = "LandingPage.html";
    };
}

function checkEmail(id) {
    var b1 = document.getElementById(id).value;
    if (b1.length < 5 || !(b1.includes('@') && b1.includes('.') && b1.indexOf('@') < b1.indexOf('.'))) {
        alert("כתובת הדואר האלקטרוני לא תקינה. עליה להכיל @ ונקודה, ולהכיל 5 תוים לפחות");
        document.getElementById(id).value = "";
    }
}

