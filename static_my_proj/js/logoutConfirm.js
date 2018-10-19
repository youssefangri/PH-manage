document.getElementById("logout").onclick = function (){
    var txt;
    var r = confirm("Are you sure you want to logout?");
    if (r == true) {
        return true;
    } else {
        return false;
    }
}
