import { writable } from 'svelte/store'
import { localStorageStore } from 'fractils'

export const logStore = localStorageStore('loggedIn', false);
export const isSignUp1Done = writable(false);
export const isSignUp2Done = writable(false);
export const isSignUp3Done = writable(false);