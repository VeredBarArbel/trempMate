// project - part 2
function buttonVisibility(buttonID) {
    document.getElementById(buttonID).style.visibility = "visible";
}

function notification(elementId, message) {
    alert(message);
}

// project - part 3
function navCurrentTab(currentId) {
    console.log("change class");
    const navIds = ['navHome', 'navProfile', 'navSearch', 'navAdd', 'navContact'];
    for (const id in navIds) {
        console.log(id);
        document.getElementById(id).className = "empty";
    }
    document.getElementById(currentId).className = "active";
}