# Lead Manager 

  Full stack Django/React/Redux application with token-based authentication with Knox. 

# Project Structure
 * The base directory configures the server build (source code in *server/*, see below)
```bash
leadmanager/           # Node.JS server which serves the client bundle, and handles HTTP requests 
|                   # (uses TypeScript, Express.JS)
|___accounts/           # Nested React project (uses TypeScript, Bootstrap)
|___frontend/       # React boilerplate used to build bundle. Probably don't ever need to edit
|______src/)       # Server JavaScript output, compiled from ../server/
|_________actions/)       # Server JavaScript output, compiled from ../server/
|_________componets/)       # Server JavaScript output, compiled from ../server/
|____________accounts/)       # Server JavaScript output, compiled from ../server/
|____________common/)       # Server JavaScript output, compiled from ../server/
|____________layout/)       # Server JavaScript output, compiled from ../server/
|____________leads/)       # Server JavaScript output, compiled from ../server/
|_________reducers/)       # Server JavaScript output, compiled from ../server/
|___leadmanager/          # React TypeScript code        
|___leads/       # Client JavaScript, HTML, CSS bundle, compiled from ../client/
```

## Build 
* Dependencies
npm install

* Run webpack (For DEV)
npm run dev

* Build production (For Production)
npm run build

* Launch Server
cd leadmanager
python manage.py runserver

## Reference 

* https://www.youtube.com/watch?v=Uyei2iDA4Hs&list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60
  * Tutorial by Travery Media
