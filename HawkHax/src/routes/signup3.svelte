<script>
    import { goto } from '$app/navigation';
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

    function checkInfo(){
        console.log("info saved");
        goto("/signup4");
    
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
            <div class="title">
                <h4> Select the frameworks you are familiar with</h4>
            </div>
            <div class="list-of-frameworks">
                {#each frameworks as framework}
                <div id="ck-button">
                    <label>
                       <input type="checkbox" value="1" hidden><span>{framework}</span>
                    </label>
                </div>
                {/each}
            
            </div>
    
            <input type="button" class="button" value="Next" on:click={checkInfo} />
            
            
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
    
    ::placeholder{
    color: #e5e5e5;
    }

    .title{
    margin-top:20px;
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
    
    body {
        font-family:sans-serif;
    }
    
    #ck-button {
        padding:15px auto;
        margin:4px;  
        border-radius:4px;
        border:1px solid #D0D0D0;
        overflow:auto;
        float:left;
    }
    
    #ck-button:not(:checked){
        background-color:#080808;
    }
    
    #ck-button:hover {
        background-color:#b00b69;
    }
    
    #ck-button label {
        float:left;
        min-width:4em;
    }
    
    #ck-button label span {
        padding: 10px 10px;
        text-align:center;
        display:block;
    }
    
    #ck-button label input {
        display:none;
    }
    
    #ck-button input:checked + span {
        background:#b00b69;
        color:#fff;
    }
    
    label {
        width: 100%;
    }
    
    
    
    </style>