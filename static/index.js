const homeMain = document.getElementById('home-main');
const asideMenu = document.getElementById('nav-aside');
const menuButton = document.getElementById('menu-button');

function openMenuButton() {
    asideMenu.style.width = "300px";
};

function closeMenuButton() {
    asideMenu.style.width = "0px";
}

function nameOnFocusOut() {
    el = document.getElementById("name-input");
    val = el.value;
    if (matchTextOnly(val) == false) {
        el.style.color = "red";
    } else {
        el.style.color = "rgb(44, 55, 75)";
    };
};

function yearOnFocusOut() {
    el = document.getElementById("year-input");
    val = el.value;
    if (matchIntOnly(val) == false || matchLength(val, length=4) == false) {
        el.style.color = "red";
    } else {
        el.style.color = "rgb(44, 55, 75)";
    };
};

function brandOnFocusOut() {
    el = document.getElementById("brand-input")
    val = el.value;
    if (matchTextOnly(val) == false) {
        el.style.color = "red";
    } else {
        el.style.color = "rgb(44, 55, 75)";
    };
};

function athleteOnFocusOut() {
    el = document.getElementById("athlete-input")
    val = el.value;
    if (matchTextOnly(val) == false) {
        el.style.color = "red";
    } else {
        el.style.color = "rgb(44, 55, 75)";
    };
};

function valueOnFocusOut() {
    el = document.getElementById("value-input");
    val = el.value;
    if (matchIntOnly(val) == false) {
        el.style.color = "red";
    } else {
        el.style.color = "rgb(44, 55, 75)";
    };
};

function validateNotesInput() {
    el = document.getElementById("notes-input")
    val = el.value;
    if (matchIntTextOnly(val) == false) {
        el.focus();
    };
};

function matchTextOnly(input) {
    if (input.match(/^[A-Za-z ]+$/)) {
        return true;
    }
    else {
        return false;
    };
};

function matchIntOnly(input) {
    if (input.match(/^[0-9]+$/)) {
        return true;
    }
    else {
        return false;
    };
};

function matchIntTextOnly(input) {
    if (input.match(/^[a-zA-z0-9 ]+$/)) {
        return true;
    }
    else {
        return false;
    };
};

function matchLength(input, length) {
    if (input.length == length) {
        return true;
    } else {
        return false;
    };
};
