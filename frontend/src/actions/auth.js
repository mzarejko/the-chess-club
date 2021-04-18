import {backend_url} from '../utils/endpoints';
import axios from 'axios';
import {history} from '../utils/history';
import {urls} from '../utils/urls';

export const logout = () => {
    axios.post(backend_url.LOGOUT,{
        "refresh" : localStorage.getItem('refresh_token')
    }).then((response) => {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        history.push(urls.MENU)
    }).catch((err) => {
        console.log(err)
    });
}

export const login = (mail, password) => {
        axios.post(backend_url.LOGIN, {
            "email": mail,
            "password": password
        }).then((response) => {
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            history.push(urls.HOME); 
        }).catch((error) => {
            console.log(error.request.response)
        });
    }

export const register = (username,  email,  password1, password2) => {
        console.log(email)
        axios.post(backend_url.REGISTER, {
            "username": username,
            "email": email,
            "password1": password1,
            "password2": password2
        }).then((response) => {
            history.push(urls.LOGIN); 
            console.log(response.request.response)
        }).catch((error) => {
            console.log(error.request.response)
        });
    }





