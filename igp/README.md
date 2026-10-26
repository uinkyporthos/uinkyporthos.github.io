# PORTHOS · publicación automática en Instagram (@_.porthos._)

Mismo sistema que ÜINKY (`ig/`), Bataká y TOROTE: cada 30 minutos el workflow **«Instagram PORTHOS»** publica en **@_.porthos._** lo de `igp/queue.json` que ya venció **y** tiene `"aprobado": true`. Los archivos se sirven desde `https://uinkyporthos.github.io/igp/...`.

## Lote 1 · mar 27 oct – dom 1 nov 2026 (36 publicaciones)
- **Feed, 3 al día (09:00 · 13:00 · 19:00):** 18 piezas, entre ellas 4 carruseles y 3 reels (máx. 12 s, sin audio).
- **Stories, 3 al día (08:30 · 13:30 · 20:30):** una palabra a la mañana, un dato al mediodía y el pedido a la noche.
- Todo entra con `"aprobado": false`. **Nada se publica hasta que lo apruebes.**

## Puesta en marcha (una sola vez)
1. @_.porthos._ tiene que ser cuenta profesional (Business o Creator).
2. App de Meta «TOROTE» → App roles → agregar @_.porthos._ como **Instagram Tester** → aceptar la invitación en instagram.com/accounts/manage_access/.
3. En la app: Use cases → API setup with Instagram login → **Generate token** para @_.porthos._.
4. Secretos en *Settings → Secrets and variables → Actions* de este repo:
   - `IG_TOKEN_PORTHOS` — el token (**nunca en un chat ni en un archivo**)
   - `IG_USER_ID_PORTHOS` — el ID de la cuenta
   - `GH_PAT` *(opcional, compartido con ÜINKY)* — para guardar el token renovado
5. *Actions → Instagram PORTHOS → Run workflow → `check`* → debe decir `Token OK -> _.porthos._`.

## Día a día
- **Aprobar:** cambia `"aprobado": false` a `true` y haz commit.
- **Si apruebas tarde:** `python scripts/mover_fechas_porthos.py desde 2026-10-28` (o `... 1` para correr todo un día).
- **Pausar:** vuelve a `false`. **Revisar:** *Run workflow → `validate`*. **Registro:** `igp/published.json`.

Reglas: sin precios; único texto en francés, «Formule française»; sobre los videos solo el nombre del jabón; cuadros en carbón #262221 con filete oro #B49C78.
