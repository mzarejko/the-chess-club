import * as GiIcons from "react-icons/gi";
import * as FaIcons from "react-icons/fa";
import {urls} from '../../utils/urls';

export const CardItems= [
    {
        path: urls.HOST_GAME,
        icon: <GiIcons.GiCrossedSwords />,
        image: 'https://media.giphy.com/media/ViHG6N1Zhq1A7tDwbF/giphy.gif',
        description: 'create game',
        alt: 'create_game'
    },
    {
        path: urls.MY_GAMES,
        icon: <FaIcons.FaTrophy />,
        image: 'https://media.giphy.com/media/l19ipdY2pjK3d8Omtz/giphy.gif',
        description: 'my games',
        alt: 'my_games'
    },
    {
        path: urls.MY_GAMES,
        icon: <FaIcons.FaUserEdit/>,
        image: 'https://media.giphy.com/media/OMFfLpauGoT4c/giphy.gif',
        description: 'edit my profile',
        alt: 'edit_profile'
    },
]
