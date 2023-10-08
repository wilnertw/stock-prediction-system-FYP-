function matchPassword() {  
    var pw1 = document.getElementById("psw");  
    var pw2 = document.getElementById("con_psw");  
    if(pw1 != pw2)  
    {   
      alert("Passwords did not match");  
    } else {  
      alert("Password created successfully");  
    }  
  }  