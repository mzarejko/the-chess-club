export const urls = {
  LOGIN : '/login/',
  REGISTER: '/register/',
  FORGET_PASSWORD: '/forget-password/',
  RESET_PASSWORD: '/reset-password/',
  HOME: '/home/',
  MENU: '/',
  GAME: '/play/:gameId/',
  ANONYMOUS_GAME: '/anonymous-play/:gameId/'
}

export function chooseGameUrl(id){
  return `/play/${id}/`
}
