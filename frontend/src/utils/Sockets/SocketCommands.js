export const backendToFrontendCommands = {
  UPDATE_MESSAGES: 'messages',
  UPDATE_NEW_MESSAGE: 'new_message',
  UPDATE_POSITIONS: 'positions',
  UPDATE_REACHABLE_SQUARES: 'squares',
  CHECK: 'check',
  UNCHECK: 'uncheck',
  END_GAME: 'end'
}

export const frontendToBackendCommands = {
  FETCH_POSITIONS: 'fetch_positions',
  FETCH_MESSAGES: 'fetch_messages',
  SEND_NEW_MESSAGE: 'new_message',
  MOVE_PIECE: 'move_piece',
  FETCH_REACHABLE_SQUARES: 'fetch_reachable_squares',
  REMOVE_PIECE: 'remove_piece'
}
