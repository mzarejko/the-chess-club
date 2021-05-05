import {backend_url} from '../utils/endpoints';
import {getJoinGameUrl} from '../utils/endpoints';
import axios from 'axios';
import axiosInstance from '../utils/axiosApi';
import {history} from '../utils/history';
import {chooseGameUrl} from '../utils/urls';

export const createGame = (findGames, infoDisplayer) => {
    axiosInstance.post(backend_url.CREATE_GAME)
    .then((response) => {
        findGames()
    }).catch((err) => {
        infoDisplayer(err.request.response)
    });
}

export const joinGame = (id, infoDisplayer) => {
    axiosInstance.put(getJoinGameUrl(id))
    .then((response) => {
        infoDisplayer(response.request.response)
        history.push(chooseGameUrl(id))
    }).catch((error) => {
        console.log(error)
    })
}


export const listGames = (author, opponent, winner) => {
    let path = backend_url.LIST_GAMES 
    if (author){
        path += `&author__username=${author}`
    }
    if (opponent) {
        path += `&opponent__username=${opponent}`
    }
    if (winner) {
        path += `&winner__username=${winner}`
    }
    
    const index = path.indexOf('&')
    if(index !== -1){
        path = path.substring(0,index)+'?'+path.substring(index+1);
    }
    return axios.get(path)
}
