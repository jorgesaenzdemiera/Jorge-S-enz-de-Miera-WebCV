import streamlit as st

col_1, col_2 = st.columns(2)
col_1.page_link("pages/1_Currículum.py", label="🡸 Ir a Currículum")
col_1.page_link("Presentación.py", label="🡸 Ir a Presentación")

col_2.write("Educación y Tecnología")

st.markdown("""
            # USO DE LAS TECNOLOGÍAS EN LAS AULAS
            ![Portada](https://github.com/jorgesaenzdemiera/archivos/blob/main/images/intro.jpg?raw=true)
            \n
            Las generaciones actuales son nativas tecnológicas, ya que los dispositivos tecnológicos han formado parte de sus vidas desde edades tempranas. En otras palabras, los niños de la actualidad nacen con un acercamiento a la tecnología muy amplio y con el paso de los años este se hace más fuerte. Se produce en actividades muy cotidianas como calmar el llanto del niño recurriendo a videos, música, películas o series de diversas plataformas para conseguir de esta manera la distracción y tranquilidad de los niños. Por tanto, debido al mundo globalizado y tecnológico en el que estamos establecidos, la sociedad y la educación tienen que tener como objetivo adaptarse a la actualidad, y por ello nace la necesidad de orientar la educación hacia el uso apropiado de la tecnología,  ya que su papel en el futuro de los alumnos va a ser muy elevado. 
            \n
            Para ello, los profesores deben conocer las diferentes herramientas y recursos digitales a los que pueden acceder, no solo vale introducirlas en el aula, sino que debe servir a los alumnos para que así desarrollen nuevas habilidades. Hay que tener en cuenta que dejar a los estudiantes trabajar con tecnologías e internet tiene sus ventajas y sus desventajas, como las siguientes:
            \n
            **Ventajas:**
            - Fuentes de información rápidas
            - Enseñanza visual y atractiva
            - Eficacia de comunicación a distancia con la familia y los amigos
            - Necesidad actual de conocer las tecnologías para distintas tareas laborales y cotidianas
            \n
            **Desventajas:**
            - Dependencia a las nuevas tecnologías
            - Peligros en redes
            - Acoso en la red
            - Brecha informática o digital
            - Acceso a fake news
            - Elemento distractor
            - Puede usarse con un fin poco ético
            \n
            El uso de la tecnología dentro del campo educativo está cada día más presente por parte de muchos de los educadores, pero aún queda mucho avance, ya que no todos tienen las mismas posibilidades de aplicar los mismos recursos en el aula por la brecha digital o tecnológica, que es definida como “la desigualdad en el acceso, uso  y/o impacto de las nuevas tecnologías de la información y la comunicación (TIC) entre  diferentes grupos sociales” (Grupo artico34, sf). Esta desigualdad sigue presente en la actualidad y se ha destacado especialmente durante la  reciente pandemia. Aquellos sin acceso a dispositivos tecnológicos se encontraron  limitados en sus capacidades. Esta brecha también ha existido previamente entre las  diversas generaciones dentro de entornos laborales, impactando especialmente a los  inmigrantes digitales que tuvieron y tienen que familiarizarse con nuevas tecnologías  para mantenerse activos en sus roles. Además, es relevante señalar la presencia de  esta desigualdad en diferentes segmentos de la población, ya que las personas con  recursos limitados enfrentan dificultades al perder oportunidades debido a la falta de  acceso a las tecnologías. 
            \n
            Por suerte, España es un país desarrollado y puede utilizar recursos tecnológicos dentro del aula para así adaptarse a la actualidad digital en la que estamos sumergidos y pueden ponerla  en marcha a través de: PowerPoints, vídeos, blogs, el acceso a Inteligencias Artificiales como Chat GPT o Bard, juegos didácticos, entre otros.  
            \n
            Este blog apoya la idea de que el alumnado trabaje con materiales digitales, ya que como se ha mencionado anteriormente, trabajar con este tipo de herramientas proporciona una enseñanza más visual y atractiva, lo que avivará su motivación, captando así su interés e implicación por la asignatura ya que son mayormente clases más dinámicas y entretenidas en comparación a las tradicionales. Sin embargo hay que tener en cuenta que estas tecnologías pueden presentar numerosos peligros, por un lado, se va a producir la mencionada brecha digital, porque como ya hemos visto, no todas las personas pueden permitirse acceder de la misma manera a diferentes informaciones, conocimientos, educación y recursos por lo que siempre estarán presentes desigualdades entre unas sociedades y otras. Por otro lado, el auge de timos y bulos en la web, con mensajes diseñados para captar la atención y, eventualmente, robar información o suplantar identidades, representa un riesgo, particularmente para los niños y jóvenes, quienes son vulnerables a estas tácticas. 
            \n
            Otro peligro preocupante son los acosos que hay en internet. Este blog apoya la idea de abordar temas de seguridad de manera seria en el contexto educativo, es por ello, que al igual que hay que informar a los alumnos, se debe informar y concienciar a las familias, tanto de lo positivo que tiene trabajar con ellas en el aula y fuera del aula, como de lo negativo.  Para colaborar a la detección y reconocimiento de noticias falsas, desde este blog ofrecemos una serie de puntos que deben seguir tanto familiares, docentes y alumnos para evitar la divulgación de noticias falsas:
            ![FakeNews](https://github.com/jorgesaenzdemiera/archivos/blob/main/images/unnamed.png?raw=true)
            \n
            Debido a que el uso de las tecnologías es un campo de investigación muy abierto, este blog se centrará en la explicación y profundización del término Inteligencia Artificial (IA) y los puntos positivos y negativos que hay en su uso. Empezaremos respondiendo a la siguiente cuestión:
            \n
            ## ¿Qué es la Inteligencia Artificial?
            \n
            La inteligencia artificial (IA) se refiere a la capacidad de las máquinas para imitar funciones cognitivas humanas, como el aprendizaje, el razonamiento y la resolución de problemas. Se aplica en diversas áreas, desde asistentes virtuales hasta diagnósticos médicos y sistemas de recomendación. El aprendizaje automático, una rama de la IA, permite a las máquinas mejorar su rendimiento a través de la experiencia y la asimilación de datos. 
            \n
            Para interactuar con la IA, utilizamos unos prompts, que podrían definirse como “una frase o pregunta que se utiliza para estimular una respuesta por parte de Inteligencias Artificiales, como Chat GPT.” (Morales, 2023). La claridad en los prompts es esencial para obtener las respuestas más exactas sobre lo que buscamos por lo que, debemos comunicar lo que queremos encontrar de la manera más precisa posible. Asimismo, la IA se basa en aplicar algoritmos y modelos matemáticos que cuentan con cierta complejidad para así responder distintos tipos de cuestiones, como el  reconocimiento de patrones o la toma de decisiones. 
            \n
            Una vez explicado el concepto de IA hay que tener en cuenta la opinión de los padres, familiares y los propios alumnos de utilizarla en las aulas, ya que pueden surgir grupos de padres que ruegan la prohibición de la utilización de estas herramientas por los diferentes debates sociales y morales que puedan llegar a surgir.
            \n
            Entre los **dilemas** asociados con la IA, discutimos:
            \n
            #### Posibles problemas
            \n
            Al igual que la tecnología la IA trae consigo implícita una serie de problemas y de puntos positivos. Por ejemplo, hay muchos problemas de protección de privacidad, dado que opera mediante algoritmos basados en nuestras preferencias y accede a datos personales. También, se usa para dar diagnósticos o sentencias judiciales, esto puede acarrear ciertos problemas. La IA es programada por empresas específicas que influyen en la información que recibimos a través de ella, por lo que existe una influencia de manipular la conciencia humana. Recopila errores de gente que publica cosas en internet. Por tanto, en muchas ocasiones da respuestas que no se ajustan a lo que le piden. Muchas páginas web están cerrando las fuentes de open I, porque pierden dinero.
            \n
            Es de vital importancia tener en cuenta que alguien que programa la IA no es neutral, por lo que esta siempre estará condicionada a quienes programan esto, y transmitirá y priorizará “x” información. Por lo que realmente la IA no funciona como una representación global, sino que, simplemente crean sesgos que tienen que ver con un origen étnico y la cultura occidental, que da una visión determinada sobre otros colectivos, haciendo que nos cuestionemos: ¿Quién produce la información? ¿Estamos todos representados?
            \n
            La IA no puede pensar ni analizar desigualdades internas. Además, niega los derechos de autor por lo que hay implicaciones legales y denuncias por motivos económicos cierran el acceso a la información. En cuanto a esta información hay que tener claro que proporciona información personal de cualquier persona, por el flujo de información y de datos.
            \n
            #### Puntos positivos
            \n
            La IA es una herramienta que procesa y analiza la información y los datos muy rápidamente, además proporciona a la actividad humana un acceso a la información rápida, intuitiva y sencilla consiguiendo que nos faciliten tareas y ahorremos tiempo en búsquedas que realmente no son necesarias. Utilizar la IA viene bien cuando el diseño es instruccional, es decir, la función que conlleva es copia y pega y para cuando solo es necesario la veracidad de conocimientos para bufetes, médicos… Últimamente se usa para una detección precoz de determinados cánceres, lo que provoca más gente sana y viva, potencia cosas buenas relacionadas a la salud.
            \n
            #### ¿Puede una IA sustituir a un profesor?
            \n
            A pesar de que sea un inmenso avance tecnológico, la Inteligencia Artificial “no sustituye al médico, sino que potencia sus capacidades y le ayuda a realizar su trabajo en menos tiempo” (Higuera, 2023). Y pasa lo mismo en otros muchos escenarios, como la educación. Hay que destacar el hecho de que la IA supone un impulso hacia el progreso y la innovación, pero aplicarla en el aula no supone en sí innovación. Para que exista realmente una innovación en el aula,  no basta solo con introducir la tecnología y la IA, sino que hay que replantear el modelo de educación existente, y con ello replantear qué es realmente aprender y educar, remodelar esas técnicas de memorización a día de hoy existentes y adoptar un paradigma educativo transformador que incluya nuevas tecnologías y se aproveche de sus beneficios. 
            \n
            Llevar al aula la inteligencia artificial es una cuestión compleja, pero si realmente la vemos y utilizamos únicamente  como un medio, que ayude a la sociedad a ser mejor, a ahorrar tiempo, a acceder a la información rápidamente, y  no como un fin, conseguiremos el propósito que tiene este blog, aplicar la IA en la educación. En relación a los profesores, seguirá siendo necesario que haya una intervención humana, una persona que sienta, que pueda crear una conexión con los alumnos, las familias y sus compañeros, y que pueda pensar por sí solo y tomar decisiones.  Hay que tener claro que la IA no puede sustituir a los seres humanos, pero sí puede ayudar con la carga de trabajo de los educadores. Sumandonos al artículo “La inteligencia artificial en la educación” ( 2024), podemos tratar los siguientes puntos: 
            \n
            #### ¿Trabajar con IA mejora la enseñanza?
            \n
            Introducir la IA en el campo educativo significa preparar a los alumnos para un futuro, ya que esta ocupará un papel integral en sus vidas, tanto personales como laborales. Permitirá crear entornos de aprendizaje personalizados, adaptativos e innovadores, que a su vez facilitará el desarrollo de estrategias de  adquisición de conocimiento por parte del alumno y proporcionará a la IA la información necesaria para generar estrategias efectivas de enseñanza, basadas en sus análisis predictivos y evaluativos. También, aplicarla en la educación supone una automatización en las  tareas administrativas, lo que permite a los educadores centrarse más en enseñar y orientar a los estudiantes. Además debemos tener en cuenta que podría potenciar la creatividad de los alumnos y funcionar como un sistema de apoyo para docentes y abordar temas éticos, a través de asistentes de IA en clase. Asimismo, los maestros podrán recurrir a la IA para tratar cuestiones complejas de una manera más accesible y comprensible  para todos y todas. Para poder conseguirlo y aplicarlo debe haber un cambio trascendental, una formación docente muy elevada y a su vez es adecuado que los propios alumnos aprendan a integrar en sus vidas la IA de manera justa, eficaz, ética y efectiva. 
            \n
            #### Personalizar la enseñanza con la ayuda de la IA
            \n
            Introducir herramientas de IA en el campo educativo ofrece muchas oportunidades para mejorar la enseñanza y el aprendizaje. Los maestros pueden recurrir a ciertas plataformas que permitirán un aprendizaje personalizado  adaptativo al nivel del estudiante.  Usar la IA en la educación significa que ayuda al docente a adaptar el material de las Necesidades Educativas Especiales(NEE). Trabajar con IA supone un ajuste al nivel de las dificultades que puede presentar el alumno y a su ritmo de aprendizaje. Además, la IA podría darles desafíos y materiales que los alumnos necesitan practicar más. 
            \n
            Se pueden utilizar diferentes software de tutoría inteligente, que funcionarán como una apoyo para los alumnos fuera del colegio. Esto podría personalizar explicaciones, ofrecer más práctica a los alumnos e introducir feedback en los lugares que más lo necesiten. Y por último, las herramientas IA pueden analizar datos de rendimiento académico e identificar tendencias y patrones, colaborando así con los maestros en la detección de posibles dificultades de aprendizaje.  En resumen, estas herramientas pueden mejorar la experiencia educativa, funcionar como apoyo para docentes y alumnos y abrir un abanico de experimentación y descubrimiento. 
            \n
            #### ¿Qué habilidades pueden desarrollarse a través de la IA?
            \n
            - Se pueden desarrollar habilidades técnicas como la comprensión, programación y codificación.
            - Los estudiantes que trabajen con IA pueden aprender a recopilar, procesar y analizar datos. 
            - La capacidad crítica y analítica aumentará considerablemente. 
            - Se aplica la resolución de problemas en situaciones de aprendizajes y situaciones reales.
            - Se promueve la creatividad e innovación.
            - Los niños que trabajan con IA aprenden a colaborar y a trabajar en equipo a través de proyectos interdisciplinares, permitiendo ver las distintas perspectivas que hay en un mismo grupo
            - Permite que los niños aprendan a adaptarse al cambio, lo que van a ver mucho en su día a día.
            \n
            #### ¿Cómo evolucionará la relación entre el aula y la IA en el futuro?
            \n
            Está previsto que en 2024 la Inteligencia Artificial sea llevada al aula a un escenario real y permitirá un avance a situaciones de necesidades específicas de los alumnos, funcionará como una apoyo para preparar las asignaturas, proporcionará servicios innovadores en la educación, creará obras visuales complejas, se conseguirá una  fusión entre metodologías pedagógicas innovadoras y activas y las tecnologías avanzadas y por último permitirá al profesorado la creación de recursos de aprendizaje.
            \n
            ![IA2024](https://github.com/jorgesaenzdemiera/archivos/blob/main/images/Captura%20de%20pantalla%202024-05-28%20192618.png?raw=true)
            \n
            ## Conclusiones
            En definitiva, este blog confía en lo favorable que es utilizar la Inteligencia Artificial en nuestras vidas, ya que la puede llegar a mejorar mucho, pero también es necesario proporcionar planes de cómo utilizarla, intervenciones éticas-morales y en la que se nos limite a usarla si provoca algún tipo de problema. Es un arma de doble filo y al igual que arregla nuestras vidas puede destruirla si no tenemos cuidado. Está en nuestras manos avanzar globalmente con la ayuda de estas entidades, pero también está en nuestras manos utilizarla siempre para el bien.
            \n""")
st.write('')
st.write('')
st.write("Autor: **Jorge Sáenz de Miera**")
