<script>
    import { goto } from '$app/navigation';
    let bio = '';
</script>
    
    <head>
        
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap" rel="stylesheet">
        <!--Stylesheet-->
        
    </head>
    <body>
        <form id="signup4">
            <h3>Log In</h3>
            <div class="title">
                <h5> Please enter your biography below</h5>
            </div>
            <textarea placeholder="Tell us about yourself!" name="bio" form="signup4" rows="5" bind:value={bio}/>
            {#if bio === '' || bio.length < 10}
            <h6>Biography must be at least 10 characters in length</h6>
            {:else}
            <input class="button" type="button" value="Next" />
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
    
    body {
      background-color: #080710;
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
    
    textarea {
        margin-top:5px;
        width: 100%;
        padding: 8px 20px;
        background-color: rgba(41, 42, 42, 0.705);
        cursor:text;
    }

    .title{
    margin-top: 20px;
    }
    
    </style>