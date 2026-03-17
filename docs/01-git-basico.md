\# 📚 Git Básico - Mi Primer Aprendizaje



\*\*Fecha:\*\* 16 de Marzo de 2026  

\*\*Autor:\*\* patoraya2



\---



\## ¿Qué es Git?



Git es un \*\*sistema de control de versiones\*\* que me permite:

\- 📝 Guardar versiones de mi código

\- 🔄 Volver a versiones anteriores si algo sale mal

\- 👥 Colaborar con otros desarrolladores

\- 📊 Ver el historial de cambios



\---



\## Conceptos Principales



\### Repository (Repositorio)

Es una carpeta que contiene mi proyecto y todo su historial de cambios.



\*\*Ejemplo:\*\* `aprendiendo-vibecodingn8n/` es mi repositorio.



\### Commit

Es una "foto" de mi código en un momento específico. Cada commit tiene:

\- Un mensaje describiendo qué cambié

\- Quién hizo el cambio

\- Cuándo se hizo

\- Qué archivos se modificaron



\*\*Ejemplo:\*\* `git commit -m "docs: Crear estructura inicial"`



\### Branch (Rama)

Es una línea de desarrollo independiente. La rama principal se llama `main` o `master`.



\*\*Ejemplo:\*\* Puedo tener una rama `main` y otra `desarrollo`.



\### Push

Es enviar mis commits locales a GitHub para compartirlos.



\*\*Ejemplo:\*\* `git push origin main`



\### Clone

Es descargar un repositorio de GitHub a mi computadora.



\*\*Ejemplo:\*\* `git clone https://github.com/patoraya2/aprendiendo-vibecodingn8n.git`



\---



\## Comandos Que Aprendí



| Comando | Qué hace |

|---------|----------|

| `git init` | Inicia un nuevo repositorio local |

| `git clone <url>` | Descarga un repo de GitHub |

| `git status` | Muestra estado actual |

| `git add <archivo>` | Agrega archivo para guardar |

| `git commit -m "mensaje"` | Guarda los cambios |

| `git push origin main` | Envía cambios a GitHub |

| `git log` | Muestra historial de commits |



\---



\## Mi Flujo de Trabajo



\### Paso 1: Crear/Clonar repositorio

```bash

git clone https://github.com/patoraya2/aprendiendo-vibecodingn8n.git

cd aprendiendo-vibecodingn8n

```



\### Paso 2: Hacer cambios

\- Edito archivos

\- Creo nuevas carpetas

\- Escribo código



\### Paso 3: Verificar cambios

```bash

git status

```



\### Paso 4: Preparar cambios

```bash

git add <archivo>

\# O agregar todo:

git add .

```



\### Paso 5: Guardar cambios

```bash

git commit -m "Mensaje descriptivo"

```



\### Paso 6: Enviar a GitHub

```bash

git push origin main

```



\---



\## Lo Que Hice Hoy



1\. ✅ Creé un repositorio en GitHub llamado `aprendiendo-vibecodingn8n`

2\. ✅ Clonarlo a mi computadora

3\. ✅ Creé estructura de carpetas (`docs/`, `ejemplos/`, `proyectos/`, `recursos/`)

4\. ✅ Edité el README.md con documentación

5\. ✅ Hice mi primer commit: `docs: Crear estructura inicial del proyecto`

6\. ✅ Hice push a GitHub



\---



\## Lecciones Aprendidas



\- Git es fundamental para cualquier desarrollador

\- La documentación es importante desde el inicio

\- Los commits deben tener mensajes claros y descriptivos

\- La repetición ayuda a memorizar los comandos

\- GitHub es donde vive mi código en línea



\---



\## Próximos Pasos



\- \[ ] Aprender sobre ramas (branches)

\- \[ ] Entender Pull Requests (PRs)

\- \[ ] Aprender a resolver conflictos

\- \[ ] Dominar Git workflow profesional



\---



\## Notas Personales



Este archivo será mi referencia cada vez que olvide algo de Git. La documentación es poder.



\*\*Última actualización:\*\* 16/03/2026

