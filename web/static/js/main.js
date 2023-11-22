function dataBase(){
    var mysql = require('mysql')

    var con = mysql.createConnection({
        host: "localhost",
        user: "root",
        database: "fyp"
    });
}

function signin_check(){
    var psw1 = document.getElementById("password").value
    var psw2 = document.getElementById("pass_con").value
    var user = document.getElementById("username").value
    var user2 = document.getElementById("email").value

    var existing_username = 'SELECT * FROM users WHERE username = user'
    var existing_email = 'SELECT * FROM users WHERE email = user2'

    if (psw1 == psw2){
        alert("Sign In Successful");
    }
    if (existing_username || existing_email){
        console.log('User already exist.')
    }

}

function feedback_alert(){
    alert("Feedback has been submitted.")
}

function saved_alert(){
    alert("Saved Successfully")
}

function acc_deleted(){
    alert("Account Deleted")
}