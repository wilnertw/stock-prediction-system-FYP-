function pswCheck(){
    var psw1 = document.getElementById("password").value
    var psw2 = document.getElementById("pass_con").value

    if (psw1 == psw2){
        alert("Sign In Successful")
    }else{
        alert("Password must match")
    }
}