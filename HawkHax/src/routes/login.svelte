
<script>
 import { logStore } from "../stores.js";
 import {goto} from "$app/navigation"
  

  let email = "";
  let password = "";

  let loginFailed = false;
  let displayFieldError = false;

  async function log_in() {
    if (email.length == 0 || password.length == 0) {
      displayFieldError = true;

    }
    else {
      let reqBody = { email : email, password : password }
      let payLoad = {
            method : 'POST',
            headers: {'Content-Type': "application/json"},
            body : JSON.stringify(reqBody)
        }

      const response = await fetch("http://localhost:8080/validateuser",payLoad);
      if (response.ok) {
        logStore.set(true);
        goto("/home");
        
      }
      else {
        loginFailed = true;
      }
    }
    
  }
</script>

<head>
	
      <link rel="preconnect" href="https://fonts.gstatic.com">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap" rel="stylesheet">
      <!--Stylesheet-->
      
  </head>
  <body>
      <form>
          <h3>Log In</h3>
  
          <label for="username">Email</label>
          <input type="text" placeholder="Email" bind:value={email} id="username">
  
          <label for="password">Password</label>
          <input type="password" placeholder="Password" bind:value={password} id="password">
  
          <button type="button" class="button" value="Log In" on:click={log_in}> Log In </button>
          
         <div class="link">
            <a href="./signup">Don't have an account? Sign up here!</a>
         </div>
          
         {#if loginFailed}
            <h2 style="color:red; text-align:center;"> Login failed </h2>
         {/if}  
         
         {#if displayFieldError}
          <h2 style="color:red; text-align:center;"> Please ensure both fields are filled out!</h2>
         {/if}
         
          
      </form>
  </body>

  <style media="screen">
    *,
    *:before,
*:after{
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body{
  background-color: #080710;
}

.link {
  margin-top : 25px;
  display:block;
  text-align: center;
}

form {
  display : block;
  margin-left : auto;
  margin-right : auto;
  margin-bottom : 20px;
  width:35%;
  background-color: rgba(255,255,255,0.13); 
  border-radius: 10px;
  backdrop-filter: blur(30px);
  border: 2px solid rgba(255,255,255,0.1);
  box-shadow: 0 0 40px rgba(8,7,16,0.6);
  padding: 50px 35px;
}
form *{
  font-family: 'Poppins',sans-serif;
  color: #ffffff;
  letter-spacing: 0.5px;
  outline: none;
  border: none;
}
form h3{
  font-size: 32px;
  font-weight: 500;
  line-height: 42px;
  text-align: center;
}

label{
  display: block;
  margin-top: 30px;
  font-size: 16px;
  font-weight: 500;
}
input{
  display: block;
  height: 50px;
  width: 100%;
  background-color: rgba(255,255,255,0.07);
  border-radius: 3px;
  padding: 0 10px;
  margin-top: 8px;
  font-size: 14px;
  font-weight: 300;
}
::placeholder{
  color: #e5e5e5;
}

.button{
  margin-top: 50px;
  width: 100%;
  background-color: #ffffff;
  color: #080710;
  padding: 15px 0;
  font-size: 18px;
  font-weight: 600;
  border-radius: 5px;
  cursor: pointer;
}


</style>