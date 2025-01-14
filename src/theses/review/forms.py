from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, RadioField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired
from flask import Markup
from wtforms.widgets import TextArea


class ThesisReviewFilter(FlaskForm):
    status = SelectField("status", choices=[])
    worktype = SelectField("worktype", choices=[])
    areasofstudy = SelectField("areasofstudy", choices=[])


class AddThesisOnReview(FlaskForm):
    title = StringField(
        "title",
        description="Укажите название загружаемой работы",
        validators=[DataRequired()],
    )
    thesis = FileField()
    author = StringField(
        "author", description="Ваше полное ФИО. Например, Иванов Иван Иванович"
    )
    supervisor = SelectField("supervisor", choices=[])
    type = SelectField("type", choices=[])
    area = SelectField("area", choices=[])


class EditThesisOnReview(FlaskForm):
    name_ru = StringField(
        "title",
        description="Укажите название загружаемой работы",
        validators=[DataRequired()],
    )
    text_uri = FileField()
    author = StringField(
        "author", description="Ваше полное ФИО. Например, Иванов Иван Иванович"
    )
    supervisor = SelectField("supervisor", choices=[])
    type = SelectField("type", coerce=int, choices=[])
    area = SelectField("area", coerce=int, choices=[])


class ReviewForm(FlaskForm):
    o1_label_5 = Markup(
        "<strong>Отлично (5)</strong>: по своему содержанию и оформлению работа соответствует всем предъявленным требованиям"
    )
    o1_label_4 = Markup(
        "<strong>Очень хорошо (4)</strong>: лучше, чем хорошо, но хуже, чем отлично"
    )
    o1_label_3 = Markup(
        "<strong>Хорошо (3)</strong>: по своему содержанию и оформлению работа соответствует большинству предъявленных требований, или имеется ряд неточностей, которые не мешают общему восприятию работы"
    )
    o1_label_2 = Markup(
        "<strong>Удовлетворительно (2)</strong>: лучше, чем достаточно, но хуже, чем хорошо"
    )
    o1_label_1 = Markup(
        "<strong>Достаточно (1)</strong>: По своему содержанию и оформлению работа явно нарушает не более трёх предъявленных требований"
    )
    o1_label_0 = Markup("<strong>Плохо (0)</strong>: хуже, чем «достаточно»")

    review_o1_radio_switcher = RadioField(
        "ReviewO1Form",
        choices=[
            ("5", o1_label_5),
            ("4", o1_label_4),
            ("3", o1_label_3),
            ("2", o1_label_2),
            ("1", o1_label_1),
            ("0", o1_label_0),
        ],
    )

    review_o1_comment = StringField(
        "review_o1_comment",
        description="Тут перечислите замечания к работе по этому критерию",
        widget=TextArea(),
    )

    o2_label_5 = Markup(
        "<strong>Отлично (5)</strong>: в работе описан контекст решаемой задачи, присутствует обзор аналогов, предшествующих работ и используемых инструментов (если это уместно), существенные утверждения работы подтверждены ссылками на источники, составлена библиография по теме работы"
    )
    o2_label_4 = Markup(
        "<strong>Очень хорошо (4)</strong>: лучше, чем хорошо, но хуже, чем отлично"
    )
    o2_label_3 = Markup(
        "<strong>Хорошо (3)</strong>: продемонстрированы навыки работы с источниками, но упущены некоторые важные результаты, не все существенные утверждения работы подтверждены ссылками на источники. Составлена библиография по теме работы"
    )
    o2_label_2 = Markup(
        "<strong>Удовлетворительно (2)</strong>: лучше, чем достаточно, но хуже, чем хорошо"
    )
    o2_label_1 = Markup(
        "<strong>Достаточно (1)</strong>: в работе не описан контекст решаемой задачи, либо полностью отсутствует обзор аналогов, предшествующих работ либо используемых инструментов (если это уместно), присутствуют субъективные оценочные суждения или многочисленные неподтверждённые утверждения"
    )
    o2_label_0 = Markup(
        "<strong>Плохо (0)</strong>: отсутствует литературный обзор, библиография по теме работы"
    )

    review_o2_radio_switcher = RadioField(
        "ReviewO2Form",
        choices=[
            ("5", o2_label_5),
            ("4", o2_label_4),
            ("3", o2_label_3),
            ("2", o2_label_2),
            ("1", o2_label_1),
            ("0", o2_label_0),
        ],
    )

    review_o2_comment = StringField(
        "review_o2_comment",
        description="Тут перечислите замечания к обзору",
        widget=TextArea(),
    )

    t1_label_5 = Markup(
        "<strong>Отлично (5)</strong>: в работе приведены исчерпывающие аргументы принятых решений"
    )
    t1_label_4 = Markup(
        "<strong>Очень хорошо (4)</strong>: лучше, чем хорошо, но хуже, чем отлично"
    )
    t1_label_3 = Markup(
        "<strong>Хорошо (3)</strong>: в работе приведены методологически верные аргументы принятых решений. Дополнительные аргументы могут улучшить работу"
    )
    t1_label_2 = Markup(
        "<strong>Удовлетворительно (2)</strong>: лучше, чем достаточно, но хуже, чем хорошо"
    )
    t1_label_1 = Markup(
        "<strong>Достаточно (1)</strong>: в работе есть слабая аргументация принятых решений"
    )
    t1_label_0 = Markup(
        "<strong>Плохо (0)</strong>: в работе отсутствует аргументация принятых решений"
    )

    review_t1_radio_switcher = RadioField(
        "ReviewT1Form",
        choices=[
            ("5", t1_label_5),
            ("4", t1_label_4),
            ("3", t1_label_3),
            ("2", t1_label_2),
            ("1", t1_label_1),
            ("0", t1_label_0),
        ],
    )

    review_t1_comment = StringField(
        "review_t1_comment", description="Ваш ответ", widget=TextArea()
    )

    t2_label_5 = Markup(
        "<strong>Отлично (5)</strong>: в работе приведен полный сравнительный анализ с аналогами"
    )
    t2_label_4 = Markup(
        "<strong>Очень хорошо (4)</strong>: лучше, чем хорошо, но хуже, чем отлично"
    )
    t2_label_3 = Markup(
        "<strong>Хорошо (3)</strong>: в работе приведен подробный сравнительный анализ с аналогами. Однако не все значимые аналоги приведены или сравнение проводилось не по всем значимым критериям"
    )
    t2_label_2 = Markup(
        "<strong>Удовлетворительно (2)</strong>: лучше, чем достаточно, но хуже, чем хорошо"
    )
    t2_label_1 = Markup(
        "<strong>Достаточно (1)</strong>: в работе приведены аналоги, но их выбор необоснован, перечень недостаточен, или сравнение с ними ничего не демонстрирует"
    )
    t2_label_0 = Markup(
        "<strong>Плохо (0)</strong>: в работе отсутствует аргументация принятых решений"
    )

    review_t2_radio_switcher = RadioField(
        "ReviewT2Form",
        choices=[
            ("5", t2_label_5),
            ("4", t2_label_4),
            ("3", t2_label_3),
            ("2", t2_label_2),
            ("1", t2_label_1),
            ("0", t2_label_0),
        ],
    )

    review_t2_comment = StringField(
        "review_t2_comment", description="Ваш ответ", widget=TextArea()
    )

    p1_label_5 = Markup(
        "<strong>Отлично (5)</strong>: качество кода на высоком уровне с соблюдением рекомендаций по архитектуре, стилю и тестированию ПО. Продемонстрированно владение современными технологиями и библиотеками. Также по открытому репозиторию исходного кода видно, что работа велась в течение всего года"
    )
    p1_label_4 = Markup(
        "<strong>Очень хорошо (4)</strong>: лучше, чем хорошо, но хуже, чем отлично"
    )
    p1_label_3 = Markup(
        "<strong>Хорошо (3)</strong>: хорошее качество кода, продемонстрировано владение современными технологиями и библиотеками. Или по открытому репозиторию исходного кода видно, что работа велась с существенными перерывами или только в течение одного семестра"
    )
    p1_label_2 = Markup(
        "<strong>Удовлетворительно (2)</strong>: лучше, чем достаточно, но хуже, чем хорошо"
    )
    p1_label_1 = Markup(
        "<strong>Достаточно (1)</strong>: практическая часть присутствует и работает исправно, однако архитектура не адекватна решаемой задаче и стиль исполнения низкого качества. Или по открытому репозиторию исходного кода видно, что работа велась только в последний месяц перед датой зачёта"
    )
    p1_label_0 = Markup(
        "<strong>Плохо (0)</strong>: практическая часть отсутствует или ее наличие не позволяет сделать выводы о техническом уровне автора. Открытый репозиторий исходного кода не предоставлен"
    )
    p1_label_x = Markup(
        "<strong>Не применимо</strong>: исходный код закрыт или работа не предполагает написания кода"
    )

    review_p1_radio_switcher = RadioField(
        "ReviewP1Form",
        choices=[
            ("5", p1_label_5),
            ("4", p1_label_4),
            ("3", p1_label_3),
            ("2", p1_label_2),
            ("1", p1_label_1),
            ("0", p1_label_0),
            ("x", p1_label_x),
        ],
    )

    review_p1_comment = StringField(
        "review_p1_comment", description="Ваш ответ", widget=TextArea()
    )

    p2_label_5 = Markup(
        "<strong>Отлично (5)</strong>: экспериментальная методология полностью описана, соответствует принятым в данной области стандартам, и сама по себе не вызывает вопросов, непосредственные результаты задокументированы и доступны, обработка результатов методологически корректна"
    )
    p2_label_4 = Markup(
        "<strong>Очень хорошо (4)</strong>: лучше, чем хорошо, но хуже, чем отлично"
    )
    p2_label_3 = Markup(
        "<strong>Хорошо (3)</strong>: экспериментальная методология проработана недостаточно хорошо, однако общее направление экспериментов адекватно поставленной задаче. Обработка данных содержит ошибки, не ставящие, однако, под сомнение общий результат. Указаны только итоговые данные экспериментов"
    )
    p2_label_2 = Markup(
        "<strong>Удовлетворительно (2)</strong>: лучше, чем достаточно, но хуже, чем хорошо"
    )
    p2_label_1 = Markup(
        "<strong>Достаточно (1)</strong>: эксперименты выполнены, а результаты обработаны без опоры на качественную экспериментальную методологию, или в ходе работы были допущены существенные ошибки, ставящие результаты под сомнение. Итоговые данные предоставлены не полностью"
    )
    p2_label_0 = Markup(
        "<strong>Плохо (0)</strong>: экспериментов и/или измерений нет, или они содержат серьёзные ошибки или искажения"
    )
    p2_label_x = Markup(
        "<strong>Не применимо</strong>: работа не предполагает экспериментов или измерений"
    )

    review_p2_radio_switcher = RadioField(
        "ReviewP2Form",
        choices=[
            ("5", p2_label_5),
            ("4", p2_label_4),
            ("3", p2_label_3),
            ("2", p2_label_2),
            ("1", p2_label_1),
            ("0", p2_label_0),
            ("x", p2_label_x),
        ],
    )

    review_p2_comment = StringField(
        "review_p2_comment", description="Ваш ответ", widget=TextArea()
    )

    review_overall_comment = StringField(
        "review_overall_comment", description="Ваш ответ", widget=TextArea()
    )

    verdict_label_1 = Markup("<strong>Можно зачесть</strong>")
    verdict_label_0 = Markup("<strong>На доработку</strong>")

    review_verdict_radio_switcher = RadioField(
        "ReviewVerdictForm", choices=[("1", verdict_label_1), ("0", verdict_label_0)]
    )

    review_file = FileField()
