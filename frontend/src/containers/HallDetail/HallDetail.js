import React, {Component} from 'react'
import {HALL_URL} from "../../api-urls";
import {NavLink} from "react-router-dom";
import axios from 'axios';


// компонент, который выводит одну карточку с залом
// зал также загружается при выводе компонента на экран (mount),
// а не при обновлении (didUpdate), т.к. компонент выводится на отдельной странице,
// и при переключении страниц исчезает с экрана, а потом снова маунтится.
class HallDetail extends Component {
    state = {
        hall: null
    };
    componentDidMount(){
        // match - атрибут, передаваемый роутером, содержащий путь к этому компоненту
        const match = this.props.match;
        // match.params - переменные из пути (:id)
        // match.params.id - значение переменной, обозначенной :id в свойстве path Route-а.
        axios.get(HALL_URL + match.params.id)
            .then(response => {console.log(response.data); return response.data;})
            .then(hall => this.setState({hall}))
            .catch(error => console.log(error));
    }
    render() {
        // если hall в state нет, ничего не рисуем.
        if (!this.state.hall) return null;
        // достаём данные из hall
        const {name, id} = this.state.hall;
        return <div>
            {/* постер, если есть */}
            {/*{poster ? <div className='text-center'>*/}
                {/*<img className="img-fluid rounded" src={poster}/>*/}
            {/*</div> : null}*/}

            {/* название зала */}
            <h1>{name}</h1>

            {/* редактировать зал */}
            <NavLink to={'/halls/' + id + '/edit'} className="btn btn-primary mr-2">Edit</NavLink>

            {/* назад */}
            <NavLink to='/halls' className="btn btn-primary">Halls</NavLink>
        </div>;
    }
}


export default HallDetail;