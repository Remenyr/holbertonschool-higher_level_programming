$('DIV#add_item').on('click', function () {
    const created = document.createElement('li');
    const item = $(created).text('Item');
    $('UL.my_list').append(item);
  });
