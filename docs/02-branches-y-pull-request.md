\# 🌿 Branches y Pull Requests - Flujo Profesional



\*\*Fecha:\*\* 16 de Marzo de 2026  

\*\*Autor:\*\* patoraya2



\---



\## ¿Qué es un Branch (Rama)?



Un \*\*branch\*\* es una \*\*línea de desarrollo independiente\*\* dentro del mismo repositorio.



\### Analogía

Imagina un árbol:

\- El \*\*tronco\*\* es `main` (la rama principal, producción)

\- Las \*\*ramas pequeñas\*\* son `feature/\*`, `bugfix/\*` (donde trabajamos)



\### Beneficios

\- 🔒 `main` siempre está seguro (no tocar directo)

\- 🔄 Puedo trabajar en múltiples features a la vez

\- 👥 Mis compañeros trabajan en otras ramas sin conflictos

\- 🛡️ Cambios se revisan antes de entrar a `main`



\---



\## ¿Qué es un Pull Request (PR)?



Un \*\*Pull Request\*\* es una \*\*solicitud para mergear cambios\*\* de una rama a otra.



\### Es como decir:

\*"Oye equipo, hice cambios en mi rama. ¿Pueden revisar si está bien antes de ponerlo en main?"\*



\### Flujo

```

Mi rama (feature/x) 

&#x20;   ↓

Hago cambios

&#x20;   ↓

Hago commit

&#x20;   ↓

Hago push

&#x20;   ↓

Abro Pull Request en GitHub

&#x20;   ↓

Alguien revisa (code review)

&#x20;   ↓

Se aprueba

&#x20;   ↓

Se mergea a main

```



\---



\## Comandos Principales



\### Crear una rama

```bash

git checkout -b feature/nombre

```

O en versiones nuevas:

```bash

git switch -c feature/nombre

```



\### Ver todas las ramas

```bash

git branch

```



Muestra:

```

\* feature/mi-primer-ejemplo  ← Estoy aquí (asterisco)

&#x20; main

```



\### Cambiar de rama

```bash

git checkout main

```



\### Ver ramas remotas

```bash

git branch -a

```



Muestra:

```

\* main

&#x20; feature/mi-primer-ejemplo

&#x20; remotes/origin/main

&#x20; remotes/origin/feature/mi-primer-ejemplo

```



\### Eliminar una rama local

```bash

git branch -d feature/nombre

```



\### Eliminar una rama remota

```bash

git push origin --delete feature/nombre

```



\---



\## Lo Que Hice Hoy - Paso a Paso



\### 1️⃣ Creé una rama nueva

```bash

git checkout -b feature/mi-primer-ejemplo

```



\### 2️⃣ Hice cambios (creé un script Python)

Creé el archivo: `ejemplos/01-hola-mundo.py`



\### 3️⃣ Verifiqué los cambios

```bash

git status

```



\### 4️⃣ Agregué los cambios

```bash

git add ejemplos/01-hola-mundo.py

```



\### 5️⃣ Hice commit

```bash

git commit -m "feat: Agregar primer script Python - Hola Mundo"

```



\### 6️⃣ Hice push a GitHub

```bash

git push origin feature/mi-primer-ejemplo

```



GitHub respondió con:

```

Create a pull request for 'feature/mi-primer-ejemplo' on GitHub by visiting:

https://github.com/patoraya2/aprendiendo-vibecodingn8n/pull/new/feature/mi-primer-ejemplo

```



\### 7️⃣ Abrí un Pull Request en GitHub

\- Clickeé en "Compare \& pull request"

\- Llené el título y descripción

\- Clickeé "Create pull request"



\### 8️⃣ Mergeé el PR a main

\- Clickeé "Merge pull request"

\- Clickeé "Confirm merge"

\- GitHub hizo: `Merge pull request #1 from patoraya2/feature/mi-primer-ejemplo`



\### 9️⃣ Sincronicé mi computadora

```bash

git checkout main

git pull origin main

```



\### 🔟 Verifiqué que todo estaba bien

```bash

git log --oneline

```



Resultado:

```

9b77c17 Merge pull request #1 from patoraya2/feature/mi-primer-ejemplo

a65979c feat: Agregar primer script Python - Hola Mundo

8f8e6b5 docs: Agregar documentación de Git básico

47d0960 docs: Crear estructura inicial del proyecto y README documentado

96fc2d4 Initial commit

```



\---



\## 📋 Convenciones de Nombres para Branches



\### Tipos de branches

```

feature/\*      → Nuevas funcionalidades

bugfix/\*       → Arreglar bugs

hotfix/\*       → Arreglos urgentes en producción

docs/\*         → Cambios en documentación

refactor/\*     → Refactorización de código

test/\*         → Cambios en tests

```



\### Ejemplos

```

feature/agregar-autenticacion

bugfix/arreglar-login

docs/actualizar-readme

refactor/optimizar-database

```



\### Mi rama

```

feature/mi-primer-ejemplo ✅ (Bien nombrada)

```



\---



\## 📋 Convenciones de Mensajes en Commits



\### Formato

```

tipo: descripción breve

```



\### Tipos

```

feat:       Nueva funcionalidad

fix:        Arreglo de bug

docs:       Cambios en documentación

refactor:   Cambio de código sin agregar funcionalidad

test:       Agregar o modificar tests

chore:      Cambios de configuración

style:      Cambios de formato (sin lógica)

perf:       Mejora de rendimiento

```



\### Ejemplos

```

feat: Agregar primer script Python - Hola Mundo

docs: Agregar documentación de Git básico

fix: Arreglar error en el login

refactor: Optimizar funciones de autenticación

```



\---



\## Lecciones Aprendidas



✅ Los branches protegen `main`  

✅ Los PRs permiten code review  

✅ Todo desarrollador debe saber esto  

✅ Es el flujo estándar de la industria  

✅ La documentación en PRs es importante  

✅ Los nombres de ramas deben ser claros  

✅ Los mensajes de commit deben ser descriptivos  



\---



\## El Flujo Profesional



```

┌─────────────┐

│   main      │ (Rama principal, siempre funciona)

└──────┬──────┘

&#x20;      │

&#x20;      └─────────────┐

&#x20;                    │

&#x20;             ┌──────▼─────────┐

&#x20;             │ feature/nueva  │ (Mi rama de trabajo)

&#x20;             └──────┬─────────┘

&#x20;                    │

&#x20;            (Hago cambios, commits)

&#x20;                    │

&#x20;             ┌──────▼─────────┐

&#x20;             │  Push a GitHub │

&#x20;             └──────┬─────────┘

&#x20;                    │

&#x20;             ┌──────▼──────────────┐

&#x20;             │  Abro Pull Request  │

&#x20;             └──────┬──────────────┘

&#x20;                    │

&#x20;             ┌──────▼──────────────┐

&#x20;             │  Code Review (OK)   │

&#x20;             └──────┬──────────────┘

&#x20;                    │

&#x20;             ┌──────▼──────────────┐

&#x20;             │  Merge a main       │

&#x20;             └──────┬──────────────┘

&#x20;                    │

&#x20;      ┌─────────────▼──────────────┐

&#x20;      │        main (actualizado)  │

&#x20;      └────────────────────────────┘

```



\---



\## Próximos Pasos



\- \[ ] Aprender a resolver conflictos en Git

\- \[ ] Entender estrategias de branching (Git Flow)

\- \[ ] Revisar PRs de otros

\- \[ ] Dominar rebase vs merge

\- \[ ] Aprender sobre squash commits



\---



\## Notas Personales



Hoy aprendí el flujo profesional COMPLETO que usan todos los desarrolladores del mundo.

Esto es lo que hace que los equipos trabajen sin pisarse unos a otros.



\*\*Última actualización:\*\* 16/03/2026

