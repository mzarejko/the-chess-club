import React, { Component } from 'react'
import './GameList.css'
import {joinGame} from '../../actions/game';
import {listGames} from '../../actions/game';
import InfoDisplayer from '../../components/InfoDisplayer/InfoDisplayer';
import {createGame} from '../../actions/game';
import Button from '../Buttons/Buttons';
 
class GameList extends Component {

    constructor(props){
        super(props)
        this.state = {
            games: [],
            author: '',
            opponent: '',
            winner: '',

        }
        this.infoDisplayerRef = React.createRef();
    }

    updateGames(results){
        this.setState({
            games: results
        })
    }

    componentDidMount(){
        this.findGames()
    }


    findGames = () => {
        listGames(this.state.author,
                  this.state.opponent,
                  this.state.winner)
        .then((response) => {
            this.updateGames(response.data)})
        .catch((error) => {
            console.log(error.request.response)
        })
    }
    
    changeKeys = (key) => {
        this.setState({
            [key.target.name] : key.target.value
        }, this.findGames);
    }

    join = (id) => {
        joinGame(id, this.infoDisplayerRef.current.updateInfo)
    }

    create = (id) => {
        createGame(this.findGames, this.infoDisplayerRef.current.updateInfo)
    }

    render() {
        return (
            <div className="gameList">
                <div>
                    <Button buttonSize='medium'    
                        buttonStyle='outline' 
                        onClick={this.create}>
                            create game
                    </Button>
                </div>
                <input
                    type="text"
                    value={this.state.author}
                    name="author"
                    placeholder={"find author ..."}
                    onChange={this.changeKeys} />
                <input
                    type="text"
                    name="opponent"
                    value={this.state.opponent}
                    placeholder={"find opponent ..."}
                    onChange={this.changeKeys} />
                <input
                    type="text"
                    name="winner"
                    value={this.state.winner}
                    placeholder={"find winner ..."}
                    onChange={this.changeKeys} />

                <div className="menu_back">
                    <div className='game-first'>
                        <p>author</p>
                        <p>opponent</p>
                        <p>winner</p>
                        <p>date</p>
                    </div>
                    {this.state.games.map((item) => {
                        return (
                            <div onClick={() => {this.join(item.pk)}} key={item.pk} 
                                                className="game-row">
                                <p>{item.author}</p>
                                <p>{item.opponent}</p>
                                <p>{item.winner}</p>
                                <p>{item.date}</p>
                            </div>
                        )
                    })}
                </div>
                <InfoDisplayer ref={this.infoDisplayerRef} />
            </div>
        )   
    }
}



export default GameList; 
