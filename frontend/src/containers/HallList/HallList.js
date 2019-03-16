import React, {Fragment, Component} from 'react'
import {HALL_URL} from "../../api-urls";
import HallCard from "../../components/HallCard/HallCard";
import {NavLink} from "react-router-dom";
import axios from 'axios';


// компонент для показа списка залов клиенту
// залы запрашиваются из API в момент показа компонента на странце (mount)
class HallList extends Component {
    state = {
        halls: [],
    };

    componentDidMount() {
        axios.get(HALL_URL)
            .then(response => {console.log(response.data); return response.data;})
            .then(halls => this.setState({halls}))
            .catch(error => console.log(error));
    }

    hallDeleted = (hallId) => {
        axios.delete(HALL_URL + hallId + '/').then(respose => {
            console.log(respose.data);
            this.setState(prevState => {
                let newState = {...prevState};
                let halls = [...newState.halls];
                let hallIndex = halls.findIndex(hall => hall.id === hallId);
                halls.splice(hallIndex, 1);
                newState.halls = halls;
                return newState;
            })
        }).catch(error => {
            console.log(error);
            console.log(error.response);
        })
    };

    render() {
        return <Fragment>
            <p><NavLink to='/halls/add'>Добавить зал</NavLink></p>
            <div className='row'>
                {this.state.halls.map(hall => {
                    return <div className='col-xs-12 col-sm-6 col-lg-4 mt-3'  key={hall.id}>
                        <HallCard hall={hall} onDelete={() => this.hallDeleted(hall.id)}/>
                    </div>
                })}
            </div>
        </Fragment>
    }
}


export default HallList;