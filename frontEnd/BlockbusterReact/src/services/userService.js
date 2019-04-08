import http from "./httpService";
import { register } from "../serviceWorker";

const apiEndpoint = "http://127.0.0.1:8000/api/users/";

// export function register(user) {
//   return http.post(apiEndpoint, {
//     email: user.username,
//     password: user.password,
//     name: user.name
//   });
// }
