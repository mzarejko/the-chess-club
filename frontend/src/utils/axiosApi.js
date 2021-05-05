import axios from 'axios';
import {backend_url} from './endpoints';
import {logout} from '../actions/auth';

/*
 After each request this code check if request is aunthenticated 
 and if not then backend return 401 error and then frontend should send 
 request for refresh token and try the same request, if it fail again then it should 
 logout user
 */


const axiosInstance = axios.create({
    baseURL: backend_url.HOST,
    timeout: 5000,
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

axiosInstance.interceptors.request.use((config) => {
    console.log('request')
    config.headers.Authorization =  'Bearer '+localStorage.getItem('access_token');
    return config;
}, (error) => {
    console.log('request error')
    return error
});

axiosInstance.interceptors.response.use((response) => {
    return response;
}, (error) => {
    console.log('response error')
    if (error.response.status === 401){
        resetToken().then(()=>{
            error.config.headers['Authorization'] = 'Bearer' + localStorage.getItem('access_token');
            error.config.baseURL = undefined;
            console.log('token refresh')
            return axios.request(error.config);
        });
    }
    return error
});



export default axiosInstance; 



