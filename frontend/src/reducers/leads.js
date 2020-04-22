//The way we define these is called types
import { GET_LEADS, DELETE_LEAD, ADD_LEAD } from "../actions/types.js";
//Get_Leads -> Get the leads from the backend and display them here

const initialState = {
  leads: []
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_LEADS:
      return {
        ...state,
        leads: action.payload
        //send those leads as a payload in the action
      };
    case DELETE_LEAD:
      return {
        ...state,
        leads: state.leads.filter(lead => lead.id != action.payload)
      };
    case ADD_LEAD:
      return {
        ...state,
        leads: [...state.leads, action.payload]
      };
    default:
      return state;
  }
}
