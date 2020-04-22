# Lead Manager 

  Full stack Django/React/Redux application with token-based authentication with Knox. 
  Project is deployed and running at https://sean-lead-manager.herokuapp.com

# Project Structure
 * The base directory configures the server build (source code in *server/*, see below)
```bash
leadmanager/           
|   
|___accounts/            
|___frontend/        
|______src/)        
|_________actions/)       # Actions - user/leads/message
|_________componets/)       # Components Accounts/Common/Layout/Leads
|____________accounts/)       # Login/Register
|____________common/)       # PrivateRoute
|____________layout/)       # Header/Alerts
|____________leads/)       # Dashboard/Form/Leads
|_________reducers/)       # Reducer - Auth/Erros/Index/Leads/Messages
|___leadmanager/                 
|___leads/        
```

## Build 
* Dependencies
  * npm install

* Run webpack (For DEV)
  * npm run dev

* Build production (For Production)
  * npm run build

* Launch Server
  * cd leadmanager
  * python manage.py runserver

## Reference 

* https://www.youtube.com/watch?v=Uyei2iDA4Hs&list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60
- A very thorough tutorial by Travery Media
