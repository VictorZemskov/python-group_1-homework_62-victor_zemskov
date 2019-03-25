import React, {Component} from 'react'
import {USER_URL, SHOWS_URL} from "../../api-urls";
import {NavLink} from "react-router-dom";
import MovieCategories from "../../components/MovieCategories/MovieCategories";
import axios from 'axios';
import moment from 'moment';
import ShowSchedule from "../../components/ShowSchedule/ShowSchedule";


// компонент, который выводит одну карточку с фильмом
// фильм также загружается при выводе компонента на экран (mount),
// а не при обновлении (didUpdate), т.к. компонент выводится на отдельной странице,
// и при переключении страниц исчезает с экрана, а потом снова маунтится.
class UserDetail extends Component {
    state = {
        user: {
            username: "",
            first_name: "",
            last_name: "",
            password: "",
            passwordConfirm: "",
            email: "",
        },
    };
    componentDidMount() {
        // match - атрибут, передаваемый роутером, содержащий путь к этому компоненту
        const match = this.props.match;
        const id = localStorage.getItem('id');


        // match.params - переменные из пути (:id)
        // match.params.id - значение переменной, обозначенной :id в свойстве path Route-а.
        axios.get(USER_URL + id, {
            headers: {'Authorization': 'Token ' + localStorage.getItem('auth-token')}
        })
            .then(response => {
                console.log(response.data);
                return response.data;
            })
            .then(user => {
                this.setState({user});

                // Загрузка расписания показов
                // this.loadShows(user.username);
            })
            .catch(error => console.log(error));
    }


    render() {
        // если movie в state нет, ничего не рисуем.
        if (!this.state.user) return null;
        // достаём данные из movie
        const {username, first_name, last_name, password, email, id} = this.state.user;
        return <div>
            <h3>Имя пользователя: {username}</h3>
            <h3>Имя: {first_name}</h3>
            <h3>Фамилия: {last_name}</h3>
            <h3>email: {email}</h3>
            <NavLink to={'/users/' + id + '/edit'} className="btn btn-primary mr-2">Edit</NavLink>
        </div>;
    }
}


export default UserDetail;