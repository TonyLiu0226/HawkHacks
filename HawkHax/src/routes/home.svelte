
<script context="module"> 
    import  Card  from '../components/Card.svelte';
    import { logStore } from "../stores.js";
    import {get} from 'svelte/store'

    export async function load() {
        if (!get(logStore)) {
            return {
                status: 302,
                //redirect: "/login"
            };
        }
    
    }
</script>
<script>
</script>

<!-- svelte-ignore a11y-missing-attribute -->
<html>
  <body>
<Card />
<Card />
<div class="Game">

</div>
</body>
</html>
<style>

html,body{
  height: 100%;
  display: flex;
  flex-direction: column;
}
.Game{
  flex-grow: 1;
  border-radius: 150px;
  outline: 15px solid black;
  left:65%;
  height:70%;
  right:15px;
  top:140px;
  position:fixed;
}

</style>