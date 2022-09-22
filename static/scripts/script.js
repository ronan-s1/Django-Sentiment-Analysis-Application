document.getElementById("load").style.visibility = "hidden";

function load()
{
    document.getElementById("submit-button").style.display = "none";
    document.getElementById("load").style.visibility = "visible";
    document.getElementById("display").style.visibility = "hidden";
}

function yelp_load()
{
    document.getElementById("submit-button").style.display = "none";
    document.getElementById("load").style.visibility = "visible";
    document.getElementById("graph-div").style.display = "none";
    document.getElementById("yelp-result").style.display = "none";
    document.getElementById("yelp-result-table").style.display = "none";
}
