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

export const login = (mail, password, infoDisplayer) => {
        axios.post(backend_url.LOGIN, {
            "email": mail,
            "password": password
        }).then((response) => {
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            history.push(urls.HOME); 
        }).catch((error) => {
            infoDisplayer(error.request.response)
        });
    }

export const register = (username,  email,  password1, password2, infoDisplayer) => {
        axios.post(backend_url.REGISTER, {
            "username": username,
            "email": email,
            "password1": password1,
            "password2": password2
        }).then((response) => {
            infoDisplayer(response.request.response)
        }).catch((error) => {
            infoDisplayer(error.request.response)
        });
    }


export const sendPasswordRename = (email) => {
    axios.post(backend_url.sendPasswordRename, {
        "email": email
    }).then((response) => {
        console.log(response.request.response)
    }).catch((error) => {
        console.log(error.request.response)
    }) 
}


export const changePassword = (password1, password2, uidb64, token) => {
    axios.patch(backend_url.RESET_PASSWORD, {
        "password1": password1,
        "password2": password2,
        "uidb64": uidb64,
        "token": token
    }).then((response) => {
        console.log(response.request.response)
    }).catch((error) => {
        console.log(error.request.response)
    })
}

export const sendMailToChangePassword = (email) => {
    axios.post(backend_url.SEND_RESET_LINK_PASSWORD, {
        "email": email
    }).then((response)=> {
        console.log(response.request.response)
    }).catch((error) => {
        console.log(error.request.response)
    })
}
