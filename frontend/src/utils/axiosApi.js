import axios from 'axios';
import {backend_url} from './endpoints';
import {logout} from '../actions/auth';

const axiosInstance = axios.create({
    baseURL: backend_url.HOST,
    timeout: 5000,
});

axiosInstance.interceptors.request.use((config) => {
    config.headers.Authorization =  'Bearer '+localStorage.getItem('access_token');
    return config;
}, (error) => {
    return error
});

axiosInstance.interceptors.response.use((response) => {
    return response;
}, (error) => {
    if (error.response.status === 401){
        resetToken().then(()=>{
            error.config.headers['Authorization'] = 'Bearer' + localStorage.getItem('access_token');
            error.config.baseURL = undefined;
            return axios.request(error.config);
        });
    }
    return error
});

function resetToken(){
    axios.post(backend_url.REFRESH_TOKEN, {
    "refresh" : localStorage.getItem('refresh_token') 
    }).then((response) => {
        localStorage.removeItem('access_token')
        localStorage.setItem('access_token', response.data.access);
    }).catch((err) => {
        logout()
        return err
    });
};


export default axiosInstance; 



