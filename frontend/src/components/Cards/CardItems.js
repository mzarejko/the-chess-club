import * as GiIcons from "react-icons/gi";
import * as FaIcons from "react-icons/fa";
import {urls} from '../../utils/paths/urls';

export const CardItems= [
    {
        path: urls.GAME,
        icon: <GiIcons.GiCrossedSwords />,
        image: 'https://media.giphy.com/media/ViHG6N1Zhq1A7tDwbF/giphy.gif',
        description: 'play',
        alt: 'create_game'
    },
    {
        path: urls.LOGIN,
        icon: <FaIcons.FaTrophy />,
        image: 'https://media.giphy.com/media/l19ipdY2pjK3d8Omtz/giphy.gif',
        description: 'login',
        alt: 'my_games'
    },
    {
        path: urls.REGISTER,
        icon: <FaIcons.FaUserEdit/>,
        image: 'https://media.giphy.com/media/OMFfLpauGoT4c/giphy.gif',
        description: 'register',
        alt: 'edit_profile'
    },
]
