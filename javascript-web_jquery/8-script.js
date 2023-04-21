$(function () {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
      const results = data.results;
      for (const tt of results) {
        const created = document.createElement('li');
        const item = $(created).text(tt.title);
        $('#list_movies').append(item);
      }
    });
  });
