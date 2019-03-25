import React, {Component, Fragment} from 'react'
import axios from "axios";
import {USER_URL} from "../../api-urls";
import UserForm from "../../components/UserForm/UserForm";


class UserEdit extends Component {
    state = {
        // исходные данные фильма, загруженные из API.
        user: null,

        // сообщение об ошибке
        alert: null,
    };

    componentDidMount() {
        // match.params - переменные из пути к этому компоненту
        // match.params.id - значение переменной, обозначенной :id в свойстве path Route-а.
        const id = localStorage.getItem('id');
        axios.get(USER_URL + id, {
            headers: {'Authorization': 'Token ' + localStorage.getItem('auth-token')}
        })
            .then(response => {
                const user = response.data;
                console.log(user);
                this.setState(prevState => {
                    const newState = {...prevState};
                    newState.user = user;
                    // newState.user.category_name = movie.category_name.map(category => category.id);
                    return newState;
                });
            })
            .catch(error => {
                console.log(error);
                console.log(error.response);
            });
    }

    // вывод сообщение об ошибке
    showErrorAlert = (error) => {
        this.setState(prevState => {
            let newState = {...prevState};
            newState.alert = {type: 'danger', message: `Movie was not added!`};
            return newState;
        });
    };

    // сборка данных для запроса
    gatherFormData = (user) => {
        let formData = new FormData();
        Object.keys(user).forEach(key => {
            const value = user[key];
            if (value) {
                if(Array.isArray(value)) {
                    // для полей с несколькими значениями (категорий)
                    // нужно добавить каждое значение отдельно
                    value.forEach(item => formData.append(key, item));
                } else {
                    formData.append(key, value);
                }
            }
        });
        return formData;
    };

    // обработчик отправки формы
    formSubmitted = (user) => {
        // сборка данных для запроса
        const formData = this.gatherFormData(user);

        // отправка запроса
        return axios.put(USER_URL + localStorage.getItem('id') + '/', formData, {
            headers: {'Authorization': 'Token ' + localStorage.getItem('auth-token')}
        })
            .then(response => {
                // при успешном создании response.data содержит данные фильма
                const user = response.data;
                console.log(user);
                // если всё успешно, переходим на просмотр страницы фильма с id,
                // указанным в ответе
                this.props.history.replace('/users/' + user.id);
            })
            .catch(error => {
                console.log(error);
                // error.response - ответ с сервера
                // при ошибке 400 в ответе с сервера содержатся ошибки валидации
                // пока что выводим их в консоль
                console.log(error.response);
                this.showErrorAlert(error.response);
            });
    };

    render() {
        const {alert, user} = this.state;
        return <Fragment>
            {alert ? <div className={"mb-2 alert alert-" + alert.type}>{alert.message}</div> : null}
            {user ? <UserForm onSubmit={this.formSubmitted} user={user}/> : null}
        </Fragment>
    }
}


export default UserEdit