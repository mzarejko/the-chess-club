export const urls = {
  LOGIN : '/login/',
  REGISTER: '/register/',
  FORGET_PASSWORD: '/forget-password/',
  RESET_PASSWORD: '/reset-password/',
  HOME: '/home/',
  MENU: '/',
  GAME: '/play/:Id/',
  ANONYMOUS_GAME: '/anonymous-play/:Id/'
}

export function gameUrl(id){
  return `/play/${id}/`
}
