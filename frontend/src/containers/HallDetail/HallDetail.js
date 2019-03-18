import React, {Component} from 'react'
import {HALL_URL, MOVIES_URL, SHOWS_URL} from "../../api-urls";
import {NavLink} from "react-router-dom";
import axios from 'axios';
import moment from "moment";
import ShowSchedule from "../../components/ShowSchedule/ShowSchedule";


// компонент, который выводит одну карточку с залом
// зал также загружается при выводе компонента на экран (mount),
// а не при обновлении (didUpdate), т.к. компонент выводится на отдельной странице,
// и при переключении страниц исчезает с экрана, а потом снова маунтится.
class HallDetail extends Component {
    state = {
        hall: null,
        shows: null
    };
    // componentDidMount(){
    //     // match - атрибут, передаваемый роутером, содержащий путь к этому компоненту
    //     const match = this.props.match;
    //     // match.params - переменные из пути (:id)
    //     // match.params.id - значение переменной, обозначенной :id в свойстве path Route-а.
    //     axios.get(HALL_URL + match.params.id)
    //         .then(response => {console.log(response.data); return response.data;})
    //         .then(hall => this.setState({hall}))
    //         .catch(error => console.log(error));
    // }

    componentDidMount() {
        // match - атрибут, передаваемый роутером, содержащий путь к этому компоненту
        const match = this.props.match;

        // match.params - переменные из пути (:id)
        // match.params.id - значение переменной, обозначенной :id в свойстве path Route-а.
        axios.get(HALL_URL + match.params.id)
            .then(response => {
                console.log(response.data);
                return response.data;
            })
            .then(hall => {
                this.setState({hall});

                // Загрузка расписания показов
                this.loadShows(hall.id);
            })
            .catch(error => console.log(error));
    }

    loadShows = (hall_nameId) => {
        // https://momentjs.com/ - библиотека для работы с датой и временем в JS
        // более удобная, чем встроенный класс Date(). Не забудьте импортировать.
        // установка: npm install --save moment (уже ставится вместе с реактом)
        // импорт: import moment from 'moment';

        // вернёт текущую дату со временем в формате ISO с учётом временной зоны
        const startDate = moment().format('YYYY-MM-DD HH:mm');
        // вернёт только дату на 3 дня вперёд от текущей в указанном формате
        const finishDate = moment().add(3, 'days').format('YYYY-MM-DD');

        // encodeURI закодирует строку для передачи в запросе
        // отличается от encodeURIComponent тем, что пропускает символы,
        // входящие в формат URI, в т.ч. & и =.
        const query = encodeURI(`hall_name_id=${hall_nameId}&start_date=${startDate}&finish_date=${finishDate}`);
        axios.get(`${SHOWS_URL}?${query}`).then(response => {
            console.log(response);
            this.setState(prevState => {
                let newState = {...prevState};
                newState.shows = response.data;
                return newState;
            })
        }).catch(error => {
            console.log(error);
            console.log(error.response);
        });
    };

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

            {this.state.shows ? <ShowSchedule shows={this.state.shows}/> : null}

            {/* назад */}
            {/*<NavLink to='/halls' className="btn btn-primary">Halls</NavLink>*/}
        </div>;
    }
}


export default HallDetail;