let users = null
function loadUsers(){

    fetch('https://jsonplaceholder.typicode.com/users/')
    .then(response => response.json())
    .then(json => users = json)
}
