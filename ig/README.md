# ÜINKY · publicación automática en Instagram (@uinky__)

Mismo sistema que Bataká y TOROTE: cada 30 minutos un GitHub Action publica en **@uinky__** lo de `ig/queue.json` que ya venció **y** tiene `"aprobado": true`. Los archivos se sirven desde este mismo sitio (`https://uinkyporthos.github.io/ig/...`).

## Lote 1 · 28 oct – 10 nov 2026 (56 publicaciones)

- **Feed, 19:00:** 14 piezas — 5 carruseles, 5 posts y 4 reels.
- **Stories, 09:00 · 13:00 · 20:30:** 42 en total — «le mot du jour» en la mañana, un dato o pregunta al mediodía y un pedido en la noche.
- Todo entra con `"aprobado": false`. **Nada se publica hasta que lo apruebes.**

## Puesta en marcha (una sola vez)

1. **Cuenta:** @uinky__ tiene que ser profesional (Business o Creator). Desde la app: Configuración → Tipo de cuenta y herramientas.
2. **App de Meta:** en developers.facebook.com → *Crear app* → caso de uso **«Administrar mensajes y contenido en Instagram»**. En *Configuración de la API con inicio de sesión de Instagram*, agrega @uinky__ y concede `instagram_business_basic` e `instagram_business_content_publish`. Pulsa **Generar token** y copia también el **ID de usuario de Instagram**. Puedes reutilizar la app de TOROTE o Bataká y solo agregar la cuenta.
3. **Secretos** en *Settings → Secrets and variables → Actions* de este repo:
   - `IG_TOKEN` — el token
   - `IG_USER_ID` — el ID
   - `GH_PAT` *(opcional)* — token fino de GitHub con «Secrets: Read and write» solo en este repo, para guardar el token renovado
   
   **Nunca pegues el token en un chat ni en un archivo.**
4. **Probar:** *Actions → Instagram ÜINKY → Run workflow → `check`*. Tiene que decir `Token OK -> uinky__`.

## Día a día

- **Aprobar:** cambia `"aprobado": false` a `true` (todo el lote o pieza por pieza) y haz commit.
- **Si apruebas tarde:** lo vencido sale todo junto. Antes de aprobar corre `python scripts/mover_fechas.py desde 2026-11-02` (o `mover_fechas.py 3` para correr todo 3 días).
- **Pausar algo:** vuelve a ponerlo en `false`.
- **Revisar sin publicar:** *Run workflow → `validate`*.
- **Registro:** `ig/published.json`.

Los reels del cielo, del jardín y de «les quatre» van sin sonido (las tomas originales no tienen audio). El del taller lleva el sonido real del corte y del mazo.
