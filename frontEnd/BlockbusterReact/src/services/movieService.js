import http from "./httpService";

const apiEndpoint = "http://127.0.0.1:8000/api/movie/";

export function getMovies() {
  return http.get(apiEndpoint);
}

export function getMovie(movieId) {
  return http.get(apiEndpoint + movieId);
}

export function saveMovie(movie, genres) {
  let genre = "";
  console.log("genres: " + JSON.stringify(genres));
  for (var i = 0; i < genres.length; i++) {
    console.log("gen.id: " + genres[i].id + " genre id: " + movie.genreId);
    if (genres[i].id == movie.genreId) {
      movie.genre = { id: movie.genreId, name: genres[i].name };
    }
    console.log("movie genre: " + JSON.stringify(movie.genre));
  }

  if (movie.id) {
    const body = { ...movie };
    delete body.id;
    body.genreId = parseInt(body.genreId);
    body.liked = "false";

    console.log(apiEndpoint + "edit/" + movie.id, JSON.stringify(body) + "/");
    return http.put(apiEndpoint + "edit/" + movie.id + "/", body);
  }
  movie.liked = "false";
  console.log(apiEndpoint + "create/", JSON.stringify(movie));
  return http.post(apiEndpoint + "create/", movie);
}

export function deleteMovie(movieId) {
  return http.delete(apiEndpoint + "delete/" + movieId);
}
