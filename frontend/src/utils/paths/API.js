
// set this url ony if app is in production
// var HOST_BASE ="https://the-chess-club-backend.herokuapp.com/" 
// var HOST_WS = 'ws://the-chess-club-backend.herokuapp.com/'

// set this if development
var HOST_BASE ="http://127.0.0.1:8000/" 
var HOST_WS = 'ws://127.0.0.1:8000/'

export const backend_url = {
  HOST : `${HOST_BASE}`,
  REGISTER : `${HOST_BASE}accounts/register/`, 
  LOGIN : `${HOST_BASE}accounts/login/`, 
  REFRESH_TOKEN : `${HOST_BASE}accounts/refresh-token/`,
  USERS : `${HOST_BASE}accounts/users/`,
  LOGOUT : `${HOST_BASE}accounts/logout/`,
  SEND_RESET_LINK_PASSWORD : `${HOST_BASE}accounts/reset-password-email/`,
  RESET_PASSWORD : `${HOST_BASE}accounts/reset-password-complete/`,
  SOCKET : `${HOST_WS}`,
  CREATE_GAME : `${HOST_BASE}games/new/`,
  LIST_GAMES : `${HOST_BASE}games/`,
}


export function getChatEndpoint(id, token){
  return `${HOST_WS}chat/${id}/?token=${token}`
}

export function getGameEndpoint(id, token){
  return `${HOST_WS}game/${id}/?token=${token}`
}

export function getJoinGameEndpoint(id){
  return `${backend_url.LIST_GAMES}${id}/?token={localStorage.getItem('access_token')}`
}
