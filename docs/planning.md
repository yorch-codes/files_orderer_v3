# Planning

## Idea

Quiero automatizar la organización de archivos para evitar ordenar carpetas manualmente.

## Problem

Cuando una carpeta acumula muchos archivos, organizarlos por tipo consume tiempo y genera desorden.

## Objetive

Crear un script en Python que organice archivos automáticamente en carpetas según su extensión usando `typer` y `pathlib`.

## MVP (Do it)

Para mantenerlo aterrizado:

```shell
✓ recibir ruta del usuario
✓ validar directorio
✓ recorrer archivos
✓ crear carpetas por extensión
✓ mover archivos automáticamente
✓ usar typer y pathlib
```

## Don't do it (v1)

Aquí nos protegemos.

```shell
✗ interfaz gráfica
✗ TUI
✗ reorganizar directorios
✗ configuración avanzada
✗ IA
✗ logging completo
```

## Flow

```shell
Usuario ejecuta script con ruta del directorio
↓
Se valida directorio
↓
Se recorre archivos
↓
Se crean carpetas por extensión
↓
Se mueven archivos
↓
Confirmación final
```

## Future Ideas (V2+)

```shell
-> resumen de archivos movidos
-> dry-run (simulación)
-> soporte para subdirectorios
-> categorías personalizadas
-> archivos de configuración
```
