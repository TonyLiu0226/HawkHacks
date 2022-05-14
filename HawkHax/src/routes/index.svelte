

<script context="module"> 
    import { logStore } from "../stores.js";
    import {get} from 'svelte/store'

    export async function load() {
        if (get(logStore)) {
            return {
                status: 302,
                redirect: "/home"
            };
        }
        else {
            return {
                status : 302,
                redirect : "/login"
            }
        }
        
    }
</script>

