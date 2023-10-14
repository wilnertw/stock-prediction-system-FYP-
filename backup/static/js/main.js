function pswCheck(){
    var psw1 = document.getElementById("password")
    var psw2 = document.getElementById("pass_con")

    if (psw1 == psw2){
        alert("Sign in successful")
    }else{
        alert("Password must match")
    }
}