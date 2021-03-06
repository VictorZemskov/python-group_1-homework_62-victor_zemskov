import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/v1';
const MOVIES_URL = '/movies/';
const HALL_URL = '/halls/';
const CATEGORIES_URL = '/categories/';
const SHOWS_URL = '/shows/';
const LOGIN_URL = '/login/';
const REGISTER_URL = '/register/';
const USER_URL = '/users/';
const TOKEN_LOGIN_URL = '/token-login/';

const instance = axios.create({baseURL: BASE_URL});

export {BASE_URL, MOVIES_URL, HALL_URL, CATEGORIES_URL, SHOWS_URL, LOGIN_URL, REGISTER_URL, USER_URL, TOKEN_LOGIN_URL};

export default instance;