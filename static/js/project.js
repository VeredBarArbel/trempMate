function buttonVisibility(buttonID) {
    document.getElementById(buttonID).style.visibility = "visible";
}

function notification(elementId, message) {
    alert(message);
}

const navIds = ['navHome', 'navProfile', 'navSearch', 'navAdd', 'navContact'];
function navCurrentTab(currentId) {
    for (id in navIds) {
        document.getElementById(id).className = "empty";
    }
    document.getElementById(currentId).className = "active";
}