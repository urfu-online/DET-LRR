from addict import Dict
indicators_raw = [{'group': 'Кадровый состав авторского коллектива (Соблюдение квалификационных требований)',
               'title': 'Наличие базового образования или профессиональной переподготовки в предметной области курса хотя бы у одного из авторов',
               'type': 'contental',
               'values_list': ['нет-данных', 'отсутствует', 'имеется'],
               "scores": []
               },
              {'group': 'Кадровый состав авторского коллектива (Соблюдение квалификационных требований)',
               'title': 'Наличие опыта работы или преподавания в предметной области не менее 3 лет не менее чем у 50% авторов',
               'type': 'contental',
               'values_list': ['нет-данных', 'отсутствует-у-более-чем-50-авторов', 'имеется-не-менее-чем-у-50-авторов']},
              {'group': 'Кадровый состав авторского коллектива (Соблюдение квалификационных требований)',
               'title': 'Доля авторов с ученой степенью и(или) званием доцента или профессора. Допустимые значения показателя: 0-100%',
               'type': 'contental', 'values_list': ['0-100'],
               'class': 'numeric',
               },
              {'group': 'Полнота заполнения полей паспорта ресурса', 'title': 'Наименование', 'type': 'methodical',
               'values_list': ['не-заполнено', 'заполнено']},
              {'group': 'Полнота заполнения полей паспорта ресурса', 'title': 'Сведения об авторах',
               'type': 'methodical', 'values_list': ['не-заполнено', 'заполнено']},
              {'group': 'Полнота заполнения полей паспорта ресурса', 'title': 'Описание', 'type': 'methodical',
               'values_list': ['не-заполнено', 'заполнено']},
              {'group': 'Полнота заполнения полей паспорта ресурса', 'title': 'Трудоемкость', 'type': 'methodical',
               'values_list': ['не-заполнено', 'заполнено']},
              {'group': 'Полнота заполнения полей паспорта ресурса', 'title': 'Пререквизиты', 'type': 'methodical',
               'values_list': ['не-заполнено', 'заполнено']},
              {'group': 'Полнота заполнения полей паспорта ресурса',
               'title': 'Корректное описание цели, задач и результатов обучения', 'type': 'methodical',
               'values_list': ['не-заполнено', 'заполнено']},
              {'group': 'Полнота заполнения полей паспорта ресурса', 'title': 'Корректное описание компетенций',
               'type': 'methodical', 'values_list': ['не-заполнено', 'заполнено']},
              {'group': 'Полнота заполнения полей паспорта ресурса', 'title': 'Длительность', 'type': 'methodical',
               'values_list': ['не-заполнено', 'заполнено']},
              {'group': 'Полнота заполнения полей паспорта ресурса', 'title': 'Направления подготовки',
               'type': 'methodical', 'values_list': ['не-заполнено', 'заполнено']},
              {'group': 'Полнота заполнения полей паспорта ресурса', 'title': 'Язык контента', 'type': 'methodical',
               'values_list': ['не-заполнено', 'заполнено']},
              {'group': 'Редакционно-издательская обработка',
               'title': 'Присутствие в материалах ресурса опечаток, пунктуационных или грамматических ошибок, изъянов в форматировании материалов и других признаков отсутствия редакционно-издательской обработки',
               'type': 'methodical',
               'values_list': ['не-выявлено', 'выявлено']},
              {'group': 'Соблюдение требований в области защиты авторских прав',
               'title': 'Наличие в ресурсе материалов, не созданных творческим трудом правообладателя ресурса (неаттрибутированные заимствования или плагиат: тексты, опубликованные в книгах, журналах, в сети Интернет; иллюстрации, в том числе рисунки, графики, схемы '
                        'и диаграммы; фотографии – включая репродукции произведений графики, живописи, скульптуры и архитектуры), для которых не соблюдены правила оформления заимствования',
               'type': 'methodical',
               'values_list': ['отсутствуют', 'имеются']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Степень соответствия выбора средств (инструментов) реализации оценочных материалов задачам оценки теоретических результатов обучения',
               'type': 'methodical',
               'values_list': ['отсутствуют', 'не-соответствуют', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего',
                          'высокая']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Степень соответствие выбора средств (инструментов) реализации оценочных материалов задачам оценки практических результатов обучения',
               'type': 'methodical',
               'values_list': ['отсутствуют', 'не-соответствуют', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего',
                          'высокая']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Степень соответствия оценочных материалов запланированным результатам обучения',
               'type': 'methodical',
               'values_list': ['отсутствуют', 'не-соответствуют', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего',
                          'высокая']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Степень соответствия оценочных материалов учебному содержанию ЭОР',
               'type': 'methodical',
               'values_list': ['отсутствуют', 'не-соответствуют', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего',
                          'высокая']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Оценочные материалы обеспечивают целостную оценку результатов обучения', 'type': 'methodical',
               'values_list': ['отсутствуют', 'нет', 'да']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Оценочных материалов достаточно для объективной и достоверной оценки результатов обучения',
               'type': 'methodical', 'values_list': ['отсутствуют', 'нет', 'да']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Степень соответствия структуры и содержание оценочных материалов методическим требованиям (включают инструкцию, описание алгоритма выполнения, критерии оценивания)',
               'type': 'methodical',
               'values_list': ['отсутствуют', 'не-соответствуют', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего',
                          'высокая']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Оценочные материалы представлены в разных видах и формах', 'type': 'methodical',
               'values_list': ['отсутствуют', 'нет', 'да']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'ЭОР обеспечен итоговыми контрольно-оценочными материалами', 'type': 'methodical',
               'values_list': ['отсутствуют', 'нет', 'да']},
              {'group': 'Соответствие требованиям к структуре ресурса',
               'title': 'Уровень структуризации материалов ресурса, позволяющей сформировать теоретические знания, практические навыки и проконтролировать достижение результатов обучения',
               'type': 'methodical',
               'values_list': ['не-структурированы', 'низкий', 'ниже-среднего', 'средний', 'выше-среднего', 'высокий']},
              {'group': 'Соответствие требованиям к структуре ресурса',
               'title': 'Степень обеспеченности элементов структуры материалами, «позволявшими сформировать теоретические знания, практические навыки и проконтролировать достижение результатов обучения»',
               'type': 'methodical',
               'values_list': ['не-обеспечены', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего', 'высокая']},
              {'group': 'Состав применяемых технологий',
               'title': 'Применяемые технологии обеспечивают реализацию всех необходимых для достижения заявленных результатов обучения видов учебной деятельности',
               'type': 'methodical', 'values_list': ['нет', 'да']},
              {'group': 'Состав применяемых технологий',
               'title': 'Наличие компонентов ресурса, предусматривающих несинхронную коммуникацию с преподавателем (например: форум, задание с ручной проверкой)',
               'type': 'methodical', 'values_list': ['отсутствуют', 'имеются']},
              {'group': 'Состав применяемых технологий',
               'title': 'Наличие компонентов интерактивного взаимодействия с обучающимся без участия преподавателя (например: тест, задание с автоматизированной проверкой, задания со взаимной проверкой и пр.)',
               'type': 'methodical',
               'values_list': ['отсутствуют', 'имеются']},
              {'group': 'Управление учебной деятельностью', 'title': 'Методические рекомендации по работе с ресурсом',
               'type': 'methodical', 'values_list': ['отсутствуют', 'имеются']},
              {'group': 'Управление учебной деятельностью', 'title': 'Описание правил общения', 'type': 'methodical',
               'values_list': ['отсутствует', 'имеется']},
              {'group': 'Управление учебной деятельностью', 'title': 'График выполнения контрольных мероприятий',
               'type': 'methodical', 'values_list': ['отсутствует', 'имеется']},
              {'group': 'Управление учебной деятельностью', 'title': 'График открытия материалов', 'type': 'methodical',
               'values_list': ['отсутствует', 'имеется']},
              {'group': 'Управление учебной деятельностью', 'title': 'Система оценивания', 'type': 'methodical',
               'values_list': ['отсутствует', 'имеется']},
              {'group': 'Управление учебной деятельностью',
               'title': 'Наличие инструментов для аналитики/ аналитических исследований отношения обучающихся к реализации учебной процесса на основе данного ЭОР: анкеты обратной связи',
               'type': 'methodical',
               'values_list': ['отсутствуют', 'имеются']},
              {'group': 'Соблюдение требований в области защиты авторских прав',
               'title': 'Доля оригинальности контента. Допустимые значения показателя: 0-100%', 'type': 'contental',
               'values_list': ['0-100'],
               'class': 'numeric',
               },
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Степень соответствия содержания оценочных материалов задачам оценки теоретических результатов обучения',
               'type': 'contental',
               'values_list': ['отсутствуют', 'не-соответствуют', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего',
                          'высокая']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Степень соответствия содержания оценочных материалов задачам оценки практических результатов обучения',
               'type': 'contental',
               'values_list': ['отсутствуют', 'не-соответствуют', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего',
                          'высокая']},
              {'group': 'Соответствие требованиям к оценочным материалам',
               'title': 'Степень сбалансированности состава оценочных материалов на всем наборе результатов обучения',
               'type': 'contental',
               'values_list': ['отсутствуют', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего', 'высокая']},
              {'group': 'Соответствие содержанию дисциплины ОП',
               'title': 'Доля покрытия разделов, тем и видов учебой работы рабочей программы дисциплины структурой и содержанием ресурса. Допустимые значения показателя: 0-100%',
               'type': 'contental/На соответствие дисицплине (для каждой заявленной дисциплины)',
               'values_list': ['нет-данных', '0-100'],
               'class': 'numeric_empty',
               },
              {'group': 'Соответствие содержанию дисциплины ОП',
               'title': 'Полнота соответствия формируемых ресурсом компетенций и достигаемых результатов обучения, компетенциям и результатам, предусмотренным дисциплиной',
               'type': 'contental/На соответствие дисицплине (для каждой заявленной дисциплины)',
               'values_list': ['не-соответствуют', 'не-полностью-соответствуют', 'полностью-соответствуют']},
              {'group': 'Соответствие требованиям к контенту',
               'title': 'Степень соответствия материалов ресурса актуальным достижениям науки и практики в соответствующей предметной области',
               'type': 'contental',
               'values_list': ['не-соответствуют', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего', 'высокая']},
              {'group': 'Соответствие требованиям к контенту',
               'title': 'Степень актуальности и востребованности материалов', 'type': 'contental',
               'values_list': ['не-актуальны', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего', 'высокая']},
              {'group': 'Соответствие требованиям к контенту',
               'title': 'Степень соответствия контента ресурса методическим требованиям, установленным для материалов определенного вида',
               'type': 'contental',
               'values_list': ['не-соответствует', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего', 'высокая']},
              {'group': 'Соответствие требованиям к контенту',
               'title': 'Степень полноты и достаточности материалов ресурса в предметной области (фактологическая и прагматическая содержательность, формирование целостного представления об изучаемом вопросе)',
               'type': 'contental',
               'values_list': ['не-достаточен', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего', 'высокая']},
              {'group': 'Соответствие требованиям к контенту',
               'title': 'Степень полноты и достаточности материалов для достижения заявленных результатов обучения и соответствующих компетенций',
               'type': 'contental',
               'values_list': ['не-достаточен', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего', 'высокая']},
              {'group': 'Соответствие требованиям к контенту',
               'title': 'Отсутствие в материалах ресурса фактологических ошибок', 'type': 'contental',
               'values_list': ['имеются', 'отсутствуют']},
              {'group': 'Соответствие требованиям к контенту',
               'title': 'Степень понятности и доступности для целевой аудитории языка изложения содержания ресурса',
               'type': 'contental',
               'values_list': ['не-понятен', 'низкая', 'ниже-среднего', 'средняя', 'выше-среднего', 'высокая']},
              {'group': 'Соответствие требованиям к контенту',
               'title': 'Соответствие заявленной трудоемкости реальной временной потребности для освоения материала ресурса',
               'type': 'contental', 'values_list': ['не-соответствует', 'соответствует']},
              {'group': 'Дизайн-эргономические и технические характеристики используемых средств обучения',
               'title': 'Соответствие текстовых материалов дизайн-эргономическим требованиям',
               'type': 'technical',
               'values_list': ['отсутствуют', 'не-соответствуют', 'соответствуют']},
              {'group': 'Дизайн-эргономические и технические характеристики используемых средств обучения',
               'title': 'Соответствие видео и аудио материалов дизайн-эргономическим и техническим требованиям',
               'type': 'technical',
               'values_list': ['отсутствуют', 'не-соответствуют', 'соответствуют']},
              {'group': 'Дизайн-эргономические и технические характеристики используемых средств обучения',
               'title': 'Соответствие графических материалов дизайн-эргономическим и техническим требованиям',
               'type': 'technical',
               'values_list': ['отсутствуют', 'не-соответствуют', 'соответствуют']},
              {'group': 'Дизайн-эргономические и технические характеристики используемых средств обучения',
               'title': 'Соответствие интерактивных материалов дизайн-эргономическим и техническим требованиям',
               'type': 'technical',
               'values_list': ['отсутствуют', 'не-соответствуют', 'соответствуют']},
              {'group': 'Дизайн-эргономические и технические характеристики используемых средств обучения',
               'title': 'Соответствие нетипизированных образовательных программных продуктов (симуляторов, тренажеров и др.) дизайн-эргономическим и техническим требованиям',
               'type': 'technical',
               'values_list': ['отсутствуют', 'не-соответствуют', 'соответствуют']},
              {'group': 'Дизайн-эргономические и технические характеристики используемых средств обучения',
               'title': 'Функционирование всех компонентов ресурса на заявленном наборе браузеров/операционных сред',
               'type': 'technical',
               'values_list': ['не-функционируют', 'функционируют']},
              {'group': 'Дизайн-эргономические и технические характеристики используемых средств обучения',
               'title': 'Работоспособность ссылок на сторонние ресурсы', 'type': 'technical',
               'values_list': ['не-работоспособны', 'работоспособны']},
              {'group': 'Доступ к ресурсу', 'title': 'Вид регистрации пользователя для доступа к ресурсу',
               'type': 'technical', 'values_list': ['не-предусмотрена', 'открытая', 'закрытая']}]

statuses = ["ЭОР для внутреннего использования",
            "КУРС для внутреннего использования",
            "ЭОР для внешнего использования/ЭОР сторонний",
            "КУРС для внешнего использования/ КУРС сторонний",
            "Обеспечивает реализацию части дисциплины в электронной среде",
            "Обеспечивает реализацию в электронной среде всей дисциплины, в соответствии с РПД",
            "Обеспечивает в электронной среде полное достижение результатов обучения по дисциплине",
            "Не интерактивный",
            "С поддержкой преподавателя",
            "Автоматизированный"]

indicators = [Dict(i) for i in indicators_raw]
