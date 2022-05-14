
<script>
  import { goto } from '$app/navigation';
  import { isSignUp1Done} from '../stores.js'

  let userEmail = '';
  let pw1 = '';
  let pw2 = '';
  let githubName = '';
  let phone = '';
  let bio = '';
  
  let message = [];
  let errorMsg = '';

  let validEmail = false;
  let validPhone = false;
  let gitHubExists = false;

  let languageList = [''];
  let frameworkList = [''];


  async function registerUser() {
    let reqBody = { _id : userEmail, password : pw1, languages : languageList, frameworks : frameworkList, github :githubName }
      let payLoad = {
            method : 'POST',
            headers: {'Content-Type': "application/json"},
            body : JSON.stringify(reqBody)
        }

      const response = await fetch("http://localhost:8080/adduser",payLoad);
      if (response.ok) {
        goto("/home");
        
      }
      
    }
  


  const languages = ['C',						
'C++',					
'C#',			
'Go',				
'Java',				
'JavaScript',			
'PHP',
'Python',		
'Scala',
'TypeScript',			
'HTML',
'CSS',
'Verilog',
'ARM Assembly',
'x86-64 Assembly',
'Haskell',
'BASIC',
'Kotlin',
'Racket',
"Swift",
"R",
"Rust",
"Julia",
"Ruby",
"Erlang"];

const frameworks = ['Spring',
    'React',
    'Vue',
    'Svelte',
    'Flask',
    'FastAPI',
    'MongoDB',
    'Firebase',
    'Amazon Web Services',
    'Backbone',
    'Express.JS', 
    'Angular',
    'Django',
    'Laravel',
    'CircuitPython',
    'SASS',
    'ASP.NET Core',
    'Redis',
    'MySQL',
    'NoSQL',
    'SQL',
    'Ruby on Rails',
    'Jquery',
    'Next.js',
    'Apache'];


  function validateEmail() {
    let checker = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
    return checker.test(userEmail);
  }

  function validatePhone() {

    let validator = /^(\+?1 ?)?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    return validator.test(phone);
  }
  
  function validateGitHub() {
    return true;
  }

  function checkInfo(){
    console.log("info saved");
    isSignUp1Done.set(true);
    goto("/signup2");
    
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
          <h3>Sign Up</h3>
          <h6>{errorMsg}</h6>
    
          <label for="username">Email</label>
          <input type="email" placeholder="Email" id="username" bind:value={userEmail} on:input={() => {validEmail = validateEmail()}}>
          {#if userEmail === ""}
          <h6>Email cannot be empty</h6>
          {/if}
          
          {#if !validEmail}
          <h6>Please ensure that your email is in a valid format</h6>
          {/if}

          <label for="password">Password</label>
          <input type="password" placeholder="Password" id="password" bind:value={pw1}>
          {#if pw1.length < 8}
          <h6>Password must be at least 8 characters</h6>
          {/if}

          <label for="password2">Confirm Password</label>
          <input type="password" placeholder="Confirm password" id="password2" bind:value={pw2}>
          {#if pw2 != pw1}
          <h6>Your passwords don't match</h6>
          {/if}

          <label for="github">GitHub Username</label>
          <input type="text" placeholder="Enter GitHub Username" id="github" bind:value={githubName} on:input={() => {gitHubExists = validateGitHub()}}>
          {#if githubName === ''}
          <h6>GitHub cannot be empty</h6>
          {/if}
          {#if !gitHubExists}
          <h6>GitHub account called: {githubName} does not exist!</h6>
          {/if}

          <label for="phone">Phone Number</label>
          <input type="text" placeholder="###-###-####" id="phone" bind:value={phone} on:input={()=> {validPhone = validatePhone()}}>
          {#if phone === ''}
          <h6>Phone cannot be empty</h6>
          {/if}
          
          {#if !validPhone}
          <h6>Please ensure that your phone is in a valid format</h6>
          {/if}

          <div class="title">
            <label for="languages"> Select the languages you are familiar with</label>
        </div>
        <div class="list-of-languages">
          <fieldset>
            {#each languages as language}
            <div id="ck-button">
                <label>
                   <input type="checkbox" name="language" bind:group={languageList} value={language}><span>{language}</span>
                </label>
            </div>
            {/each}
          </fieldset>
        </div>

        <div class="title">
          <label for="frameworks"> Select the frameworks you are familiar with</label>
      </div>
      <div class="list-of-frameworks">
        <fieldset>
          {#each frameworks as framework}
          <div id="ck-button">
              <label>
                 <input type="checkbox" name="framework" bind:group={frameworkList} value={framework}><span>{framework}</span>
              </label>
          </div>
          {/each}
        </fieldset>
      </div>

      <div class="title">
        <label for="bio"> Please enter your biography below</label>
      </div>
    <textarea placeholder="Tell us about yourself!" name="bio" form="signup4" rows="5" bind:value={bio}/>
    {#if bio === '' || bio.length < 10}
    <h6>Biography must be at least 10 characters in length</h6>
    {/if}

          {#if !(!validEmail || userEmail === '' || pw1.length < 8 || pw2 != pw1 || githubName === '' || !gitHubExists || phone==='' || !validPhone || bio ==='' || bio.length < 10)}
          <input type="button" class="button" value="Sign up" on:click={registerUser}/>
          {:else} 
            <h4 style="text-align: center;">Sign Up</h4>
          {/if}
          <div class="link">
          <a href="/login" style="text-align: center;">Already have an account? Log in here</a>
          </div>

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

body {
  background-color: #080710;
}

.link {
  margin-top:10px;
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

form h6 {
  color:red;
}

form h4 {
  margin-top: 50px;
  width: 100%;
  background-color: grey;
  color: #080710;
  padding: 15px 0;
  font-size: 18px;
  font-weight: 600;
  border-radius: 5px;
  cursor: pointer;
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

.title{
    margin-top:20px;
}

textarea {
        margin-top:5px;
        width: 100%;
        padding: 8px 20px;
        background-color: rgba(41, 42, 42, 0.705);
        cursor:text;
    }


</style>