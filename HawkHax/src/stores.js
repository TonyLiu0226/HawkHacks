import { writable } from 'svelte/store'
import { localStorageStore } from 'fractils'

export const logStore = localStorageStore('loggedIn', false);
