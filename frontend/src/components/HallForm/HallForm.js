import React, {Component} from 'react'


class HallForm extends Component {
    // в props передаются начальные данные для зала
    // в дальнейшем они копируются в state и извне компонента HallForm больше не меняются
    // (всё остальное управление значением hall и его полей лежит на HallForm).
    constructor(props) {
        super(props);

        // пустой объект зала для формы создания
        const newHall = {
            name: "",
        };

        this.state = {
            submitEnabled: true,
            // изначально hall пустой (для формы добавления)
            hall: newHall,
        };

        // если hall передан через props
        if(this.props.hall) {
            // браузер запрещает программно записывать в value полей типа "file"
            // что-либо, кроме пустой строки
            // поэтому ссылку на текущий постер храним в другом свойстве и отображаем рядом
            // this.state.posterUrl = this.props.movie.poster;

            // записываем в state существующий hall
            this.state.hall = this.props.hall;

            // но удаляем у него значение poster
            // чтобы при сабмите формы не отправлять существующий url или пустую строку
            // (чтобы API не ругался, т.к. url и строка не являются файлами).
            // если ничего не отправлять, постер не поменяется.
            // this.state.movie.poster = null;
        }
    }



    // блокировка отправки формы на время выполнения запроса
    disableSubmit = () => {
        this.setState(prevState => {
            let newState = {...prevState};
            newState.submitEnabled = false;
            return newState;
        });
    };

    // разблокировка отправки формы
    enableSubmit = () => {
        this.setState(prevState => {
            let newState = {...prevState};
            newState.submitEnabled = true;
            return newState;
        });
    };



    // функция, обновляющая поля в this.state.hall
    updateHallState = (fieldName, value) => {
        this.setState(prevState => {
            let newState = {...prevState};
            let hall = {...prevState.hall};
            hall[fieldName] = value;
            newState.hall = hall;
            return newState;
        });
    };

    // обработчик ввода в поля ввода
    inputChanged = (event) => {
        const value = event.target.value;
        const fieldName = event.target.name;
        this.updateHallState(fieldName, value);
    };



    // отправка формы
    // внутри вызывает onSubmit - переданное действие - со своим фильмом в качестве аргумента.
    submitForm = (event) => {
        if(this.state.submitEnabled) {
            event.preventDefault();
            this.disableSubmit();
            this.props.onSubmit(this.state.hall)
                .then(this.enableSubmit);
        }
    };

    render() {
        if (this.state.hall) {
            // распаковка данных зала, чтобы было удобнее к ним обращаться
            const {name} = this.state.hall;
            // распаковка переменных из state.
            const {posterFileName, submitEnabled} = this.state;

            return <div>
                <form onSubmit={this.submitForm}>
                    <div className="form-group">
                        <label className="font-weight-bold">Название</label>
                        <input type="text" className="form-control" name="name" value={name}
                               onChange={this.inputChanged}/>
                    </div>
                    <button disabled={!submitEnabled} type="submit"
                            className="btn btn-primary">Сохранить
                    </button>
                </form>
            </div>;
        }
    }
}


export default HallForm;