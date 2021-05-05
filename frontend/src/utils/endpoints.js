
export const backend_url = {
  HOST : "http://127.0.0.1:8000/",
  REGISTER : "http://127.0.0.1:8000/accounts/register/", 
  LOGIN : "http://127.0.0.1:8000/accounts/login/", 
  REFRESH_TOKEN : 'http://127.0.0.1:8000/accounts/refresh-token/',
  USERS : 'http://127.0.0.1:8000/accounts/users/',
  LOGOUT : 'http://127.0.0.1:8000/accounts/logout/',
  SEND_RESET_LINK_PASSWORD : 'http://127.0.0.1:8000/accounts/reset-password-email/',
  RESET_PASSWORD : 'http://127.0.0.1:8000/accounts/reset-password-complete/',
  SOCKET : "ws://127.0.0.1:8000",
  CREATE_GAME : 'http://127.0.0.1:8000/games/new/',
  LIST_GAMES : 'http://127.0.0.1:8000/games/',
}

export function getChatUrl(id, token){
  return `ws://127.0.0.1:8000/chat/${id}/?token=${token}`
}

export function getJoinGameUrl(id){
  return `${backend_url.LIST_GAMES}${id}/`
}

